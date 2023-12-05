from App.models import *
from App.controllers import *
from App.database import db
import json, csv


def create_course(code, courseName, credits, difficulty):
    course = Course.query.get(code)
    if not course:
        #prereqID = Prerequisite(code)
        course = Course(code,courseName, credits, difficulty)    
        db.session.add(course)
        db.session.commit()
        return course
    return None

    
def get_course_by_courseCode(code):
    return Course.query.get(code)
   

def check_prerequisites(course, student):
    qualify =0
    #prereq = Prerequisite.query.get(course.prereqID).first()
    if len(course.prerequisites) > 0:
        for p in course.prerequisites:
            for s in student.studentHistory:
                for c in s.courses:
                    if p.courseCode == c.courseCode:
                        qualify += 1
    
    if len(course.prerequisites) == 0 or len(course.prerequisites) == qualify:
        return True
    return False