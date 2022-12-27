"""
This file is demonstrating the 'R' in CRUD
Reading ToDo items
Exercise: getting user data in Flask ToDo App
"""

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# need to define the URI to connect to our database -- database must exist or created first
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/todoapp'
#
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'<todo {self.id} {self.description}>'


# actually creates that tables based on the db.Model that was configured
# if the table already exists, this will not do anything
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html', data=Todo.query.all())


if __name__ == '__main__':
    # set the debug mode to on
    app.debug = True
    app.run(host="0.0.0.0", port=5000)
