### Relashionship
```python
### parent class

class SomeParent(db.model):
    __tablename__ = 'someparents'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    children = db.relationship('SomeChild', backref='some_parent', lazy=True)


class SomeChild(db.Model):
    __tablename__ = 'somechildren'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    some_parent_id = db.Column(db.Integer, db.ForeignKey('someparents.id'), nullable=False)

```
Takeaways

SQLAlchemy configures the settings between model relationships once and generates JOIN statements for us whenever we need them.
db.relationship is an interface offered in SQLAlchemy to provide and configure a mapped relationship between two models.
db.relationship is defined on the parent model, and it sets:
    the name of its children (e.g. children), for example parent1.children
    the name of a parent on a child using the backref, for example:
      child1 = SomeChild(name='Andrew')
      child1.some_parent   // name of the backref -- returns the parent object that chil1 belongs to 



```python
# parent table
class Driver(db.Model):
    __tablaname__ = 'drivers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    state = db.Column(db.String)
    vehicles = db.relationship('Vehicle', backref='driver', lazy=True)

# child table
class Vehicle(db.Model):
    __tablename__ = 'vehicles'
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String)
    model = db.Column(db.String)
    year = db.Column(db.Integer)
    driver_id = db.Column(db.Integer, db.ForeignKey('drivers.id'), nullable=False)

```