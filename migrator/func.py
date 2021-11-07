import os
import sys
import datetime
import migrator

# f: filename

def isFileExist(f):
    if os.path.exists(f+'.sql'):
        print("""%s.sql is exist. Delete first.""" % f)
        sys.exit()
    return True

# p: pathname

def isPathExist(p):
    if os.path.isdir(path):
        print("""Folder is exist. Delete First""")
        sys.exit()
    return True

# ts: timestamp %d/%m/%Y %H:%M:%S format
# generate current timestamp

def ts():
    return datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')

# rb: response int
# wlog: writting the log verbose
def logResponse(rb,args=None):
    res={
        0:ts() +' --> Database %s is successfully created. Check folder %s to view database file. ' % (args,migrator.cfg[migrator.driver]['path']) ,
        1:ts() +' --> .SQL file has been created. Check project folder.',
        2:ts() +' --> ',
        3:ts() +' --> '
    }
    wlog=open('migration\migration.log','a+')
    wlog.write(res[rb]+'\n')
    wlog.close()


# I'ts return to [Timestamp] --> ['Verbose']
