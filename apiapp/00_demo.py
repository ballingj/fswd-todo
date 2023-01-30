from flask import Flask, jsonify
from flask_cors import CORS, cross_origin


# def create_app(test_config=None):
app = Flask(__name__, instance_relative_config=True)
# CORS(app)
# '*' means any origins
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

# CORS Headers
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
    return response

@app.route('/messages')
@cross_origin()
# if we want to allow cors in this path add this decorator
def get_messages():
    return jsonify({'message': 'GETTING MESSAGES'})

# return app


if __name__ == '__main__':
    # set the debug mode to on
    app.debug = True
    app.run(host="0.0.0.0", port=5000)
