from App.models import *
from App.controllers import *
from App.database import db

def create_course_plan(student_id, semesterID):
    new_course_plan = CoursePlan(student_id, semesterID)
    db.session.add(new_course_plan)
    db.session.commit()
    return new_course_plan


def add_course_to_plan(course, plan):
    course_plan = CoursePlan.query.get(plan.planID)
    course = Course.query.get(course.courseCode)

    if course_plan and course:
        course_plan.courses.append(course)
        db.session.commit()
        return course_plan
    return None

def remove_course_from_plan(course, plan):
    course_plan = CoursePlan.query.get(plan.planID)
    course = Course.query.get(course.courseCode)

    if course_plan and course:
        course_plan.courses.remove(course)
        db.session.commit()
        return course_plan
    return None


def get_course_plan(planID):
    return CoursePlan.query.get(planID)


def autogenerator(student, planType, degreeType, programID, semesterID):
    return student.autogenerateCoursePlan(planType, degreeType, programID, semesterID)
