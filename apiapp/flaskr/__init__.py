# Import your dependencies
from flask import Flask, jsonify, request, abort
from models import setup_db, Plant
from flask_cors import CORS, cross_origin

# Define the create_app function

def create_app(test_config=None):
    # Create and configure the app
    # Include the first parameter: Here, __name__is the name of the current Python module.
    app = Flask(__name__, instance_relative_config=True)
    setup_db(app)
    CORS(app)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
        return response


    @app.route('/hello')
    def hello():
        return jsonify({'message': 'Hello World!'})

    # specifying variables via route
    @app.route('/entrees/<int:entree_id>')
    def retrieve_entree(entree_id):
        return f'Entree {entree_id}'

    # allowing GET and POST methods
    @app.route('/greetings', methods=['GET', 'POST'])
    def greeting():
        if request.method == 'POST':
            return "create_greeting()"
        else:
            return "send_greeting()"


    # Query Parameters to enable Paginations
    @app.route('/entrees', methods = ['GET'])
    def get_entrees():
        page = request.args.get('page', 1, type=int)
        return (':)')

    # Pagination using Query Parameters:
    # i.e., http://127.0.0.1:5000/plants?page=1
    # i.e., http://127.0.0.1:5000/plants?page=2
    @app.route('/plants', methods=['GET','POST'])
    def get_plants():
        #paginations
        page = request.args.get('page', 1, type=int)
        start = (page -1) * 10  # page=1 will be start=0 (idx 0-9); page=2, start=1 (idx 10-19)
        end = start + 10

        plants = Plant.query.all()
        formatted_plants = [plant.format() for plant in plants]

        return jsonify({
            'success': True,
            'plants': formatted_plants[start:end],
            'total_plants': len(formatted_plants)
            })


    @app.route('/plants/<int:plant_id>')
    def get_specific_plant(plant_id):
        plant = Plant.query.filter(Plant.id == plant_id).one_or_none()

        if plant is None:
            abort(404)
        else:
            return jsonify({
                'success': True,
                'plant': plant.format()
            })


    # Return the app instance
    return app



"""
# For Mac/Linux
export FLASK_APP=flaskr
export FLASK_ENV=development

# Make sure to run this command from the project directory (not from the flaskr)
flask run

"""