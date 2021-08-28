# Code Explained

## Sscanner.py

I have set up some default regex which is used to match patterns for the file scanning. 

- **Summary function:**
This function is only called in normal mode i.e -q or —quiet=false. It show all the finding in a clean and organized manner for the user.
- **Folderscan function:**
This function traverse and scan the file with the regex provided. 
By default it scans for 777 file permission, this can be changed by passing file permission as argument.
It scans for some file extensions which are stored in **needed_ext** dictionary at the starting. In future it can also be passed as an argument.
While content scanning i have skipped the **.git** folder as it interfere with the regex and some file types like .pdf .png are also skipped. File extension which are skipped are stored in **escape_file** at the starting.
This function return a string which is used in unittesting.
- **Parser_error function:**
This function is used show error if wrong argument is passed.
- **Parse_args function:**
This function is used for parsing the argument and declaring the default values.

## Test.py

Three test cases are defined with unittest two for a folder and one for git repo. Inputs are stored in **test** dictionary. It runs by default runs in quiet mode.
These unit test will match a string returned by the folderscan function which was declared in sscanner.py.

## Github actions

Created a workflow in with github actions which gets triggered when [test.py](http://test.py) changes as it have the input details of the test.
