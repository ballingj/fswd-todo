## Flask Cheatsheet

### install venv
```sh
sudo apt install python3.10-venv
```
### Creat virtual environment in a folder ./venv
```sh
python -m venv ./venv
```
### activate  -- you should see (venv) in prompt
```sh
source ./venv/bin/activate
```
### deactivate  -- you should see (venv) go away
```sh
deactivate
```
### install the pip package you need
```sh
pip install flask
pip install flask-sqlalchemy
```
### Starting Flask app from the terminal (option 1)
- Make sure you are in the directory that contains app.py
- We run a flask app defined at app.py by running this line of code on one line
```
FLASK_APP=app.py FLASK_DEBUG=true flask run
```
- ```FLASK_APP``` # must be set to the server file path with an equal sign in between. No spaces. FLASK_APP = app.py will not work.
- ```FLASK_DEBUG=true``` # will enable debug mode which allows live reload
- ```flask run```  # actually executes the flask server code in the app.py file

### Starting Flask in python code (option 2)
- Make sure you are in the directory that contains app.py
- Do not enter any of the flask code mentioned in option 1
- Simply include the following in your python file
```
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Everyone!'

#always include this at the bottom of your code
if __name__ == '__main__':
   app.run(host="0.0.0.0")
```
- then in the terminal, run the app as usual
```
python app.py
```

### Migrations
- import flask_migrate
```
import flask_migrate import migrate

```

- Add flask migrate; right below db = SQLAlchemy()
```
db = SQLAlchemy(app)
migrate = Migrate(app, db)
```

- initialize migrations at the terminal
```
flask db init

flask db migrate
```

- now run the migrations

- 'upgrade' to execute the migrations script
```
flask db upgrade
```

or 'downgrade' to rollback the migrations script
```
flask db downgrade
```
