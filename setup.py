from setuptools import setup
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
