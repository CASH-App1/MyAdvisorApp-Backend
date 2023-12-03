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

    def test_program_course_toJSON(self):
        newProgramCourse = ProgramCourses("COMP307", "CS100")
        self.assertDictEqual(newProgramCourse.get_json(), {"Program Course ID":"1", "Course Code":"COMP307", "Program ID":"CS100"})





@pytest.fixture(autouse=True, scope="module")
def empty_db():
    app = create_app({'TESTING': True, 'SQLALCHEMY_DATABASE_URI': 'sqlite:///test.db'})
    create_db()
    yield app.test_client()
    db.drop_all()

class ProgramIntegrationTests(unittest.TestCase):

    def test_create_program(self):
        program = create_program("DCIT", "Computer Science Special", 69, 15, 9)
        retrieved_program = get_program_by_id(program.id)

        self.assertEqual((retrieved_program.department_code, retrieved_program.program_name, 
                        retrieved_program.core_credits, retrieved_program.elective_credits, 
                        retrieved_program.foun_credits),
                         ("DCIT", "Computer Science Special", 69, 15, 9))

    def test_add_program_prerequisites(self):
        # Test data for the program and course
        department_code = "DCIT"
        program_name = "Computer Science with Management "
        core_credits = 30
        elective_credits = 15
        foun_credits = 12

        course_code = "COMP 2605"
        course_name = "Enterprise Database Systems"
        credits = 3
        difficulty = 6

        created_program = create_program(department_code, program_name, core_credits, elective_credits, foun_credits)
        created_course = create_course(course_code, course_name, credits, difficulty)
        self.assertIsNotNone(created_program)
        self.assertIsNotNone(created_course)

        add_program_prerequisites(program_name, course_code, "core")
        prerequisite_exists = check_prerequisite_exists(program_name, course_code)
        self.assertIsNotNone(prerequisite_exists)
       
        all_program_courses = get_all_program_courses(program_name)
        self.assertTrue(any(course.course_code == course_code for course in all_program_courses))

