from App.models import Course, Prerequisites
from App.controllers.prerequistes import (create_prereq, get_all_prerequisites)
from App.database import db
import json, csv


def create_course(code, courseName, credits, difficulty):
    course = Course.query.get(courseCode = code).first()
    if not course:
        prereqID = Prerequisite(code)
        course = Course(code, prereqID, courseName, credits, difficulty)    
        db.session.add(course)
        db.session.commit()
        return course
    return None

    
def get_course_by_courseCode(code):
    return Course.query.get(code).first()
   

def check_prerequisites(course, student):
    qualify =0
    prereq = Prerequisite.query.get(course.prereqID).first()
    if prereq.prerequisiteCourses.count() > 0:
        for p in prereq.prerequisiteCourses:
            for s in student.studentHistory:
                for c in s.courses:
                    if p.courseCode == c.courseCode:
                        qualify += 1
    
    if prereq.prerequisiteCourses.count() == 0 or prereq.prerequisiteCourses.count() == qualify:
        return True
    return False