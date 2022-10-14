# Migrator
Database migrator

Migrator will avail after running run.py

Dynamics file and path:
- migration
- database
- setup.py file
- egg file

After run "run.py" edit the migrator.conf refer to your current database config and name.


1. generate configuration and setup file
    - py run.py

2. SQL as file
    - migrator generate-file-sql --sql path dbname -> on the folder inside project directory
    - migrator generate-file-sql --sql dbname -> on the parent/project directory
