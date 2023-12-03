from .user import User 
from App.database import db
from sqlalchemy import Column, Integer, Date, ForeignKey
from App.models import Department, User

class Staff(User):
    
    staffID = db.Column(db.Integer, primary_key=True)
    departmentCode = db.Column(db.String(10), db.ForeignKey('department.departmentCode'), nullable = False)
    userID = db.Column(db.Integer, db.ForeignKey('user.id'))

    department = db.relationship('Department', backref='staff_members')
    created_programs = db.relationship('Program', backref=db.backref('program', lazy='joined'))
    created_courses = db.relationship('Course', backref=db.backref('course', lazy='joined'))
    created_semesters = db.relationship('Semester', backref=db.backref('semester', lazy='joined'))

    def __init__(self, staffID, departmentCode, firstName, lastName, email, username, password):
        user = super().__init__(username, password, firstName, lastName, email)
        self.staffID = staffID
        self. departmentCode = departmentCode
        self.userID = user.id

    def create_program(self, departmentCode, programName, coreCredits, electiveCredits, foundCredits):
        program = Program(self, departmentCode, programName, coreCredits, electiveCredits, foundCredits)
        db.session.add(program)
        db.session.commit()
      
    def create_course(self, courseCode, prereqID, courseName, credits, difficulty):
        course = Course(self, courseCode, prereqID, courseName, credits, difficulty)
        db.session.add(course)
        db.session.commit()

    def create_semester(self, year, semestertype):
        semester = Semester(self, year, semestertype)
        db.session.add(semester)
        db.session.commit()

    def remove_program(self, program_name):
        program = Program.query.filter_by(programName=program_name, creator=self).first()
        if program:
            db.session.delete(program)
            db.session.commit()
            
    def __repr__(self):
        return f"<Staff {self.staffID} - {self.firstName} {self.lastName}>"
       

       
