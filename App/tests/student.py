import os, tempfile, pytest, logging, unittest
from werkzeug.security import check_password_hash, generate_password_hash

from App.main import create_app
from App.database import db, create_db
from App.models import User, Student, Program, StudentCourseHistory, StudentProgram



LOGGER = logging.getLogger(__name__)

'''
Student Unit Tests
'''

class StudentUnitTests(unittest.TestCase):

    def test_new_student(self):
        newStudent = Student(816031123, "Jane", "Doe", "jan@email.com")
        assert (newStudent.studentID, newStudent.firstName, newStudent.lastName, newStudent.email) == (816031123, "Jane", "Doe", "jan@email.com")

    def test_student_toJSON(self):
        newStudent = Student(816031123, "Jane", "Doe", "jan@email.com")
        self.assertDictEqual(newStudent.get_json(), {"Student ID":816031123, "First Name":"Jane", "Last Name":"Doe", "Email":"jan@email.com"})

    def test_hashed_password(self):
        password = "mypass123"
        hashed = generate_password_hash(password, method='sha256')
        newStudent = Student(816031123, password, "Jane", "Doe", "jan@email.com")
        assert newStudent.password != password

    def test_check_password(self):
        password = "mypass123"
        newStudent = Student(816030212, password, "Jane", "Doe", "jan@email.com")
        assert newStudent.check_password(password) 

class StudentProgramUnitTests(self):

    def test_new_student_program(self):
        newStudentProgram = StudentProgram("816030870", "30")
        assert(newStudentProgram.studentID, newStudentProgram.programID) == ("816030870", "30")
    
