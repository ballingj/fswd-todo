from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# need to define the URI to connect to our database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/example'

# This will link an instance of database that we can
# interact with SQLAlchemy to our Flask app
db = SQLAlchemy(app)


@app.route('/')
def index():
    return 'Hello Everyone!'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
