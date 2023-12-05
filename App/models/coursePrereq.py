from App.database import db
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from App.models import *

class CoursePrereq(db.Model):
  __tablename__ = 'course_prereq'
  coursePrereqID = db.Column(db.Integer, primary_key = True)
  courseID = db.Column(db.Integer, db.ForeignKey(Course.courseCode))
  prereqID = db.Column(db.Integer, db.ForeignKey(Course.courseCode))
  
  