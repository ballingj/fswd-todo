# Import your dependencies
from flask import Flask, jsonify, request, abort
from models import setup_db, Plant
from flask_cors import CORS, cross_origin

PLANTS_PER_PAGE = 8

def paginate_plants(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * PLANTS_PER_PAGE
    end = start + PLANTS_PER_PAGE

    plants = [plant.format() for plant in selection]
    current_plants = plants[start:end]

    return current_plants


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
    
    @app.route('/plants', methods=['GET'])
    def get_plants():
        selection = Plant.query.order_by(Plant.id).all()
        # paginations
        current_plants = paginate_plants(request, selection)
        if len(current_plants) == 0:
            abort(404)

        return jsonify({
            'success': True,
            'plants': current_plants,
            'total_plants': len(selection)
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

    @app.route('/plants/<int:plant_id>', methods=['PATCH'])
    def update_plant(plant_id):

        body = request.get_json()

        try:
            plant = Plant.query.filter(Plant.id == plant_id).one_or_none()
            if plant is None:
                abort(404)

            if 'is_poisonous' in body:
                plant.is_poisonous = bool(body.get('is_poisonous'))

            plant.update()

            return jsonify({
                'success': True,
                'id': plant.id
            })

        except:
            abort(404)


    @app.route('/plants/<int:plant_id>', methods=['DELETE'])
    def delete_book(plant_id):
        try:
            plant = Plant.query.filter(Plant.id == plant_id).one_or_none()

            if plant is None:
                abort(404)

            plant.delete()
            selection = Plant.query.order_by(Plant.id).all()
            current_plants = paginate_plants(request, selection)

            return jsonify({
                'success': True,
                'deleted': plant_id,
                'books': current_plants,
                'total_plants': len(selection)
            })

        except:
            abort(422)


    @app.route('/plants', methods=['POST'])
    def create_plant():
        # get the value from the request body
        body = request.get_json()

        new_name = body.get('name', None)
        new_scientific_name = body.get('scientific_name', None)
        new_is_poisonous = bool(body.get('is_poisonous', False))
        new_primary_color = body.get('primary_color', None)

        try:
            plant = Plant(
                    name = new_name,
                    scientific_name = new_scientific_name,
                    is_poisonous = new_is_poisonous,
                    primary_color = new_primary_color
                    )
            
            plant.insert()

            selection = Plant.query.order_by(Plant.id).all()
            current_plants = paginate_plants(request, selection)

            return jsonify({
                'success': True,
                'created': plant.id,
                'books': current_plants,
                'total_books': len(selection)
            })
        except:
            abort(422)

    # Error Handling 

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "Not found"
        }), 404


    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422


    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "Bad Request"
        }), 400


    @app.errorhandler(405)
    def not_allowed(error):
        return jsonify({
            "success": False,
            "error": 405,
            "message": "Method Not Allowed"
        }), 405


    # Return the app instance
    return app



"""
# For Mac/Linux
export FLASK_APP=flaskr
export FLASK_ENV=development

# Make sure to run this command from the project directory (not from the flaskr)
flask run

"""