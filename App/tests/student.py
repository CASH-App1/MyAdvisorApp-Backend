import os, tempfile, pytest, logging, unittest
from werkzeug.security import check_password_hash, generate_password_hash

from App.main import create_app
from App.database import db, create_db
from App.models import User, Student, Program, StudentProgram
from App.controllers import add_student, update_student, get_student

from App.models import User, Student, Program, StudentCourseHistory, StudentProgram


LOGGER = logging.getLogger(__name__)

'''
Student Unit Tests
'''

class StudentUnitTests(unittest.TestCase):

    def test_new_student(self):
        newStudent = Student(816031123, "Jane", "Doe", "jan@email.com", "jan", "janepass")
        assert (newStudent.studentID, newStudent.firstName, newStudent.lastName, newStudent.email, newStudent.username) == (816031123, "Jane", "Doe", "jan@email.com", "jan")

    def test_student_toJSON(self):
        newStudent = Student(816031123, "Jane", "Doe", "jan@email.com", "jan", "janepass")
        self.assertDictEqual(newStudent.get_json(), {"Student ID":816031123, "First Name":"Jane", "Last Name":"Doe", "Email":"jan@email.com", "Username":"jan"})

    def test_hashed_password(self):
        password = "mypass123"
        hashed = generate_password_hash(password, method='sha256')
        newStudent = Student(816031123, "Jane", "Doe", "jan@email.com", "jan", "janepass")
        assert newStudent.password != password

    def test_check_password(self):
        password = "mypass123"
        newStudent = Student(816031123, "Jane", "Doe", "jan@email.com", "jan", password)
        assert newStudent.check_password(password) 

class StudentProgramUnitTests(unittest.TestCase):

    def test_new_student_program(self):
        newStudentProgram = StudentProgram("816030870", "30")
        assert(newStudentProgram.studentID, newStudentProgram.programID) == ("816030870", "30")

"Integration Tests"
class StudentIntegrationTests(unittest.TestCase):

    def setUp(self):
        app = create_app(
            {'TESTING': True, 'SQLALCHEMY_DATABASE_URI': 'sqlite:///test.db'})
        self.app = app.test_client()

        with app.app_context():
            create_db()
            db.create_all()

    def tearDown(self):
        with self.app:
            db.session.remove()
            db.drop_all()
            db.engine.dispose()

    def test_create_student(self):
        student = add_student(816, "Sam", "Dawson", "sdawson@example.com", "sam_dawson", "password123", 
                "Computer Science Major", "Electronics Minor")
        retrieved_student = get_student(student.studentID)
        
        student = add_student(814, "Jessica", "Pearson", "jessica.p@example.com", "jessica_pearson", "passjess", "Computer Science Major", "Mathematics Major")
        updated_student = update_student(student.studentID, "Janette", "Spectar", "janette@example.com", "janette_spectar", "new_password")
        retrieved_student = get_student(update_student.studentID)

        assert(retrieved_student.firstName, retrieved_student.lastName, retrieved_student.email, retrieved_student.username) == ("Janette", "Spectar", "janette@example.com", "janette_spectar")

   
   