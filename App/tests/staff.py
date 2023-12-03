import unittest, pytest
from App.main import create_app
from App.database import db, create_db
from App.models import Staff
from App.controllers import *
from werkzeug.security import generate_password_hash

'''
Staff Unit Tests 
'''

class StaffUnitTests(unittest.TestCase):

    def test_new_staff(self):
        #newUser = User()
        newStaff = Staff(101, "DCIT", "Bobby", "Smith", "bob@mail.com", "bob", "bobpass")
        assert (newStaff.staffID, newStaff.departmentCode, newStaff.firstName,  newStaff.lastName, newStaff.email, newStaff.username) == (101, "DCIT", "Bobby", "Smith", "bob@mail.com", "bob")

    # pure function no side effects or integrations called
    def test_staff_toJSON(self):
        newStaff = Staff(101, "DCIT", "Bobby", "Smith", "bob@mail.com", "bob", "bobpass")
        self.assertDictEqual(newStaff.get_json(), {"Staff ID":101, "First Name":"Bobby", "Last Name":"Smith", "Email":"bob@mail.com", "Department Code":"DCIT", "Username":"bob"})
    

    def test_hashed_password(self):
        password = "pass123"
        hashed = generate_password_hash(password, method='sha256')
        newStaff = Staff(101, "DCIT", "Bobby", "Smith", "bob@mail.com", "bob", "bobpass")
        assert newStaff.password != password

    def test_check_password(self):
        password = "pass123"
        newStaff = Staff(101, "DCIT", "Bobby", "Smith", "bob@mail.com", "bob", password)
        assert newStaff.check_password(password) 
