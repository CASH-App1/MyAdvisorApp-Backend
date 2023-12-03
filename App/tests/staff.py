import os, tempfile, pytest, logging, unittest
from App.main import create_app
from App.database import db, create_db
from App.models import Staff

from werkzeug.security import generate_password_has

'''
Staff Unit Tests 
'''

class StaffUnitTests(unittest.TestCase):

    def test_new_staff(self):
        #newUser = User()
        newStaff = Staff("bob@mail.com", "DCIT", "Bobby", "Smith")
        assert (newStaff.email, newStaff.departmentCode, newStaff.firstName,  newStaff.lastName) == ("bob@mail.com", "DCIT", "Bobby", "Smith")

    # pure function no side effects or integrations called
    def test_staff_toJSON(self):
        newStaff = Staff("bob", "bobpass", "bob@mail.com", "DCIT", "Bobby", "Smith")
        #staff_json = newStaff.toDict()
        self.assertDictEqual(newStaff.get_json(), {"Staff ID":101, "First Name":"Bobby", "Last Name":"Smith", "Email":"bob@mail.com", "Department Code":"DCIT", "Username":"bob"})
    

    def test_hashed_password(self):
        password = "pass123"
        hashed = generate_password_hash(password, method='sha256')
        newStaff = Staff("bob", "bobpass", "bob@mail.com", "Bobby", "Smith")
        assert newStaff.password != password

    def test_check_password(self):
        password = "pass123"
        newStaff = Staff("bob", password, "bob@mail.com", "Bobby", "Smith")
        assert newStaff.check_password(password) 

"Integration Tests"

@pytest.fixture(autouse=True, scope="module")
def empty_db():
    app = create_app({'TESTING': True, 'SQLALCHEMY_DATABASE_URI': 'sqlite:///test.db'})
    create_db()
    yield app.test_client()
    db.drop_all()

class StaffIntegrationTests(unittest.TestCase):

    def test_create_staff(self):
        staff = create_staff(101, "CLL", "Jane", "Austin", "jane101@mail.com", "jane", "janepass")
        retrieved_staff = get_staff_by_id(staff.staffID)
        
        self.assertEqual((retrieved_staff.departmentCode, retrieved_staff.firstName, retrieved_staff.lastName, 
                        retrieved_staff.email, retrieved_staff.username),
                         ("CLL", "Jane", "Austin", "jane101@mail.com", "jane"))

    def test_update_staff(self):
        staff = create_staff(101, "CLL", "Jane", "Austin", "jane101@mail.com", "jane", "janepass")
        updated_staff = update_staff(staff.staffID, "DCIT", "Janice", "Dottin", "janice@example.com", "jan_dot", "newjanepass")
        retrieved_staff = get_staff_by_id(updated_staff.staffID)

        self.assertEqual((retrieved_staff.departmentCode, retrieved_staff.firstName, retrieved_staff.lastName, 
                        retrieved_staff.email, retrieved_staff.username),
                        ("DCIT", "Janice", "Dottin", "janice@example.com", "jan_dot"))

