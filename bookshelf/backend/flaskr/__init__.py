import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy  
from flask_cors import CORS
import random

from models import setup_db, Book

BOOKS_PER_SHELF = 8

# @DONE: General Instructions
#   - As you're creating endpoints, define them and then search for 'TODO' within the frontend to update the endpoints there.
#     If you do not update the endpoints, the lab will not work - of no fault of your API code!
#   - Make sure for each route that you're thinking through when to abort and with which kind of error
#   - If you change any of the response body keys, make sure you update the frontend to correspond.

def paginate_books(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * BOOKS_PER_SHELF
    end = start + BOOKS_PER_SHELF

    books = [book.format() for book in selection]
    current_books = books[start:end]

    return current_books

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    # CORS Headers
    @app.after_request
    def after_request(response):
        response.headers.add(
            "Access-Control-Allow-Headers", "Content-Type,Authorization,true"
        )
        response.headers.add(
            "Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS"
        )
        return response

    
    @app.route('/books', methods=['GET'])
    def retrieve_books():
        selection = Book.query.order_by(Book.id).all()
        # paginations
        current_books = paginate_books(request, selection)

        if len(current_books) == 0:
            abort(404)

        return jsonify({
            'success': True,
            'books': current_books,
            'total_books': len(selection)
        })


    @app.route('/books/<int:book_id>', methods=['PATCH'])
    def update_book(book_id):

        body = request.get_json()

        try:
            book = Book.query.filter(Book.id == book_id).one_or_none()
            if book is None:
                abort(404)

            if 'rating' in body:
                book.rating = int(body.get('rating'))

            book.update()

            return jsonify({
                'success': True,
                'id': book.id
            })

        except:
            abort(400)


    @app.route('/books/<int:book_id>', methods=['DELETE'])
    def delete_book(book_id):
        try:
            book = Book.query.filter(Book.id == book_id).one_or_none()
        
            if book is None:
                abort(404)
            
            book.delete()
            selection = Book.query.order_by(Book.id).all()
            current_books = paginate_books(request, selection)

            return jsonify({
                'success': True,
                'deleted': book_id,
                'books': current_books,
                'total_books': len(selection)
            })

        except:
            abort(422)


    @app.route('/books', methods=['POST'])
    def create_book():
        # get the value from the request body
        body = request.get_json()
        
        new_title = body.get('title', None)
        new_author = body.get('author', None)
        new_rating = body.get('rating', None)
        search = body.get('search', None)

        try:
            if search:
                # not sure why this is here / nothing to do with creating a book but part of TDD lesson
                selection = Book.query.order_by(Book.id).filter(Book.title.ilike("%{}%".format(search))).all
                current_books = paginate_books(request, selection)

                return jsonify({
                    'success': True,
                    'books': current_books,
                    'total_books': len(selection)
                })
            else:
                # this is the code to add a book
                book = Book(title=new_title, author=new_author, rating=new_rating)
                book.insert()
                
                selection = Book.query.order_by(Book.id).all()
                current_books = paginate_books(request, selection)
                
                return jsonify({
                    'success': True,
                    'created': book.id,
                    'books': current_books,
                    'total_books': len(selection)
                })
        except:
            abort(422)

    # Start of Error Handlers

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "Resource not found"
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


    return app


"""
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
"""