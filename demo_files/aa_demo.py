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

cursor.execute('''
    INSERT INTO table2 (id, completed) VALUES (1, true);
''')

# drop any existing todos table
cursor.execute("DROP TABLE IF EXISTS todos;")

# (re)create the todos table
# (note: triple quotes allow multiline text in python)
cursor.execute("""
  CREATE TABLE todos (
    id serial PRIMARY KEY,
    description VARCHAR NOT NULL
  );
""")

conn.commit()

cursor.close()
conn.close()
