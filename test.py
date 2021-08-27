import sys 
import os
import unittest
from sscanner import folderscan

inputfile = "https://github.com/Siddharth-Rajput/hacktoberFest.git"
if "git" in inputfile.split("."):
        #com = "git clone " + folder 
        os.system("git clone " + inputfile)
        folder = inputfile.split("/").pop().split(".")[0]

class TestSum(unittest.TestCase):
    
    def test_int1(self):
        result = folderscan(folder,[],True)
        self.assertFalse(result)
    """ def test_int2(self):
        result = folderscan("exfolder",[],True)
        self.assertEqual(result, "hell3o")
    def test_int3(self):
        result = folderscan("exfolder",[],True)
        self.assertEqual(result, "hell3o") """

if __name__ == '__main__':
    unittest.main()
