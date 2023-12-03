from App.models import Prerequisite, Course
from App.database import db

def get_prerequisite_courses(prereq_id):
    prerequisite = Prerequisite.query.get(prereq_id)

    if prerequisite:
        return prerequisite.prerequisiteCourses
    else:
        return None

def get_all_prereq_ids():
    all_prereq_ids = Prerequisite.query.with_entities(Prerequisite.prereqID).all()
    return [prereq_id for (prereq_id,) in all_prereq_ids]

def get_course_code_by_prereq_id(prereq_id):
    prerequisite = Prerequisite.query.get(prereq_id)

    if prerequisite:
        return prerequisite.courseCode
    else:
        return None
