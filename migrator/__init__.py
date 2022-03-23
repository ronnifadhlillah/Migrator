from .init import *
from .log import *
import configparser

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

cfg=configparser.ConfigParser()
cfg.read(os.getcwd()+'/migrator.conf')
driver=cfg['database']['connection']
