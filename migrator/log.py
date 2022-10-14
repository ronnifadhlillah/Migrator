from migrator import conf
import os
import sys
import datetime
import configparser

# f: filename

def isFileExist(f):
    if os.path.exists(f+'.sql'):
        print(datetime.datetime.now(), """ --> %s.sql is exist. Delete first.""" % f)
        sys.exit()
    return True

# p: pathname

def isFolderExist(p):
    if os.path.isdir(p):
        print(datetime.datetime.now(), """ --> Folder is exist. Delete First""")
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
        0:ts() +' --> .SQL %s ha been generated. Check folder %s to view .SQL file. ' % (args,conf.cfg[conf.dbParsing()]['path']) , # Create folder and database file.
        1:ts() +' --> .SQL file has been created. Check project folder.', # Create files in .sql extension.
        2:ts() +' --> .SQL has been imported to database successfully. Check RDBMS', # Import .sql file to database.
        3:ts() +' --> '
    }
    wlog=open('migration\migration.log','a+')
    wlog.write(res[rb]+'\n')
    wlog.close()

    # print(res[int(rb)])


# I'ts return to [Timestamp] --> ['Verbose']
