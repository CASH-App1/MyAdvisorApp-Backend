from App.database import db
from App.models import *

class CoursePlan(db.Model):
    planID = db.Column(db.Integer, primary_key=True)
    studentID = db.Column(db.Integer,  db.ForeignKey(Student.studentID), nullable=False)
    semesterID = db.Column(db.Integer,  db.ForeignKey(Semester.semesterID))
    program = db.Column(db.Integer, db.ForeignKey(Program.programID))
    courses = db.relationship('Course', secondary = 'course_plan_courses', backref = 'coursePlan', lazy = True)

    def __init__(self, studentid):
        self.studentId = studentid
        

    def get_json(self):
        courses = []
        for c in self.courses:
            courses.append(c.get_json())
            
        return{
            'Plan ID': self.planId,
            'Student ID': self.studentId,
            'Semester ID': self.semesterID,
            'Program ID': self.program,
            'Courses': courses
        }