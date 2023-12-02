from App.models import ProgramCourse, Program, Course
from App.controllers import ( get_program_by_id, get_course_by_courseCode)
from App.database import db

def create_program_course(course_code, program_id):
    new_program_course = ProgramCourse(course_code=course_code, program_id=program_id)
    db.session.add(new_program_course)
    db.session.commit()
    return new_program_course

def update_program_course(program_course_id, course_code, program_id):
    program_course = ProgramCourse.query.get(program_course_id)

    if program_course:
        program_course.courseCode = course_code
        program_course.programID = program_id
        db.session.commit()
        return program_course
    else:
        return None

def add_program_to_program_course(program_course_id, program_id):
    program_course = ProgramCourse.query.get(program_course_id)
    program = get_program_by_id(program_id)

    if program_course and program:
        program_course.program = program
        db.session.commit()
        return program_course
    else:
        return None

def add_course_to_program_course(program_course_id, course_code):
    program_course = ProgramCourse.query.get(program_course_id)
    course = get_course_by_courseCode(course_code)

    if program_course and course:
        program_course.course = course
        db.session.commit()
        return program_course
    else:
        return None
