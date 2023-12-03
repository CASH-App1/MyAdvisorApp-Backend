from App.database import db
from App.models import CoursePlan, Course
from sqlalchemy import Column, Integer, Date, ForeignKey

class CoursePlanCourses(db.Model):
    coursePlanCourseID = db.Column(db.Integer, primary_key=True)
    coursePlanID = db.Column(db.Integer, db.ForeignKey('coursePlan.planID'))
    courseCode = db.Column(db.Integer, db.ForeignKey('course.courseCode'))
    # coursePlan = db.relationship('CoursePlan', backref = 'courses', lazy = True)
    # course = db.relationship('Course', backref = 'coursePlans', lazy = True)


