from main import db, app
from app.models import TodoList
import json
import unittest

TEST_DB = "app_test.db"


class RecipesApiTests(unittest.TestCase):

    # executed before each test run
    def setUp(self):
        app.config["TESTING"] = True
        app.config["WTF_CSRF_ENABLED"] = False
        app.config["DEBUG"] = False
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app_test.db"
        self.app = app.test_client()
        db.drop_all()  # drop tables in previous tests
        db.create_all()  # table in databse
        self.create_todo()
        self.assertEqual(app.debug, False)

    def create_todo(self):
        # create to-do items that will be used for testing
        item1 = TodoList(todo="Go to school")
        item2 = TodoList(todo="Make Mediterranean Chicken")

        db.session.add(item1)
        db.session.add(item2)

        db.session.commit()
