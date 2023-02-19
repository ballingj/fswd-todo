# Solution Code
import unittest
import json

from flask_sqlalchemy import SQLAlchemy
from flaskr import create_app
from models import setup_db, Book


class BookTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "bookshelf_test"
        self.database_path = "postgresql://{}:{}@{}/{}".format(
            "student", "student", "localhost:5432", self.database_name
            )
        setup_db(self.app, self.database_path)

        self.new_book = {
            "title": "Anansi Boys",
            "author": "Neil Gaiman",
            "rating": 5
        }

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    # Start of test on different behavior 

    def test_get_paginated_books(self):
        res = self.client().get("/books")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["total_books"])
        self.assertTrue(len(data["books"]))

    def test_404_sent_requesting_beyond_valid_page(self):
        res = self.client().get("/books?page=1000", json={"rating": 1})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Resource not found")


    # @TODO: Write tests for search - at minimum two
    # that check a response when there are results and when there are none

    # TDD Lesson
    def test_get_book_search_with_results(self):
        res = self.client().get("/books", json={'search': 'Novel'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["total_books"])
        self.assertEqual(len(data["books"]), 4)


    def test_get_book_search_without_results(self):
        res = self.client().get("/books", json={'search': 'applejacks'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(data["total_books"], 0)
        self.assertEqual(len(data["books"]), 0)


    # Test Update ratings
    def test_update_book_rating(self):
        '''Test Book rating updates'''
        res = self.client().patch("/books/5", json={'rating': 1})
        data = json.loads(res.data)
        
        with self.app.app_context():
            book = Book.query.filter(Book.id == 5).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(book.format()['rating'], 1)


    def test_400_for_failed_update(self):
        '''Test Book rating update failed'''
        res = self.client().patch("/books/5")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Bad Request")

    # Test Book deletion - delete a different book in each attempt
    def test_delete_book(self):
        '''Test deletion of books'''
        res = self.client().delete("/books/34")
        data = json.loads(res.data)

        with self.app.app_context():
            book = Book.query.filter(Book.id == 34).one_or_none()
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(data["deleted"], 34)
        self.assertTrue(data["total_books"])
        self.assertTrue(len(data["books"]))
        self.assertEqual(book, None)


    def test_422_if_book_does_not_exist(self):
        '''Test deletion of books failure due to not exist'''
        res = self.client().delete("/books/1000")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "unprocessable")


    # Test create new book
    def test_create_new_book(self):
        '''Test create new book'''
        res = self.client().post("/books", json=self.new_book)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["created"])
        self.assertTrue(len(data["books"]))

    def test_405_if_book_creation_not_allowed(self):
        '''Test Not allowed'''
        res = self.client().post("/books/45", json=self.new_book)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Method Not Allowed")


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
