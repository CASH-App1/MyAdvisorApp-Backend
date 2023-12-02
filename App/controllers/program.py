from App.models import Program
from App.database import db

def create_program(department_code, program_name, core_credits, elective_credits, foun_credits):
    newProgram = Program(department_code, program_name, core_credits, elective_credits, foun_credits)
    db.session.add(newProgram)
    print("Program successfully created")
    db.session.commit()
    return newProgram
    
    

def get_program_by_name(program_name):
    return Program.query.filter_by(programName=program_name).first()

def get_program_by_id(program_id):
    return Program.query.get(program_id)
def get_core_credits(program_id):
    program = get_program_by_id(program_id)
    return program.coreCredits if program else 0

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


