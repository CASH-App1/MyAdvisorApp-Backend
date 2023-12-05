from App.database import db
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from App.models import *

class SemesterCourse(db.Model):
    __tablename__ = 'semester_courses'

    semesterCourseID = Column(db.Integer, primary_key=True)
    courseCode = Column(db.String(8), ForeignKey(Course.courseCode), nullable=False)
    semesterID = Column(db.Integer, ForeignKey(Semester.semesterID), nullable=False)

    # semester = relationship('Semester', backref=db.backref('semester_courses'))
    # course = relationship('Course', backref=db.backref('semester_courses'))

    def __init__(self, course_code, semester_id):
        self.courseCode = course_code
        self.semesterID = semester_id

    def __repr__(self):
        return f"<SemesterCourse {self.semesterCourseID}>"

    def get_json(self):
        return{
            'Semester Course ID': self.semesterCourseID,
            'Course Code': self.courseCode,
            'Semester ID': self.semesterID
        }