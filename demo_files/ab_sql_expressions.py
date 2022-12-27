############################################################
# sql expressions is the next level after engine
# interact with database using sqlexpressions in sqlalchemy
############################################################
from sqlalchemy import create_engine, Table, Column, Integer, String, Boolean, MetaData, select

engine = create_engine('postgresql://postgres:postgres@localhost:5432/example')
conn = engine.connect()

metadata = MetaData()

# Instantiate a new table
table4 = Table('table4', metadata,
               Column('id', Integer, primary_key=True),
               Column('description', String),
               Column('completed', Boolean, default=False),
               )

# Create the table
metadata.create_all(engine)

# insert a value into the table
ins = table4.insert().values(
    description='Clean a thing',
    completed=False
)

#
s = select([table4])

print(ins)
result = conn.execute(ins)
print(s)
result = conn.execute(s)

result.close()

print(table4.c.description)
