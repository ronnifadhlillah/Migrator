import click
import configparser
import os
import sys
import migrator

cfg=configparser.ConfigParser()
cfg.read(os.getcwd()+'/migrator.conf')
driver=cfg['database']['connection']

#The cfg prefix , from configuration file.

@click.group()
def main():
    """MIGRATOR : THE DATABASE MADE IN CLI"""

@main.command()
@click.option('--db',nargs=1,type=str,help='TEXT replace with database name.')
def init(db):
    """Initialize new database"""
    if driver == 'sqlite':
        if os.path.isdir(cfg[driver]['path']) is False:
            os.makedirs(cfg[driver]['path'],777)
            os.chdir(cfg[driver]['path'])
            gsqlf=open(db+'.'+driver, "x")
            gsqlf.close()
            print("""Database %s is successfully created. Check folder %s to view database file. """ % (db+'.'+driver,cfg[driver]['path']))
        else:
            print("""folder %s exists. Delete the folder and re-create the database.""" % cfg[driver]['path'])
            sys.exit()
    pass

# Sometime, there's developer has write a SQL syntax and ready to import to database. the code below is how to handle it.
# If path is not define it's return to None and make a .SQL file in project folder.
# Can genereate in dynamic path / directory.
@main.command()
@click.option('--sql',nargs=1,type=str,help='TEXT replace with sql filename.')
@click.argument('path',nargs=1,default='None')
def generate(sql,path):
    """Generate .SQL file if needed."""
    if path == 'None':
        migrator.isFileExist(sql)
        gf=open(os.path.join(os.getcwd(),sql)+'.sql', "x")
        gf.close()
        print(""".SQL file has been created. Check project folder""")
    else:
        migrator.isPathExist(path)
        os.makedirs(path,777)
        chdir(path)
        migrator.isFileExist(sql)
        gf=open(sql+'.sql', "x")
        gf.close()
        print("""$s.SQL file has been created. Check %s folder""" % (sql,path))
