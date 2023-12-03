from App.database import db
#from App.models import prerequisite
import json

class Course(db.Model):
    
    courseCode = db.Column(db.String(8), primary_key=True)
    prereqID = db.Column(db.Integer, db.ForeignKey('prerequisite.prereqID'))
    courseName = db.Column(db.String(100), nullable=False)
    credits = db.Column(db.Integer, nullable=False, )
    difficulty = db.Column(db.Integer, nullable=False)
    
    prerequisites = db.relationship('Prerequisite', backref=db.backref('course',lazy='joined'))

    def __init__(self, courseCode, prereqID, courseName, credits, difficulty):
        self.courseCode = courseCode
        self.prereqID = prereqID
        self.courseName = courseName
        self.credits = credits
        self.difficulty = difficulty


    def add_prerequisite(self, prerequisite_code): 
        prerequisite_course = Course.query.get(prerequisite_code)
        if prerequisite_course:
            self.prerequisites.append(prerequisite_course)
            db.session.commit()

    def edit_course(self, course_name, course_code, credits, difficulty):
        self.courseName = course_name
        self.courseCode = course_code
        self.credits = credits
        self.difficulty = difficulty
        db.session.commit()

    def get_json(self):
        courses = [c.get_json() in self.courses]
        return{
            'Course Code': self.courseCode,
            'Course Name': self.courseName,
            'Credits': self.credits,
            'Difficulty': self.difficulty
        }
    
    
