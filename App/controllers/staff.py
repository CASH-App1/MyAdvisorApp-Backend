from App.models import *
from App.controllers import *
from App.database import db


def create_staff(staff_id, department_code, first_name, last_name, email, username, password):
    user = User.query.filter_by(username = username).first()
    if not user:
        new_staff = Staff(staff_id, department_code,first_name,last_name, email, username, password)
        department = Department.query.get(department_code)
        if department:
            department.staffMembers.append(new_staff)
            db.session.add(new_staff)
            db.session.commit()
            return new_staff
    return None

def get_staff_by_id(ID):
    staff = Staff.query.get(ID)
    if staff:
        return staff
    return None

def get_all_staff():
    return Staff.query.all()

def update_staff(staffID, new_departmentCode, new_firstName, new_lastName, new_email, new_username, new_password):
    staff = Staff.query.get(staffID)
    if staff:
        staff.departmentCode = new_departmentCode
        staff.firstName = new_firstname
        staff.lastName = new_lastName
        staff.email = new_email
        staff.username = new_username
        staff.password = new_password
        db.session.add(staff)
        db.session.commit()
        return staff
    return None


# def add_program(self, program_name, description):
#     try:
#         new_program = Program(name=program_name, description=description)
#         db.session.add(new_program)
#         db.session.commit()
#         return new_program
#     except Exception as e:
#         db.session.rollback()
#         print(f"An error occurred while adding the program: {e}")


# def remove_program(self, program_name):
#     try:
#         program = Program.query.filter_by(name=program_name).first()
#         if program:
#             db.session.delete(program)
#             db.session.commit()
#         else:
#             print(f"Program '{program_name}' not found.")
#     except Exception as e:
#         db.session.rollback()
#         print(f"An error occurred while removing the program: {e}")


# def add_course(self, course_code, course_name, credits):
#     try:
#         new_course = Course(code=course_code, name=course_name, credits=credits)
#         db.session.add(new_course)
#         db.session.commit()
#         return new_course
#     except Exception as e:
#         db.session.rollback()
#         print(f"An error occurred while adding the course: {e}")


# def remove_course(self, course_code):
#     try:
#         course = Course.query.filter_by(code=course_code).first()
#         if course:
#             db.session.delete(course)
#             db.session.commit()
#         else:
#             print(f"Course '{course_code}' not found.")
#     except Exception as e:
#         db.session.rollback()
#         print(f"An error occurred while removing the course: {e}")
