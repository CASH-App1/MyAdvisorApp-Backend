from App.models import *
from App.controllers import *
from App.database import db

def create_department(department_code, department_name):
    department = Department.query.get(department_code)
    if department:
        return None

    new_department = Department(departmentCode=department_code, departmentName=department_name)
    db.session.add(new_department)
    db.session.commit()
    return new_department

def get_all_departments():
    return Department.query.all()

def get_department_by_code(department_code):
    return Department.query.get(department_code)
