from App.database import db
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

class SemesterCourse(db.Model):
    __tablename__ = 'semester_courses'

    semesterCourseID = Column(db.Integer, primary_key=True)
    courseCode = Column(db.String(8), ForeignKey('courses.courseCode'), nullable=False)
    semesterID = Column(db.Integer, ForeignKey('semesters.semesterID'), nullable=False)

    semester = relationship('Semester', backref=db.backref('semester_courses'))
    course = relationship('Course', backref=db.backref('semester_courses'))

    def __init__(self, course_code, semester_id):
        self.courseCode = course_code
        self.semesterID = semester_id

    def __repr__(self):
        return f"<SemesterCourse {self.semesterCourseID}>"
