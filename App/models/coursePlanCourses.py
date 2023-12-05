from App.database import db
from App.models import *
from sqlalchemy import Column, Integer, Date, ForeignKey

class CoursePlanCourses(db.Model):
  __tablename__ = 'course_plan_courses'
  coursePlanCourseID = db.Column(db.Integer, primary_key=True)
  coursePlanID = db.Column(db.Integer, db.ForeignKey(CoursePlan.planID))
  courseCode = db.Column(db.Integer, db.ForeignKey(Course.courseCode))


