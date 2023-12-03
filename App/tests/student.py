import os
import tempfile
import pytest
import logging
import unittest
from werkzeug.security import check_password_hash, generate_password_hash

from App.main import create_app
from App.database import db, create_db
from App.models import User, Student, Program, StudentCourseHistory
from App.controllers import *

LOGGER = logging.getLogger(__name__)


class StudentUnitTest(unittest.TestCase):

    def test_new_student(self):
        student = Student("01234", "johnpass", "John Doe", 1)
        assert student.name == "John Doe"

    def test_student_toJSON(self):
        student = Student("01234", "johnpass", "John Doe", 1)
        student_json = student.get_json()
        self.assertDictEqual(
            {"name": "John Doe", "student_id": "01234", "program": 1}, student_json)


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
        student = add_student("816031318", "Sam", "Dawson", "sdawson@example.com", "sam_dawson", "password123", 
                "Computer Science Major", "Electronics Minor")
        retrieved_student = get_student(student.studentID)
        
        self.assertEqual((retrieved_student.firstName, retrieved_student.lastName, retrieved_student.email, 
                        retrieved_student.username, retrieved_student.program1, retrieved_student.program2),
                         ("Sam", "Dawson", "sdawson@example.com", "sam_dawson", "Computer Science Major", "Electronics Minor"))

    def test_update_student(self):
        student = add_student("816021458", "Jessica", "Pearson", "jessica.p@example.com", "jessica_pearson", "passjess", 
                            "Computer Science Maajor", "Mathematics Major")
        updated_student = update_student(student.studentID, "Janette", "Spectar", "janette@example.com", "janette_spectar", "new_password")
        retrieved_student = get_student(updated_student.studentID)

        self.assertEqual((retrieved_student.firstName, retrieved_student.lastName, retrieved_student.email, retrieved_student.username),
                         ("Janette", "Spectar", "janette@example.com", "janette_spectar"))

    def test_create_semester_history(self):
        student = add_student("123456789", "John", "Doe", "john.d@example.com", "john_doe", "password", "History Major", "Psychology")
        semester_history = create_semester_history(student.studentID, 2023, 1)
        self.assertIsNotNone(semester_history)
        
        student_history = get_student_history(student)
        self.assertTrue(any(hist['year'] == 2023 and hist['semester_type'] == 1 for hist in student_history))
