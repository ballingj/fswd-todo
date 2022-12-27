# All lessons after this point is related to ORM
# Mapping between Tables and Classes

# Normal Class definition
class Human:
   def __init__(self, first_name, last_name, age):
       self.first_name = first_name
       self.last_name = last_name
       self.age= age

# instantiate some human class
sarah = Human("Sarah", "Silverman", 48)
bob = Human("Bob, Saget", 54)


# Table equivalent
'''
CREATE TABLE humans (
   id INTEGER PRIMARY KEY,
   first_name VARCHAR,
   last_name VARCHAR,
   age INTEGER
);


the takeaways: 
 - tables mapped to classes, 
 - table records mapped to class objects, and 
 - table columns mapped to the attributes within that class

'''
