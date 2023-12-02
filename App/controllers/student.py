from App.models import Student, CoursePlan, Program
from App.controllers import (get_program_by_name)
from App.database import db

# Controller to add a new student
def add_student(studentID, first_name, last_name, email):
    new_student = Student(, studentID=studentID, firstName=first_name, lastName=last_name, email=email)
    db.session.add(new_student)
    db.session.commit()
    return new_student

# Controller to get a student by username (student_id)
def get_student(studentID):
    return Student.query.filter_by(studentID=student_studentID).first()

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





