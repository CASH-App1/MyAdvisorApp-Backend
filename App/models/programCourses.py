from App.database import db
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

class ProgramCourse(db.Model):
    __tablename__ = 'program_courses'

    programCourseID = Column(db.Integer, primary_key=True)
    courseCode = Column(db.String(8), ForeignKey('courses.courseCode'), nullable=False)
    programID = Column(db.Integer, ForeignKey('programs.programID'), nullable=False)

    program = relationship('Program', backref=db.backref('program_courses'))
    course = relationship('Course', backref=db.backref('program_courses'))

    def __init__(self, course_code, program_id):
        self.courseCode = course_code
        self.programID = program_id

    def __repr__(self):
        return f"<ProgramCourse {self.programCourseID}>"
