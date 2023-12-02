from App.models import EasiestCourses, CoursePlan, Program, SemesterCourse, Student
from App.database import db

def create_easiest_course_plan(student_id):
  easiest_courses = EasiestCourses(student_id)
  return easiest_courses

def update_easiest_course_plan(easiest_courses, semester_id, program_id, num_courses):
    easiest_courses.reset(student_id)
    easiest_courses.set_semester(semester_id)
    easiest_courses.set_program(program_id)
    easiest_courses.set_courses(num_courses)

def get_easiest_course_plan(easiest_courses):
    return easiest_courses.get_plan()

def get_easiest_course_plan_json(easiest_courses):
    return easiest_courses.get_json()

    
