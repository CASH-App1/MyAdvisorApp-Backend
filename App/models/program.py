from App.database import db
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from App.models import *

class Program(db.Model):
    programID = Column(db.Integer, primary_key=True)
    departmentCode = Column(db.String(10), ForeignKey(Department.departmentCode), nullable=False)
    programName = Column(db.String, nullable=False)
    coreCredits = Column(db.Integer, nullable=False)
    electiveCredits = Column(db.Integer, nullable=False)
    founCredits = Column(db.Integer, nullable=False)

    coreCourses = db.relationship('Course', secondary = 'program_courses', backref=db.backref('coreProgram', lazy='joined'))
    electiveCourses = db.relationship('Course', secondary = 'program_courses', backref=db.backref('electiveProgram', lazy='joined'))
    founCourses = db.relationship('Course', secondary = 'program_courses', backref=db.backref('founProgram', lazy='joined'))

    def __init__(self, department_code, program_name, core_credits, elective_credits, foun_credits):
        self.departmentCode = department_code
        self.programName = program_name
        self.coreCredits = core_credits
        self.electiveCredits = elective_credits
        self.founCredits = foun_credits
        

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

    def get_json(self):
        return{
            'Program ID': self.programID,
            'Department Code': self.departmentCode,
            'Program Name': self.programName,
            'Core Credits' : self.coreCredits,
            'Elective Credits': self.electiveCredits,
            'Foundation Credits': self.founCredits
        }