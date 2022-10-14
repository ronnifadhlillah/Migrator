import configparser
import os

conFile="""[database]
  connection=sqlite

[sqlite]
  # SQLite database will generate automatically in database folder (database\db.sqlite) by default.
  # To change default directory change path definition beloww.
  path=database
  database=

[others]
  driverUrl=
  timezone=Asia\Jakarta
  prefix=
  """

# Passing configuration below
# Basic configuration setup is based on .conf file.
# The cfg prefix , from configuration file.
#

cfg=configparser.ConfigParser()

def dbParsing():
    cfg.read(os.getcwd()+'/migration/migrator.conf')
    return cfg['database']['connection']
