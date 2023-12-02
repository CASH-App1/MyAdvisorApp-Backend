from App.models import Course, Prerequisites
from App.controllers.prerequistes import (create_prereq, get_all_prerequisites)
from App.database import db
import json, csv


def create_course(code, courseName, credits, difficulty):
    course = Course.query.filter_by(courseCode = code).first()
    if not course:
        prereqID = Prerequisite(code)
        course = Course(code, prereqID, courseName, credits, difficulty)    
        db.session.add(course)
        db.session.commit()
        return course
    return None


    
def get_course_by_courseCode(code):
    course = Course.query.get(code).first()
    if course:
        return course
    return None

def courses_Sorted_byDifficulty():
    courses =  Course.query.order_by(Course.difficulty.asc()).all()
    codes = []

    for c in courses:
        codes.append(c.courseCode)
    
    return codes

def courses_Sorted_byDifficulty_Objects():
    return Course.query.order_by(Course.difficulty.asc()).all()
    
# def get_prerequisites(prereqID):
#     course = get_course_by_courseCode(code)
#     prereqs = get_all_prerequisites(course.courseName)
#     return prereqs

def get_credits(code):
    course = get_course_by_courseCode(code)
    return course.credits if course else 0

def get_ratings(code):
    course = get_course_by_courseCode(code)
    return course.rating if course else 0



