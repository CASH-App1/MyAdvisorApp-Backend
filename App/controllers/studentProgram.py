from App.database import db
from App.models import StudentProgram, Student, Program

# Create a StudentProgram
def create_student_program(student_id, program_id):
    new_student_program = StudentProgram(student_id=student_id, program_id=program_id)
    db.session.add(new_student_program)
    db.session.commit()
    return new_student_program

# Get a StudentProgram by ID
def get_student_program_by_id(student_program_id):
    return StudentProgram.query.get(student_program_id)

# Get all StudentPrograms
def get_all_student_programs():
    return StudentProgram.query.all()
