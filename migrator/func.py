import os
import sys

def isFileExist(f):
    if os.path.exists(f+'.sql'):
        print("""%s.sql is exist. Delete first.""" % f)
        sys.exit()
    return True

def isPathExist(p):
    if os.path.isdir(path):
        print("""Folder is exist. Delete First""")
        sys.exit()
    return True
