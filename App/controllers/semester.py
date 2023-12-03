from App.database import db
from App.models import Semester

def create_semester(year, semestertype):
    new_semester = Semester(year=year, semestertype=semestertype)
    db.session.add(new_semester)
    db.session.commit()
    return new_semester

def get_semester_by_id(semester_id):
   return Semester.query.get(semester_id)

def get_all_semesters():
    return Semester.query.all()

def get_courses_in_semester(year, semesterType):
    semester = Semester.query.filter_by(year = year, semesterType = semesterType).first()
    if semester: 
        return semester.courses
    return None

def update_semester(semester, new_year, new_semestertype):
    semester.year = new_year
    semester.semestertype = new_semestertype
    db.session.commit()
    return semester


def add_semester_course(course_code, semester_id):
    course = Course.query.get(course_code).first()
    if not course:
        return None

    semester = Semester.query.get(semester_id).first()
    if not semester:
        return None

    return semester.add_course(course)


def remove_semester_course(course_code, semester_id):
    course = Course.query.get(course_code).first()
    if not course:
        return None

    semester = Semester.query.get(semester_id).first()
    if not semester:
        return None

    return semester.remove_course(course)


# Get all semester courses
def get_all_semester_courses():
    return SemesterCourse.query.all()


def get_upcoming_semester():
    return Semester.query.order_by(SemesterHistory.semesterID.desc()).first()