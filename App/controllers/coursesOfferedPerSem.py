from App.models import CoursesOfferedPerSem
from App.controllers import get_course_by_courseCode
from App.database import db

def add_semester_courses(course_code):
    course = get_course_by_courseCode(course_code)
    if course:
        sem_courses = CoursesOfferedPerSem(code=course_code)
        db.session.add(sem_courses)
        db.session.commit()
        return sem_courses
    else:
        print("Course not found")

def delete_all_records():
    try:
        db.session.query(CoursesOfferedPerSem).delete()
        db.session.commit()
        print("All records deleted successfully.")

    except Exception as e:
        db.session.rollback()
        print(f"An error occurred: {str(e)}")

def is_course_offered(course_code):
    course = CoursesOfferedPerSem.query.filter_by(code=course_code).first()
    return True if course else False

def get_all_courses_alphabetical():
    courses = CoursesOfferedPerSem.query.order_by(CoursesOfferedPerSem.code).all()
    return courses

def get_all_offered_codes():
    offered = get_all_courses_alphabetical()
    offered_codes = [c.code for c in offered]
    return offered_codes
