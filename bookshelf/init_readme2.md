# Setup the Bookshelf Database

(venv) jeff@Jeff-Ryzen7:~/fswd_dev/bookshelf/backend$ sudo -iu postgres psql < setup.sql
[sudo] password for jeff:
NOTICE:  database "bookshelf" does not exist, skipping
DROP DATABASE
NOTICE:  database "bookshelf_test" does not exist, skipping
DROP DATABASE
ERROR:  role "student" cannot be dropped because some objects depend on it
DETAIL:  privileges for database plantsdb
owner of table plants
owner of sequence plants_id_seq
2 objects in database plantsdb
CREATE DATABASE
CREATE DATABASE
ERROR:  role "student" already exists
GRANT
GRANT
ALTER ROLE
ALTER ROLE


# Populate Books Table
(venv) jeff@Jeff-Ryzen7:~/fswd_dev/bookshelf/backend$ sudo -iu postgres psql bookshelf< books.psql
SET
SET
SET
SET
 set_config
------------

(1 row)

SET
SET
SET
SET
SET
SET
DROP TABLE
CREATE TABLE
ALTER TABLE
DROP SEQUENCE
CREATE SEQUENCE
ALTER TABLE
ALTER SEQUENCE
ALTER TABLE
COPY 16
 setval
--------
     22
(1 row)

ALTER TABLE
(venv) jeff@Jeff-Ryzen7:~/fswd_dev/bookshelf/backend$