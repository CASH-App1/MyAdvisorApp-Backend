from App.models import CourseHistory
from App.database import db

def create_course_history(course_code, grade_letter, percent, course_type, semester_id):
    new_course_history = CourseHistory(
        courseCode=course_code,
        gradeLetter=grade_letter,
        percent=percent,
        courseType=course_type,
        semesterID=semester_id
    )

    db.session.add(new_course_history)
    db.session.commit()
    return new_course_history

def edit_course_history(course_history_id, course_code, grade_letter, percent, course_type, semester_id):
    course_history = CourseHistory.query.get(course_history_id)

    if course_history:
        course_history.courseCode = course_code
        course_history.gradeLetter = grade_letter
        course_history.percent = percent
        course_history.courseType = course_type
        course_history.semesterID = semester_id

        db.session.commit()
        return course_history
    else:
        return None

def get_grade_letter(course_history_id):
    course_history = CourseHistory.query.get(course_history_id)
    return course_history.gradeLetter if course_history else None
