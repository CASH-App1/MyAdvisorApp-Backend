import os, tempfile, pytest, logging, unittest
from werkzeug.security import check_password_hash, generate_password_hash

from App.main import create_app
from App.database import db, create_db
from App.models import User


LOGGER = logging.getLogger(__name__)

'''
   User Unit Tests
'''


class UserUnitTests(unittest.TestCase):

    def test_new_user(self):
        newUser = User("bob", "bobpass")
        assert newUser.username == "bob"

    # pure function no side effects or integrations called
    def test_user_json(self):
        user = User("bob", "bobpass")
        user_json = user.get_json()
        self.assertDictEqual(user_json, {"id": "101", "username": "bob"})

    def test_hashed_password(self):
        password = "mypass"
        hashed = generate_password_hash(password, method='sha256')
        newUser = User("bob", password)
        assert newUser.password != password

    def test_check_password(self):
        password = "mypass"
        user = User("bob", password)
        assert user.check_password(password)

