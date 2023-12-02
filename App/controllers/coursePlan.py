from App.models import CoursePlan, Course, Student
from App.database import db

def create_course_plan(student_id, semester_id, program_id):
    new_course_plan = CoursePlan(studentID=student_id, semesterID=semester_id, program=program_id)
    db.session.add(new_course_plan)
    db.session.commit()
    return new_course_plan

def add_course_to_plan(plan_id, course_code):
    course_plan = CoursePlan.query.get(plan_id)
    course = Course.query.get(course_code)

    if course_plan and course:
        course_plan.courses.append(course)
        db.session.commit()
        return course_plan
    else:
        return None

def remove_course_from_plan(plan_id, course_code):
    course_plan = CoursePlan.query.get(plan_id)
    course = Course.query.get(course_code)

    if course_plan and course:
        course_plan.courses.remove(course)
        db.session.commit()
        return course_plan
    else:
        return None

def get_courses_of_plan(plan_id):
    course_plan = CoursePlan.query.get(plan_id)
    return course_plan.courses if course_plan else []

def get_student_id_from_plan(plan_id):
    course_plan = CoursePlan.query.get(plan_id)
    return course_plan.studentID if course_plan else None
