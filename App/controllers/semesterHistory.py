from App.database import db
from App.models import SemesterCourse, SemesterHistory


# Create a semester history
def create_semester_history(student_id, year, semester_type):
    new_semester_history = SemesterHistory(student_id=student_id, year=year, semester_type=semester_type)
    db.session.add(new_semester_history)
    db.session.commit()
    return new_semester_history

# List all courses for a given semester history
def list_courses_for_semester_history(semester_history):
    courses = []
    for semester_course in semester_history.semester_courses:
        courses.append({
            'course_code': semester_course.course_code,
            'course_name': semester_course.course.course_name  # Replace with actual attribute
        })
    return courses


# List all courses for a given semester
def list_courses_for_semester(semester):
    return semester.semester_courses

# Get a semester course by ID
def get_semester_course_by_id(semester_course_id):
    return SemesterCourse.query.get(semester_course_id)

# Get all semester courses
def get_all_semester_courses():
    return SemesterCourse.query.all()



