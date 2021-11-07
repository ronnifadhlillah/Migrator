import subprocess
import sys
import os
import datetime
import migrator

setup_scripts="""from setuptools import setup

setup(
    name='migrator',
    version='1.0',
    py_modules=['migrator'],
    install_requires=['SQLAlchemy','Click','migrator'],
    entry_points='''
        [console_scripts]
        migrator=migrator.migrator:main
        '''
)
"""

def generate_setup():
    os.chdir(os.getcwd())
    sp=open('setup.py','w')
    sp.write(setup_scripts)
    sp.close()
    subprocess.check_call([sys.executable, "-m", "pip", "install","-q","-e","."])
    create_migration_folder()

def create_migration_folder():
        if os.path.isdir('migration') is False:
            os.mkdir('migration',777)
            # os.makedirs('migration/dataFactory')
            mlog=open('migration/migrator.log','x')
            mlog.close
            os.makedirs('migration/migrationPool')
        os.chdir(os.getcwd())
        try:
            wconfig=open('migrator.conf', "x")
            wconfig.write(migrator.conFile)
            wconfig.close()
        except FileExistsError as fee:
            print(""".conf file is exists.""")
