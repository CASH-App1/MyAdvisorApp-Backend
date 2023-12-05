import os, tempfile, pytest, logging, unittest

from App.models import Semester, SemesterCourse, SemesterHistory
from App.main import create_app
from App.database import db, create_db
from App.controllers import *

class SemesterUnitTests(unittest.TestCase):

    def test_new_semester(self):
        newSemester = Semester(2023, 1)
        assert(newSemester.year, newSemester.semesterType) == (2023, 1)

    def test_semester_toJSON(self):
        newSemester = Semester(2023, 1)
        assert(newSemester.get_json(), {"Semester ID":None, "Courses":[],"Semester Year":2023, "Semester Type":1})

class SemesterCourseUnitTests(unittest.TestCase):

    def test_new_semester_course(self):
        newSemesterCourse = SemesterCourse("PHYS101", "SEMI2K23")
        assert(newSemesterCourse.courseCode, newSemesterCourse.semesterID) == ("PHYS101", "SEMI2K23")
    
    def test_semester_course_toJSON(self):
        newSemesterCourse = SemesterCourse("PHYS101", "SEMI2K23")
        assert(newSemesterCourse.get_json(), {"Semester Course ID":None, "Course Code":"PHYS101", "Semester ID": "SEMI2K23"})

class SemesterHistoryUnitTests(unittest.TestCase):

    def test_new_semester_history(self):
        newSemesterHistory = SemesterHistory("816031123", 2023, "1")
        assert(newSemesterHistory.studentID, newSemesterHistory.year, newSemesterHistory.semesterType) == ("816031123", 2023, "1")

    def test_semester_history_toJSON(self):
        newSemesterHistory = SemesterHistory("816031123", 2023, "1")
        assert(newSemesterHistory.get_json(), {"History ID":"SEMH001","Student ID":"816031123", "Semester Year":2023, "Semester Type":"1"})

"Integration Tests"
class SemesterIntegrationTests(unittest.TestCase):

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

    def test_create_semester(self): 
        year = 2023
        semester_type = 1
        created_semester = create_semester(year, semester_type)
        self.assertIsNotNone(created_semester)

        retrieved_semester = get_semester_by_id(created_semester.semesterID)
        self.assertEqual((retrieved_semester.year, retrieved_semester.semesterType),
                         (year, semester_type))

    def test_add_semester_course(self):
        course_code = "COMP 2611"
        course_name = "Data Structures"
        credits = 3
        difficulty = 5
        semester_year = 2023
        semester_type = 2

        created_course = create_course(course_code, course_name, credits, difficulty)
        created_semester = create_semester(semester_year, semester_type)
        self.assertIsNotNone(created_course)
        self.assertIsNotNone(created_semester)

        add_result = add_semester_course(course_code, created_semester.semesterID)
        retrieved_semester_course = get_semester_course_by_id(course_code, created_semester.semesterID)
        self.assertTrue(add_result)
        self.assertIsNotNone(retrieved_semester_course)
        self.assertEqual(retrieved_semester_course.course.code, course_code)

    def test_remove_semester_course(self):
        course_code = "COMP 2601"
        course_name = "Computer Architecture"
        credits = 3
        difficulty = 8
        semester_year = 2023
        semester_type = 1

        created_course = create_course(course_code, course_name, credits, difficulty)
        created_semester = create_semester(semester_year, semester_type)
        self.assertIsNotNone(created_course)
        self.assertIsNotNone(created_semester)

        add_semester_course(course_code, created_semester.semesterID)
        remove_result = remove_semester_course(course_code, created_semester.semesterID)
        all_semester_courses = get_all_semester_courses()
        self.assertTrue(remove_result)
        self.assertNotIn(course_code, [course.course.code for course in all_semester_courses])

    def test_create_semester_history(self):
        studentID = "123456789"
        first_name = "Selena"
        last_name = "Taylor"
        email = "taylor.d@example.com"
        username = "selena_tay"
        password = "taytay123"
        year = 2023
        semester_type = 2

        created_student = add_student(studentID, first_name, last_name, email, username, password, "Biology Major", "Geography Minor")
        created_semester_history = create_semester_history(created_student.studentID, year, semester_type)
        self.assertIsNotNone(created_student)
        self.assertIsNotNone(created_semester_history)

        retrieved_student_history = get_student_history(created_student)
        self.assertTrue(any(hist['year'] == year and hist['semester_type'] == semester_type for hist in retrieved_student_history))

    def test_update_student_history(self):
        studentID = "987654321"
        first_name = "Jane"
        last_name = "Doe"
        email = "jane.d@example.com"
        username = "jane_doe"
        password = "password"
        year = 2023
        semester_type = 1

        created_student = add_student(studentID, first_name, last_name, email, username, password, "Information Technology Major", "Mathematics Minor")
        created_semester_history = create_semester_history(created_student.studentID, year, semester_type)

        histories = [
            {'courseCode': 'COMP2605', 'gradeLetter': 'A', 'percent': 0.90, 'CourseType': 'Core'},
            {'courseCode': 'MATH1115', 'gradeLetter': 'B', 'percent': 0.85, 'CourseType': 'Elective'}
        ]

        update_result = updateStudentHistory(created_student, 2023, 1, histories)
        retrieved_student_history = get_student_history(created_student)
        self.assertTrue(update_result)
        self.assertTrue(any(hist['year'] == 2023 and hist['semester_type'] == 1 for hist in retrieved_student_history))
    
    def test_add_course_to_history(self):
        student = add_student("816037684", "Jack", "Hart", "jhart@example.com", "jackofhearts", "hart4life", "Mathematics Major", "Statistics Minor")
        semester_history = create_semester_history(student.studentID, 2023, 2)

        course_code = 'COMP2605'
        grade_letter = 'A'
        percent = 0.90
        course_type = 'Core'

        addCoursetoHistory(student.studentID, semester_history, course_code, grade_letter, percent, course_type, semester_history.historyID)
        retrieved_student_history = get_student_history(student)
        self.assertTrue(any(hist['courses'][0]['courseCode'] == course_code for hist in retrieved_student_history))
