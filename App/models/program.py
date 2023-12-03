from App.database import db
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Program(db.Model):
    programID = Column(db.Integer, primary_key=True)
    departmentCode = Column(db.String(10), ForeignKey('department.departmentCode'), nullable=False)
    programName = Column(db.String, nullable=False)
    coreCredits = Column(db.Integer, nullable=False)
    electiveCredits = Column(db.Integer, nullable=False)
    founCredits = Column(db.Integer, nullable=False)

    coreCourses = db.relationship('Course', secondary = 'program_courses', backref=db.backref('course', lazy='joined'))
    electiveCourses = db.relationship('Course', secondary = 'program_courses', backref=db.backref('course', lazy='joined'))
    founCourses = db.relationship('Course', secondary = 'program_courses', backref=db.backref('course', lazy='joined'))

    def __init__(self, department_code, program_name, core_credits, elective_credits, foun_credits):
        self.departmentCode = department_code
        self.programName = program_name
        self.coreCredits = core_credits
        self.electiveCredits = elective_credits
        self.founCredits = foun_credits
        
    students = relationship('Student', backref='program')

    def add_course(self, course_code, course_type):
        
        course = Course.query.get(course_code)
        if course:
            if course_type == 'core':
                self.coreCourses.append(course)
            elif course_type == 'elective':
                self.electiveCourses.append(course)
            elif course_type == 'foundation':
                self.founCourses.append(course)
            db.session.commit()

    def __repr__(self):
        return f"<Program {self.programID} - {self.programName}>"
