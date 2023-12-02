from App.models import Program
from App.database import db

def create_program(department_code, program_name, core_credits, elective_credits, foun_credits):
    program = Program.query.filter_by(programName = program_name).first()
    if program:
        return None

    newProgram = Program(department_code, program_name, core_credits, elective_credits, foun_credits)
    department = Department.query.get(department_code).first()
    if department:
        department.programs.append(newProgram)
        db.session.add(newProgram)
        db.session.commit()
        return newProgram
    return None

def add_program_prerequisites(programName, courseCode, courseType):
    program = Program.query.filter_by(programName = programName)
    course = Course.query.filter_by(courseCode = courseCode).first()
    if program and course:
        program.add_course(courseCode, courseType)
        db.session.commit()

def get_all_programCourses(programName):
    program = Program.query.filter_by(programName = program_name).first()
    if program:
        return ProgramCourses.query.filter_by(programID = program.programID).all()
    return None

def check_prerequisite_exists(programName, courseCode):
    program = Program.query.filter_by(programName = program_name).first()
    course = Course.query.get(courseCode = courseCode).first()
    if course and program:
        return ProgramCourses.query.filter_by(program_id= program.programID, course_code = courseCode).first()
    return None
    

def get_program_by_name(program_name):
    program = Program.query.filter_by(programName=program_name).first()
    if program:
        return program
    return None

def get_program_by_id(program_id):
    program = Program.query.get(program_id)
    if program:
        return program
    return None

def get_core_credits(program_id):
    program = get_program_by_id(program_id)
    if program:
        return program.coreCredits else 0

def get_core_courses(program_id):
    program = get_program_by_id(program_id)
    courses = program.coreCourses
    return courses if program else []

def get_elective_credits(program_id):
    program = get_program_by_id(program_id)
    return program.electiveCredits if program else 0

def get_elective_courses(program_id):
    program = get_program_by_id(program_id)
    courses = program.electiveCourses
    return courses if program else []

def get_foun_credits(program_name):
    program = get_program_by_name(program_name)
    return program.founCredits if program else 0

def get_foun_courses(program_name):
    program = get_program_by_name(program_name)
    courses = program.founCourses
    return courses if program else []

def get_all_courses(program_name):
    core_courses = get_core_courses(program_name)
    elective_courses = get_elective_courses(program_name)
    foun_courses = get_foun_courses(program_name)

    all_courses = core_courses + elective_courses + foun_courses
    return all_courses


