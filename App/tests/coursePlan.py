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


