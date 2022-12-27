from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# need to define the URI to connect to our database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/example'

# This will link an instance of database that we can
# interact with SQLAlchemy to our Flask app
db = SQLAlchemy(app)

# SQLAlchemy's way of initializing instance of a table


class Person(db.Model):
    __tablename__ = 'persons'   # by default lowercase name of class
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f"<Person: {self.name!r}>"


# actually creates that tables based on the db.Model that was configured
# if the table already exists, this will not do anything
with app.app_context():
    db.create_all()


@app.route('/')
def index():
    return 'Hello Everyone!'


if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=5001)
