import click
import configparser
import os
import sys

p=configparser.ConfigParser()
p.read(os.getcwd()+'/migrator.conf')
driver=p['database']['driver']


@click.group()
def main():
    """MIGRATOR : THE DATABASE MADE IN CLI"""

@main.command()
@click.option('--db',nargs=1,type=str,help='TEXT replace with database name.')
def init(db):
    """Initialize new database"""
    if driver == 'sqlite':
        if os.path.isdir(p[driver]['path']) is False:
            os.mkdir(p[driver]['path'],777)
            os.chdir(p[driver]['path'])
            wconfig=open(db+'.'+driver, "x")
            wconfig.close()
            print("""Database %s is successfully created. Check folder %s to view database file. """ % (db+'.'+driver,p[driver]['path']))
        else:
            print("""folder %s exists.""" % p[driver]['path'])
            sys.exit()
