import pytest, unittest
from App.models import Course, Prerequisite, CourseHistory
from App.controllers import *
from App.main import create_app
from App.database import db, create_db

class CourseUnitTests(unittest.TestCase):

    def test_new_course(self):
        newCourse = Course("CSCI101", "PR001", "DataStructures", 3, 8)
        assert (newCourse.courseCode, newCourse.prereqID, newCourse.courseName, newCourse.credits, newCourse.difficulty) == ("CSCI101", "PR001", "DataStructures", 3, 8)

    def test_course_toJSON(self):
        newCourse = Course("CSCI101", "PR001", "DataStructures", 3, 8)
        self.assertDictEqual(newCourse.get_json(), {"CourseCode":"CSCI101", "Prerequisite ID": "PR001", "Course Name":"Data Structures", "Credits":3, "Difficulty":8})


class PrerequisiteUnitTests(unittest.TestCase):

    def test_new_prerequisite(self):
        newPrerequisite = Prerequisite("MATH202")
        assert (newPrerequisite.courseCode) == ("MATH202")
    
    def test_prerequisite_toJSON(self):
        newPrerequisite = Prerequisite("MATH202")
        self.assertDictEqual(newPrerequisite.get_json(), {"Prerequisite ID":"PR001", "Course Code": "MATH202"})
    
class CourseHistoryUnitTests(unittest.TestCase):

    def test_new_course_history (self):
        newCourseHistory = CourseHistory("CSCI101", "A", "0.85", "elective")
        assert (newCourseHistory.courseCode, newCourseHistory.gradeLetter, newCourseHistory.percent, newCourseHistory.courseType) == ("CSCI101", "A", "0.85", "elective")
    
    def test_course_history_toJSON (self):
        newCourseHistory = CourseHistory("CSCI101", "A", "0.85", "elective")
        self.assertDictEqual(newCourseHistory.get_json(), {"Course History ID": "CH001", "Course Code":"CSCI101", "Grade":"A", "Percentage":"0.85", "Course Type":"elective"})


"Integration Tests"
class TestCourseIntegration(unittest.TestCase):
    def test_create_course(self):
        # Test data for the course
        course_code = "COMP 1602"
        course_name = "Computer Programming II"
        credits = 3
        difficulty = 3

        
        created_course = create_course(course_code, course_name, credits, difficulty)
        self.assertIsNotNone(created_course)

        retrieved_course = get_course_by_courseCode(course_code)
        self.assertEqual((retrieved_course.code, retrieved_course.courseName, retrieved_course.credits, retrieved_course.difficulty),
                         (course_code, course_name, credits, difficulty))
