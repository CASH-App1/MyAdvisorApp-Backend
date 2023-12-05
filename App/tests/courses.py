import pytest, unittest
from App.models import Course, CourseHistory
from App.controllers import *
from App.main import create_app
from App.database import db, create_db

class CourseUnitTests(unittest.TestCase):

    def test_new_course(self):
        newCourse = Course("CSCI101", "DataStructures", 3, 8)
        assert (newCourse.courseCode, newCourse.courseName, newCourse.credits, newCourse.difficulty) == ("CSCI101", "DataStructures", 3, 8)

    def test_course_toJSON(self):
        newCourse = Course("CSCI101", "DataStructures", 3, 8)
        self.assertDictEqual(newCourse.get_json(), {"Course Code":"CSCI101", "Course Name":"DataStructures", "Credits":3, "Difficulty":8})

'''
class PrerequisiteUnitTests(unittest.TestCase):

    def test_new_prerequisite(self):
        newPrerequisite = Prerequisite("MATH202")
        assert (newPrerequisite.courseCode) == ("MATH202")
    
    def test_prerequisite_toJSON(self):
        newPrerequisite = Prerequisite("MATH202")
        self.assertDictEqual(newPrerequisite.get_json(), {"Prerequisite ID":"PR001", "Course Code": "MATH202"})
''' 
class CourseHistoryUnitTests(unittest.TestCase):

    def test_new_course_history (self):
        newCourseHistory = CourseHistory("CH001", "CSCI101", "A", "0.85", "elective", "SEMI2K23")
        assert (newCourseHistory.courseHistoryID, newCourseHistory.courseCode, newCourseHistory.gradeLetter, newCourseHistory.percent, newCourseHistory.courseType, newCourseHistory.semesterID) == ("CH001", "CSCI101", "A", "0.85", "elective", "SEMI2K23")
    
    def test_course_history_toJSON (self):
        newCourseHistory = CourseHistory("CH001", "CSCI101", "A", "0.85", "elective", "SEMI2K23")
        self.assertDictEqual(newCourseHistory.get_json(), {"Course History ID": "CH001", "Course Code":"CSCI101", "Course Grade":"A", "Percentage":"0.85", "Course Type":"elective", "Semester ID":"SEMI2K23"})


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
