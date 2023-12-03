from App.database import db
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship

class Semester(db.Model):
    semesterID= db.Column(db.Integer, primary_key = True) 
    courses= db.relationship('SemesterCourse', backref=db.backref('course', lazy='joined'))
    year = db.Column(db.Integer, nullable = False)
    semesterType= db.Column(db.Integer, nullable = False)

    def __init__(self, year, semestertype):
        self.year = year
        self.semesterType = semestertype

    def add_course(course):
        if course not in self.courses:
            self.courses.append(course)
            db.session.commit()
            return True

    def remove_course(course):
        self.courses.remove(course)
        db.session.commit()
        return True
