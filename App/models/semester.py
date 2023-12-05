from App.database import db
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from App.models import *


class Semester(db.Model):
  semesterID = db.Column(db.Integer, primary_key=True)
  courses = db.relationship('Course',
                            secondary='semester_courses',
                            backref=db.backref('semester', lazy='joined'))
  year = db.Column(db.Integer, nullable=False, unique=True)
  semesterType = db.Column(db.Integer, nullable=False, unique=True)

  def __init__(self, year, semestertype):
    self.year = year
    self.semesterType = semestertype

  def add_course(self, course):
    if course not in self.courses:
      self.courses.append(course)
      db.session.commit()
      
      return True

  def remove_course(self, course):
    self.courses.remove(course)
    db.session.commit()
    return True

  def __repr__(self):
    return f"Semester {self.semesterType} - {self.year}"

  def get_json(self):
        courses = []
        for c in self.courses:
            courses.append(c.get_json())
            
        return{
            'Semester ID': self.semesterID,
            'Courses': courses,
            'Semester Year': self.year,
            'Semester Type': self.semesterType
        }