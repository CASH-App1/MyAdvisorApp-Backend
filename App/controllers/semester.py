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

def get_courses_in_semester(semester):
    return semester.courses

def update_semester(semester, new_year, new_semestertype):
    semester.year = new_year
    semester.semestertype = new_semestertype
    db.session.commit()
    return semester
