The instruction stated to run the following:
su - postgres bash -c "dropdb plants"
su - postgres bash -c "createdb plants"
su - postgres bash -c "psql < /home/workspace/plantsdb/plantsdb-setupsql.sql"
su - postgres bash -c "psql plants < /home/workspace/plantsdb/plants.psql"

# However they do not work.  Instead do the following:
```
sudo -iu postgres psql plantsdb < plantsdb-setup.sql

sudo -iu postgres psql plantsdb < plants.psql
```

