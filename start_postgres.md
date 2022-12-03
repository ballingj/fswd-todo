
## How to start and stop PostgreSQL server?

In this post, we are going to figure out how to start, stop, and restart a PostgreSQL server on macOS, Linux, and Windows.

### On macOS

If you installed PostgreSQL via Homebrew:

    To start manually:
```
pg_ctl -D /usr/local/var/postgres start
```
    To stop manually:
```
pg_ctl -D /usr/local/var/postgres stop
```
    To start PostgreSQL server now and relaunch at login:
```
brew services start postgresql
```
    And stop PostgreSQL:
```
brew services stop postgresql
```

### On Windows

First, you need to find the PostgreSQL database directory, it can be something like C:\Program Files\PostgreSQL\10.4\data. Then open Command Prompt and execute this command:
```
pg_ctl -D "C:\Program Files\PostgreSQL\9.6\data" start
```
####  To stop the server
```
pg_ctl -D "C:\Program Files\PostgreSQL\9.6\data" stop
```
#### To restart the server:
```
pg_ctl -D "C:\Program Files\PostgreSQL\9.6\data" restart
```
#### Another way:

    Open Run Window by Winkey + R
    Type services.msc
    Search Postgres service based on version installed.
    Click stop, start or restart the service option.

### On Linux

By default, the postgres user has no password and can hence only connect if ran by the postgres system user. The following command will assign it:

sudo -u postgres psql -c "ALTER USER postgres PASSWORD 'postgres';"
sudo -u postgres psql -c "CREATE DATABASE testdb;"

#### Start the PostgreSQL server
```
sudo service postgresql start
```
#### Stop the PostgreSQL server:
```
sudo service postgresql stop
```

