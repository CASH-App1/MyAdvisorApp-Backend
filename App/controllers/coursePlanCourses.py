from App.models import CoursePlanCourses, CoursePlan, Course
from App.database import db

def create_course_plan_courses(plan_id, course_code):
    new_course_plan_courses = CoursePlanCourses(coursePlanID=plan_id, courseCode=course_code)
    db.session.add(new_course_plan_courses)
    db.session.commit()
    return new_course_plan_courses

def edit_course_plan_courses(course_plan_course_id, plan_id, course_code):
    course_plan_courses = CoursePlanCourses.query.get(course_plan_course_id)

    if course_plan_courses:
        course_plan_courses.coursePlanID = plan_id
        course_plan_courses.courseCode = course_code
        db.session.commit()
        return course_plan_courses
    else:
        return None

def get_courses_by_plan_id(plan_id):
    return CoursePlanCourses.query.filter_by(coursePlanID=plan_id).all()

def get_course_plan_by_id(course_plan_course_id):
    course_plan_courses = CoursePlanCourses.query.get(course_plan_course_id)
    return course_plan_courses.coursePlan if course_plan_courses else None
