from App.models import Department
from App.database import db

def create_department(department_code, department_name):
    new_department = Department(departmentCode=department_code, departmentName=department_name)
    db.session.add(new_department)
    print("Department successfully created")
    db.session.commit()
    return new_department

def get_all_departments():
    return Department.query.all()

def list_departments_alphabetically():
    departments = Department.query.order_by(Department.departmentName).all()
    return departments
