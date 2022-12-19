"""
Database Relationship: One-to-Many
"""

from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask import abort
from flask_sqlalchemy import SQLAlchemy
import sys
from flask_migrate import Migrate


app = Flask(__name__)

# need to define the URI to connect to our database -- database must exist or created first
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/todoapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# define db migration
migrate = Migrate(app, db)

# child table of TodoList = contains the db.ForeignKey
class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)
    completed = db.Column(db.Boolean, nullable=False, default=False)
    list_id = db.Column(db.Integer, db.ForeignKey('todolists.id'), nullable=False)

    def __repr__(self):
        return f'<Todo {self.id!r} {self.description!r}, list {self.list_id!r}>'

# Parent table to Todo = contains the db.relationship and backref 
class TodoList(db.Model):
    __tablename__ = 'todolists'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    todos = db.relationship('Todo', backref='list', lazy=True)

    def _repr__(self):
        return f'<TodoList {self.id!r} {self.name!r}>'


@app.route('/')
def index():
    return render_template('index.html', data=Todo.query.order_by('id').all())
 

#route to create an item
@app.route('/todos/create', methods=['POST'])
def create_todo():
    error = False
    body = {}
    try:
        # get the value from the request body
        description = request.get_json()['description']
        todo = Todo(description=description)  # create an instance Todo class
        # insert statement
        db.session.add(todo)  # add to table
        db.session.commit()   # write to db
        body['description'] = todo.description
        body['id'] = todo.id
        body['completed'] = todo.completed
    except:
        error = True
        db.session.rollback()
        print(sys.exc_info())
    finally:
        db.session.close()
    if error:
        abort(400)
    else:
        return jsonify(body)


# route to update an item
@app.route('/todos/<todo_id>/set-completed', methods=['POST'])
def set_completed_todo(todo_id):
    try:
        completed = request.get_json()['completed']
        todo = Todo.query.get(todo_id)
        todo.completed = completed
        db.session.commit()
    except:
        db.session.rollback()
    finally:
        db.session.close()
    return redirect(url_for('index'))


# route to delete an item
@app.route('/todos/delete/<todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    try:
        todo = Todo.query.get(todo_id)
        db.session.delete(todo)  # or
        # Todo.query.filter_by(id=todo_id).delete()
        db.session.commit()
    except:
        db.session.rollback()
    finally:
        db.session.close()
    # return redirect(url_for('index'))
    return jsonify({ 'success': True })


if __name__ == '__main__':
    # set the debug mode to on
    app.debug = True
    app.run(host="0.0.0.0", port=5000)
