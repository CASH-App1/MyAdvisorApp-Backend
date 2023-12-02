import os, tempfile, pytest, logging, unittest
from App.models import Program, ProgramCourses
from App.main import create_app
from App.database import db, create_db


class ProgramUnitTests(unittest.TestCase):

    def test_new_program(self):
        newProgram = Program("DCIT", "Computer Science Special", "24", "3", "12")
        assert(newProgram.departmentCode, newProgram.programName, newProgram.coreCredits, newProgram.electiveCredits, newProgram.founCredits) == ("DCIT", "Computer Science Special", "24", "3", "12")
    
    def test_program_course_toDict (self):
        newProgram = Program("DCIT", "Computer Science Special", "24", "3", "12")
        self.assertDictEqual(newProgram.toDict(), {"Program ID":"CS100", "Department Code":"DCIT", "Program Name":"Computer Science Special", "Core Credits":"24", "Elective Credits":"3", "Foundation Credits":"12"})

class ProgramCourseUnitTests(unittest.TestCase):

    def test_new_program_course(self):
        newProgramCourse = ProgramCourses("COMP307", "CS100")
        assert(newProgramCourse.courseCode, newProgramCourse.programID) == ("COMP307", "CS100")

    def test_program_course_toDict(self):
        newProgramCourse = ProgramCourses("COMP307", "CS100")
        self.assertDictEqual(newProgramCourse.toDict(), {"Program Course ID":"1", "Course Code":"COMP307", "Program ID":"CS100"})
