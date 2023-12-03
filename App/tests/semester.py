import os, tempfile, pytest, logging, unittest

from App.models import Semester, SemesterCourse
from App.main import create_app
from App.database import db, create_db

class SemesterUnitTests(unittest.TestCase):

    def test_new_semester(self):
        newSemester = Semester("2023", "1")
        assert(newSemester.year, newSemester.semesterType) == ("2023", "1")

    def test_semester_toDict(self):
        newSemester = Semester("2023", "1")
        assert(newSemester.toDict(), {"Semester Year":"2023", "Semester Type":"1"})

class SemesterCourseUnitTests(unittest.TestCase):

    def test_new_semester_course(self):
        newSemesterCourse = SemesterCourse("PHYS101", "SEMI2K23")
        assert(newSemesterCourse.courseCode, newSemesterCourse.semesterID) == ("PHYS101", "SEMI2K23")
    
    def test_semester_course_toDict(self):
        newSemesterCourse = SemesterCourse("PHYS101", "SEMI2K23")
        assert(newSemesterCourse.toDict(), {"Semester Course ID":1, "Course Code":"PHYS101", "Semester ID": "SEMI2K23"})

class SemesterHistoryUnitTests(unittest.TestCase):

    def test_new_semester_history(self):
        newSemesterHistory = SemesterHistory("816031123", "2023", "1")
        assert(newSemesterHistory.studentID, newSemesterHistory.year, newSemesterHistory.semesterType) == ("816031123", "2023", "1")

    def test_semester_history_toJSON(self):
        newSemesterHistory = SemesterHistory("816031123", "2023", "1")
        assert(newSemesterHistory.toDict(), {"History ID":"SEMH001","Student ID":"816031123", "Semester Year":"2023", "Semester Type":"1"})

