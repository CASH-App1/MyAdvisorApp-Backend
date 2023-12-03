import unittest, pytest
from App.models import Program, ProgramCourses
from App.main import create_app
from App.database import db, create_db
from App.controllers import create_program, get_program_by_name,create_course, create_programCourse, get_all_programCourses, programCourses_SortedbyRating,programCourses_SortedbyHighestCredits

class ProgramUnitTests(unittest.TestCase):

    def test_new_program(self):
        programname = "Information Technology Special"
        core_credits = 69
        elective_credits = 15
        foun_credits = 9
        program = Program(programname, core_credits, elective_credits, foun_credits)
        self.assertEqual(program.name, programname)
        self.assertEqual(program.core_credits, core_credits)
        self.assertEqual(program.elective_credits, elective_credits)
        self.assertEqual(program.foun_credits, foun_credits)
    
    def test_program_toJSON(self):
        programname = "Information Technology Special"
        core_credits = 69
        elective_credits = 15
        foun_credits = 9
        
        program = Program(programname, core_credits, elective_credits, foun_credits)
        program_json = program.get_json()

        self.assertDictEqual(program_json, {
            'Program ID:': None,
            'Program Name: ': programname,
            'Core Credits: ': core_credits,
            'Elective Credits ': elective_credits,
            'Foundation Credits: ': foun_credits,
        })

    def test_new_program_course(self):
        programcourse=ProgramCourses("1","INFO2605","2")
        assert programcourse.code=="INFO2605"

    def test_program_course_toJSON(self):
        programcourse=ProgramCourses("1","INFO2605","2")
        programcourse_json=programcourse.get_json()
        self.assertDictEqual(programcourse_json,{'Program Course ID:':None, 'Program ID:':'1','Course Code: ':'INFO2605','Course Type: ':'2'})




@pytest.fixture(autouse=True, scope="module")
def empty_db():
    app = create_app({'TESTING': True, 'SQLALCHEMY_DATABASE_URI': 'sqlite:///test.db'})
    create_db()
    yield app.test_client()
    db.drop_all()

"Integration Tests"
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
