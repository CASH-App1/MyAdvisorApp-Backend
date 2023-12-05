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
        newUser = User("bob", "bobpass", "Bob", "Smith", "bob@mail.com")
        assert (newUser.username, newUser.firstName, newUser.lastName, newUser.email) == ("bob","Bob", "Smith", "bob@mail.com")

    # pure function no side effects or integrations called
    def test_user_toJSON(self):
        newUser = User("bob", "bobpass", "Bob", "Smith", "bob@mail.com")
        user_json = newUser.get_json()
        self.assertDictEqual(user_json, {"id": None, "username": "bob"})

    def test_hashed_password(self):
        password = "mypass"
        hashed = generate_password_hash(password, method='sha256')
        newUser = User("bob", "bobpass", "Bob", "Smith", "bob@mail.com")
        assert newUser.password != password

    def test_check_password(self):
        password = "mypass"
        newUser = User("bob", password, "Bob", "Smith", "bob@mail.com")
        assert newUser.check_password(password)

'''
    Integration Tests
'''

# This fixture creates an empty database for the test and deletes it after the test
# scope="class" would execute the fixture once and resued for all methods in the class


@pytest.fixture(autouse=True, scope="module")
def empty_db():
    app = create_app(
        {'TESTING': True, 'SQLALCHEMY_DATABASE_URI': 'sqlite:///test.db'})
    create_db()
    yield app.test_client()
    db.drop_all()
    
class UsersIntegrationTests(unittest.TestCase):

    def test_create_user(self):
        user = create_user("john_doe", "password123")
        retrieved_user = get_user_by_username(user.username)

        self.assertEqual((retrieved_user.username, retrieved_user.password),
                         ("john_doe", "password123"))

    def test_login(self):
        create_user("john_doe", "password123")
        logged_in_user = login("john_doe", "password123")

        self.assertIsNotNone(logged_in_user)

    def test_authenticate(self):
        create_user("john_doe", "password123")
        authenticated = authenticate("john_doe", "password123")

        self.assertTrue(authenticated)

    def test_get_all_user_json(self):
        create_user("john_doe", "password123")
        users_json_data = get_all_users_json()

        self.assertIn({"username": "john_doe"}, users_json_data)

    def test_update_user(self):
        user = create_user("john_doe", "password123")
        update_user(user.id, "new_john_doe")
        updated_user = get_user(user.id)

        self.assertEqual(updated_user.username, "new_john_doe")
