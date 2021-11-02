import sys 
import os
import unittest
from sscanner import folderscan

test=["samplefolder",
    "https://github.com/Siddharth-Rajput/hacktoberFest.git",
    "exfolder"]
# AWSKEY = AKIAI7VM24AYPFD3VHMA
name = []
for i in range(len(test)):
    if "git" in test[i].split("."):
        os.system("git clone -q " + test[i])
        name.append(test[i].split("/").pop().split(".")[0])
    else: name.append(test[i])

class TestSum(unittest.TestCase):
    def test_1(self):
        result = folderscan(name[0],[],True,"f")
        self.assertEqual("Found 0 Permission error, 0 File Extension, 0 Secrets", result)
    def test_2(self):
        result = folderscan(name[1],[],True,"r")
        self.assertEqual("Found 0 Permission error, 0 File Extension, 0 Secrets", result)
    def test_3(self):
        result = folderscan(name[2],[],True,"f")
        self.assertEqual("Found 0 Permission error, 0 File Extension, 0 Secrets", result)
    def test_4(self):
        result = folderscan(name[2],[],True,"f")
        self.assertEqual("Found 0 Permission error, 0 File Extension, 0 Secrets", result)

if __name__ == '__main__':
    unittest.main()
