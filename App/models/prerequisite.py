from App.database import db
from sqlalchemy.orm import relationship
from App.models import Course

class Prerequisite(db.Model):
    prereqID = db.Column(db.Integer,primary_key= True)
    courseCode= db.Column(db.String(8), db.ForeignKey('course.courseCode'), nullable=False)
    prerequisiteCourses= db.relationship('Prerequisite', backref= db.backref('course', lazy='joined'))
    
    def __init__(self, course_code):
        self.courseCode = course_code

        
    def addPrerequisite(self, prereq_course):
        self.prerequisiteCourses.append(prereq_course)
        db.session.commit()
    

    def edit_course(self, courseCode):
        # self.courseName = course_name
        self.courseCode = course_code
        # self.credits = credits
        # self.difficulty = difficulty
        db.session.commit()
