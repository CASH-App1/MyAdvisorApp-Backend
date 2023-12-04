from App.database import db
from App.models import *
import json

class Course(db.Model):
    
    courseCode = db.Column(db.String(8), primary_key=True)
    courseName = db.Column(db.String(100), nullable=False)
    credits = db.Column(db.Integer, nullable=False, )
    difficulty = db.Column(db.Integer, nullable=False)
    
    prerequisites = db.relationship('Course', secondary='course_prereq', primaryjoin='Course.courseCode == course_prereq.c.courseID', secondaryjoin='Course.courseCode == course_prereq.c.prereqID', backref=db.backref('prerequisite_for', lazy='dynamic'))

    def __init__(self, courseCode, courseName, credits, difficulty):
        self.courseCode = courseCode
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

        return{
            'Course Code': self.courseCode,
            'Course Name': self.courseName,
            'Credits': self.credits,
            'Difficulty': self.difficulty
        }
    
    
