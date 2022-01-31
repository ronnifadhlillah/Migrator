import click
import os
import sys
import migrator

# Written by Ronniawan Fadhlillah
# Migrator uses parts of `click`
# ==============================================================================

@click.group()
def main():
    """MIGRATOR : THE DATABASE MADE IN CLI"""

# Initialize database
# gsqlf: if using sqlite the file database will generate

@main.command()
@click.option('--db',nargs=1,type=str,help='TEXT replace with database name.')
def init(db):
    """Initialize new database."""
    if migrator.driver == 'sqlite':
        if os.path.isdir(migrator.cfg[migrator.driver]['path']) is False:
            os.makedirs(migrator.cfg[migrator.driver]['path'],777)
            os.chdir(migrator.cfg[migrator.driver]['path'])
            gsqlf=open(db+'.'+migrator.driver, "x")
            gsqlf.close()
            os.chdir('../')
            migrator.logResponse(0,db)
        else:
            print("""Folder %s and it's file is exists. Delete the folder to re-create the database.""" % migrator.cfg[migrator.driver]['path'])
            # input("would you want to delete the folder and it's file ? ")
            sys.exit()
    pass
    # replace with if database is using, sql server, mariadb / mysql

# Sometime, developer has write down a SQL syntax and ready to import to database. the code below is how to handle it.
# If path is not define it's return to None and make a .SQL file in project folder.
# Can generate in dynamic path / directory.
# Disallow duplicating file / folder / directory

@main.command()
@click.option('--sql',nargs=1,type=str,help='TEXT replace with SQL filename.')
@click.argument('path',nargs=1,default='None')
def generate(sql,path):
    """Generate .SQL file if needed."""
    # If path is not define, .sql file is create in current project folder
    if path == 'None':
        migrator.isFileExist(sql)
        gf=open(os.path.join(os.getcwd(),sql)+'.sql', "x")
        gf.close()
        migrator.logResponse(1)
    else:
    # Maybe .sql database is out of directory. Just tell the migrator the directory you want to generate
    # in migrator syntax
        migrator.isPathExist(path)
        os.makedirs(path,777)
        chdir(path)
        migrator.isFileExist(sql)
        gf=open(sql+'.sql', "x")
        gf.close()
        migrator.logResponse(2,args)
        print("""$s.SQL file has been created. Check %s folder""" % (sql,path))

# Makesure for .sql availability in directory
# argument migrator file-migrate

# Skip and will be edited

@main.command()
@click.option('--file-migrate',nargs=1,type=str,help='TEXT replace with SQL filename.')
@click.argument('path',nargs=1,default='None')
def fileMigrate():
    """Import .SQL file to database."""
    pass
