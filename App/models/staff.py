from .user import User 
from App.database import db
from sqlalchemy import Column, Integer, Date, ForignKey

class Staff(User):
    
    staffID = db.Column(db.Integer, primary_key=True)
    departmentCode = db.Column(db.String(10), db.ForeignKey(department.departmentCode), nullable = False)
    firstName = db.Column(db.String(50), nullable = False)
    lastName = db.Column(db.String(50), nullable = False)
    email = db.Column(db.String(254),nullable = False )

    department = relationship('Department', backref='staff_members')
    created_programs = relationship('Program', backref=db.backref('program', lazy='joined'))
    created_courses = relationship('Course', backref=db.backref('course', lazy='joined'))
    created_semesters = relationship('Semester', backref=db.backref('semester', lazy='joined'))

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
       

       
