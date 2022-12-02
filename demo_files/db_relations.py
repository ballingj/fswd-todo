"""
Making table relationship.
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate

app = Flask(__name__)

# need to define the URI to connect to our database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/example'

#
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# This will link an instance of database that we can
# interact with SQLAlchemy to our Flask app
db = SQLAlchemy(app)

# Add flask migrate
migrate = Migrate(app, db)

# SQLAlchemy's way of initializing instance of a table

# Parent Table 
class Driver(db.Model):
    __tablaname__ = 'driver'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    state = db.Column(db.String)
    vehicles = db.relationship('Vehicle', backref='driver', lazy=True)

# child table
class Vehicle(db.Model):
    __tablename__ = 'vehicle'
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String)
    model = db.Column(db.String)
    year = db.Column(db.Integer)
    driver_id = db.Column(db.Integer, db.ForeignKey('driver.id'), nullable=False)

# no longer required when using migrations
# db.create_all()


@app.route('/')
def index():
    return "Hello, Welcome to DMV"


# querying contents of the database & grab first record
@app.route('/driver')
def driver():
    drivers = Driver.query.all()
    return f'Hello {drivers[0].name}'


# querying contents of the database & grab some record
@app.route('/vehicle')
def vehicle():
    vehicles = Vehicle.query.all()  # returns a list
    # show the name in index
    return f'Vehicle: {vehicles[0].make} {vehicles[0].model}!'


if __name__ == '__main__':
    # set the debug mode to on
    app.debug = True
    app.run(host="0.0.0.0", port=4000)
