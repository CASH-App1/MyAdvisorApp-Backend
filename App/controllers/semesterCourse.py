from App.database import db
from App.models import SemesterCourse

# Create a semester course
def create_semester_course(course_code, semester_id):
    new_semester_course = SemesterCourse(course_code=course_code, semester_id=semester_id)
    db.session.add(new_semester_course)
    db.session.commit()
    return new_semester_course

# List all courses for a given semester
def list_courses_for_semester(semester):
    return semester.semester_courses

# Get a semester course by ID
def get_semester_course_by_id(semester_course_id):
    return SemesterCourse.query.get(semester_course_id)

# Get all semester courses
def get_all_semester_courses():
    return SemesterCourse.query.all()
