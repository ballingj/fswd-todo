############################################################
# This is the lowest level of interaction with
# database using the engine and raw sql in sqlalchemy
############################################################
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:postgres@localhost:5432/example')
conn = engine.connect()


conn.execute('DROP TABLE IF EXISTS table3;')

conn.execute('''
    CREATE TABLE table2 (
        id INTEGER PRIMARY KEY,
        description VARCHAR NOT NULL,
        completed BOOLEAN NOT NULL DEFAULT False
    );
''')

conn.execute('INSERT INTO table2 (id, description, completed) VALUES (%s, %s, %s);',
               (1, 'This is a thing1', True))

conn.execute('INSERT INTO table2 (id, description, completed) VALUES (%(id)s, %(description)s, %(completed)s);',
               {'id': 2, 'description': 'This is a thing2', 'completed': False})

SQL = 'INSERT INTO table2 (id, description, completed) VALUES (%(id)s, %(description)s, %(completed)s);'

data = {
    'id': 3,
    'description': 'This is a thing3',
    'completed': False
}
conn.execute(SQL, data)


result = conn.execute('SELECT * from table2;')

row = result.fetchone()
print(row)

rows = result.fetchall()
print(rows)
