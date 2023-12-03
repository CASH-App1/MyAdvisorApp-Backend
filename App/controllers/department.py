from App.models import Department
from App.database import db

def create_department(department_code, department_name):
    department = Department.query.get(department_code).first()
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

"Integration Tests"
 def test_create_department(self):
        department_code = 'DCIT'
        department_name = 'Department of Computing and Technology'
        created_department = create_department(department_code, department_name)

        self.assertIsNotNone(created_department)
        retrieved_department = get_department_by_code(department_code)
        self.assertEqual(retrieved_department, created_department)
