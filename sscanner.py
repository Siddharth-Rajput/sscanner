#!/usr/bin/python3
import sys, re, os, stat, argparse

regex = {"AWS Bucket0": "[a-z0-9.-]+\\.s3\\.amazonaws\\.com",
         "AWS Bucket1": "[a-z0-9.-]+\\.s3-[a-z0-9-]\\.amazonaws\\.com",
         "AWS Bucket2": "[a-z0-9.-]+\\.s3-website[.-](eu|ap|us|ca|sa|cn)",
         "AWS Bucket3": "//s3\\.amazonaws\\.com/[a-z0-9._-]+",
         "AWS Bucket4": "//s3-[a-z0-9-]+\\.amazonaws\\.com/[a-z0-9._-]+",
         "IP Address": "(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])",
         "Phone Number": "(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})",
         "Base 64": "([^A-Za-z0-9+/]|^)(eyJ|YTo|Tzo|PD[89]|aHR0cHM6L|aHR0cDo|rO0)[%a-zA-Z0-9+/]+={0,2}",
         "AWS Keys": "([^A-Z0-9]|^)(AKIA|A3T|AGPA|AIDA|AROA|AIPA|ANPA|ANVA|ASIA)[A-Z0-9]{12,}",
         "Email Address": '\S+@\S+'}


needed_ext = ["py","sh","bash","yaml"]
escape_file = ["pdf","png","jpg","md"]

def banner():
    print ('''
      
░█▀▀▀█ █▀▀ █▀▀ █▀▀█ █▀▀ ▀▀█▀▀ 　 ░█▀▀▀█ █▀▀ █▀▀█ █▀▀▄ █▀▀▄ █▀▀ █▀▀█ 
─▀▀▀▄▄ █▀▀ █── █▄▄▀ █▀▀ ──█── 　 ─▀▀▀▄▄ █── █▄▄█ █──█ █──█ █▀▀ █▄▄▀ 
░█▄▄▄█ ▀▀▀ ▀▀▀ ▀─▀▀ ▀▀▀ ──▀── 　 ░█▄▄▄█ ▀▀▀ ▀──▀ ▀──▀ ▀──▀ ▀▀▀ ▀─▀▀
    ''')

def summary(file_ext,file_fond,secret_fond):
    print("*********************")
    print("** SUMMARY OF SCAN **")
    print("*********************")
    print("%d files found with given permissions\n" % (len(file_fond)))
    for files in file_fond:
        mask = oct(os.stat(files).st_mode)[-3:]
        print("%s = > %s" % (mask, files))
    print("=============================")
    print("%d files found with given extensions\n" % (len(file_ext)))
    for files in file_ext:
        ext = files.split(".").pop()
        print("%s = > %s" % (ext, files))
    print("=============================")
    print("%d secrets found in the files \n" % (len(secret_fond)))
    for k,v in secret_fond.items():
        print("{} found in {}".format(k,v))
    print("=============================")


def folderscan(folder, permissions, quiet, repo):
    permissions = [int(item) for item in permissions]
    permissions.append(777)
    file_fond = []
    file_ext = []
    secret_fond = {}
    if os.path.exists(folder):
        for currentpath, folders, files in os.walk(folder):
            for file in files:
                if ".git" in currentpath.split("/"): continue  ## Ignoring the .git folder
                fullpath = os.path.join(currentpath, file)
                ext = fullpath.split(".").pop()
                mask = oct(os.stat(fullpath).st_mode)[-3:]

                ## Scanning for permissions
                if int(mask) in permissions: 
                    file_fond.append(fullpath)
                
                ## Scanning for extensions
                if ext in needed_ext: 
                    file_ext.append(fullpath)  
                
                ###  CONTENT SCANNING
                if ext in escape_file: continue  ## Ignoring pdf documents
                with open(fullpath, "r") as G:
                    content = G.read()
                for k, v in regex.items():
                    em = re.findall(v, content)
                    for i in range(len(em)): secret_fond[em[i]]=fullpath
                G.close()

        ## Returning Output for test case
        over = "Found {} Permission error, {} File Extension, {} Secrets".format(len(file_fond), len(file_ext), len(secret_fond))
        if quiet == False:
            summary(file_ext,file_fond,secret_fond)
        if repo == "r": os.system("sudo rm -r %s" % (folder))
    else:
        print ("Folder does not exist")
    return over

def parser_error(errmsg):
    #banner()
    print("Usage: python " + sys.argv[0] + " [Options] use -h for help")
    print("Error: " + errmsg)
    sys.exit()

def parse_args():
    # parse the arguments
    parser = argparse.ArgumentParser(epilog='\tExample: \r\npython3 ' + sys.argv[0] + " -i FolderLocation")
    parser.error = parser_error
    parser._optionals.title = "OPTIONS"
    parser.add_argument('-p', '--permissions', help='Scan the given permissions file only', default="777")
    parser.add_argument('-q', '--quiet', help='Scanner will not show Summary in detailed form', default=False)
    parser.add_argument('-i', '--input', help='Give a folder name or Git repo to scan', required=True)
    return parser.parse_args()

def main():
    args = parse_args()
    permissions = args.permissions.split(",")
    quiet = args.quiet
    folder = args.input
    banner()
    if "git" in folder.split("."):
        com = "git clone -q " + folder
        os.system(com)
        folder = folder.split("/").pop().split(".")[0]
        print("")
        print(folderscan(folder, permissions, quiet, "r"))
    else:
        print("")
        print(folderscan(folder, permissions, quiet, "f"))

if __name__ == "__main__":
    main()
