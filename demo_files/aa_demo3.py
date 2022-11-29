import psycopg2

# conn = psycopg2.connect('host= localhost dbname=example user=postgres password=postgres')
# alternatively:
conn = psycopg2.connect(
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432",
    database="example"
)

# open a cursor for db operations
cursor = conn.cursor()

# drop any existing table2 table
cursor.execute("DROP TABLE IF EXISTS table2;")

cursor.execute('''
    CREATE TABLE table2 (
        id INTEGER PRIMARY KEY,
        completed BOOLEAN NOT NULL DEFAULT False
    );
''')

# using 5s to use this function as a template
cursor.execute('INSERT INTO table2 (id, completed) VALUES (%s, %s);', (1, True))

# using the variable method
"""
cursor.execute('INSERT INTO table2 (id, completed)' +
    ' VALUES (%(id)s, %(completed)s);', {
      'id': 2, 
      'completed': False
    })
"""
SQL = 'INSERT INTO table2 (id, completed) VALUES (%(id)s, %(completed)s);'
data = {
  'id': 2,
  'completed': False
}
cursor.execute(SQL, data)

cursor.execute(
    'INSERT INTO table2 (id, completed) VALUES (%s, %s);', (3, True))

# Fetching data from the table
cursor.execute('SELECT * from table2;')

# fetchall grabs all the results
result = cursor.fetchall()
print('fetchall', result)

# fetchone grabs one record, but nothing else is left after fetch all above
result2 = cursor.fetchone()
print('fetchone', result2)

# let's refill result
cursor.execute('SELECT * from table2;')

# grab two data
result3 = cursor.fetchmany(2)
print('fetchmany(2)', result3)

result4 = cursor.fetchone()
print('fetchone', result4)

conn.commit()

cursor.close()
conn.close()
