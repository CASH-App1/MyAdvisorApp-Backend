from App.models import Student, CoursePlan, Program
from App.controllers import (get_program_by_name)
from App.database import db

# Controller to add a new student
def add_student(studentID, first_name, last_name, email, username, password, program1, program2):
    user = User.query.filter_by(username = username).first()
    if not user:
        new_student = Student(, studentID=studentID, firstName=first_name, lastName=last_name, email=email)
        program = Program.query.filter_by(programName = row['program1'])
        if program:
            new_student.programs.append(program)

            program = Program.query.filter_by(programName = row['program2'])
            if program:
                newStudent.programs.append(program)
            
            db.session.add(new_student)
            db.session.commit()
            return new_student
    return None

# Controller to get a student by username (student_id)
def get_student(studentID):
    student = Student.query.get(studentID).first()
    if student:
        return student
    return None

# Controller to get a list of all students
def get_all_students():
    students = Student.query.all()
    student_data = [{'studentID': student.studentID, 'firstName': student.firstName, 'lastName': student.lastName, 'email': student.email} for student in students]
    return student_data

# Controller to get a list of students with a specific first name and last name
def get_students_by_name(first_name, last_name):
    students = Student.query.filter_by(firstName=first_name, lastName=last_name).all()
    
    # Create a list of dictionaries containing student data
    student_search = [{'studentID': student.studentID, 'firstName': student.firstName, 'lastName': student.lastName, 'email':student.email} for student in students]
    return student_search
    
# Controller to update a student
def update_student(studentID, new_first_name, new_last_name, new_email):
    student = Student.query.get(studentID)
    if student:
        student.firstName = new_first_name
        student.lastName = new_last_name
        student.email = new_email
        db.session.add(student)
        db.session.commit()
        return student
    return None





