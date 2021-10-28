import subprocess
import sys
import os
import datetime

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

readme="""this is test
"""

def generate_setup():
    os.chdir(os.getcwd())
    sp=open('setup.py','w')
    sp.write(setup_scripts)
    sp.close()
    subprocess.check_call([sys.executable, "-m", "pip", "install","-q","-e","."])
    create_migration_folder()

def create_migration_folder():
        curr_time=datetime.datetime.now()
        fn=curr_time.strftime('%d%m%Y%H%I%S')+'db_config.conf'
        if os.path.isdir('migration') is False:
            os.mkdir('migration',777)
        wconfig=open('migrator.conf', "x")
        wconfig.write(readme)
        wconfig.close()
