import pytest, unittest
from App.models import CoursePlan, CoursePlanCourses, EasiestCourses, FastestGraduation, ElectivePriority, CoursePlanDirector
from App.controllers import create_CoursePlan, create_student, create_program, addCourseToPlan, enroll_in_programme, addSemesterCourses, generator, createCoursesfromFile, get_program_by_name, getCoursePlan, get_all_courses_by_planid, get_student, create_programCourse, removeCourse
from App.main import create_app

from App.database import db, create_db

class CoursePlanUnitTests(unittest.TestCase):
    
    def test_new_course_plan (self):
        newCoursePlan = CoursePlan("816031123", "SEMI2K23")
        assert(newCoursePlan.studentID, newCoursePlan.semesterID) == ("816031123", "SEMI2K23") 
    
    def test_course_plan_toJSON (self):
        newCoursePlan = CoursePlan("816031123", "SEMI2K23")
        self.assertDictEqual(newCoursePlan.get_json(), {"Plan ID":"1", "Student ID":"816031123", "Semester ID":"SEMI2k23"})


       
class EasiestCoursesUnitTests(unittest.TestCase):

    def test_new_easiest_courses(self):
        newEasiestCourses = EasiestCourses("SEMI2k23", "30")
        assert(newEasiestCourses.semesterID, newEasiestCourses.programID) == ("SEMI2k23", "30")

    def test_easiest_courses_toJSON(self):
        newEasiestCourses = EasiestCourses("SEMI2k23", "30")
        self.assertDictEqual(newEasiestCourses.get_json(), {"Easiest Courses ID":"EC001", "Semester ID":"SEMI2K23", "Program ID":"30"})

class FastestGraduationUnitTests(unittest.TestCase):

    def test_new_fastest_graduation(self):
        newFastestGraduation = FastestGraduation("SEMI2k23", "31")
        assert(newFastestGraduation.semesterID, newFastestGraduation.programID) == ("SEMI2k23", "31")

    def test_fastest_graduation_toJSON (self):
        newFastestGraduation = FastestGraduation("SEMI2k23", "31")
        self.assertDictEqual(newFastestGraduation.get_json(), {"Fastest Graduation  ID":"EC001", "Semester ID":"SEMI2K23", "Program ID":"31"})

class ElectivePriorityUnitTests(unittest.TestCase):

    def test_new_fastest_graduation(self):
        newElectivePriority = ElectivePriority("SEMI2k23", "32")
        assert(newElectivePriority.semesterID, newElectivePriority.programID) == ("SEMI2k23", "32")

    def test_fastest_graduation_toJSON (self):
        newElectivePriority = ElectivePriority("SEMI2k23", "32")
        self.assertDictEqual(newElectivePriority.get_json(), {"Elective Priority   ID":"EC001", "Semester ID":"SEMI2K23", "Program ID":"32"})

class CoursePlanDirectorUnitTest(unittest.TestCase):

    def test_new_course_plan_director(self):
        newCoursePlanDirector = CoursePlanDirector("ElectivePriority", "elective")
        assert(newCoursePlanDirector.builder, newCoursePlanDirector.category) == ("ElectivePriority", "elective")

    

@pytest.fixture(autouse=True, scope="module")
def empty_db():
    app = create_app({'TESTING': True, 'SQLALCHEMY_DATABASE_URI': 'sqlite:///test.db'})
    create_db()
    yield app.test_client()
    db.drop_all()


"Integration Tests" 
class CoursePlanIntegrationTests(unittest.TestCase):

    def setUp(self):
        # Set up a student for testing
        self.student = add_student("816021675", "Ella", "Mable", "emable@example.com", "mabella", "ella123", "Information Technology Major", "Mathematics Major")

    def test_create_course_plan(self):
        student_id = self.student.studentID
        course_plan = create_course_plan(student_id)
        retrieved_course_plan = get_course_plan(course_plan.planID)

        self.assertEqual(retrieved_course_plan.studentID, student_id)

    def test_add_course_to_plan(self):
        course = create_course("COMP 2603", "Object-Oriented Programming II", 3, 4)
        course_plan = create_course_plan(self.student.studentID)
        updated_course_plan = add_course_to_plan(course, course_plan)
        retrieved_course_plan = get_course_plan(course_plan.planID)

        self.assertTrue(any(c.courseCode == course.courseCode for c in retrieved_course_plan.courses))

    def test_remove_course_from_plan(self):
        course = create_course("COMP3201", "Data Analytics", 3, 8)
        course_plan = create_course_plan(self.student.studentID)
        add_course_to_plan(course, course_plan)
        updated_course_plan = remove_course_from_plan(course, course_plan)
        retrieved_course_plan = get_course_plan(course_plan.planID)

        self.assertFalse(any(c.courseCode == course.courseCode for c in retrieved_course_plan.courses))
    
    def test_autogenerate(self):
        student = add_student("123456789", "John", "Doe", "john.d@example.com", "john_doe", "password123", "Mathematics Major", "Statistics Major")
        program = create_program("DCIT", "Information Technology Special", 30, 15, 12)
        semester = create_semester(2023, 2)
        
        autogenerate_result = autogenerator(student, "Elective Priority", "Special", program.programID, semester.semesterID)
        student_plans = get_student_plans(student)

        expected_plan = {
            'planType': "Elective Priority",
            'degreeType': "Special",
            'programID': program.programID,
            'semesterID': semester.semesterID
        }

        self.assertTrue(autogenerate_result)
        self.assertIsNotNone(student_plans)
        self.assertGreater(len(student_plans), 0)

        found_autogenerated_plan = any(plan == expected_plan for plan in student_plans)
        self.assertTrue(found_autogenerated_plan)



