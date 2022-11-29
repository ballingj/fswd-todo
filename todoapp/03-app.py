"""
Using Ajax to send data to Flask
"""

from flask import Flask, render_template, request, redirect, url_for, jsonify
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


@app.route('/todos/create', methods=['POST'])
def create_todo():
    description = request.get_json()['description']   # get the value from the request body
    todo = Todo(description=description)  # create an instance Todo class
    # insert statement 
    db.session.add(todo)  # add to table 
    db.session.commit()   # write to db
    return jsonify({
        'description': todo.description
    })


if __name__ == '__main__':
    # set the debug mode to on
    app.debug = True
    app.run(host="0.0.0.0", port=5000)
