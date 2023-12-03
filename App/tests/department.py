import os, tempfile, pytest, logging, unittest

from App.models import Department
from App.main import create_app
from App.database import db, create_db


class DepartmentUnitTests(unittest.TestCase):

    def test_new_department(self):
        newDepartment = Department("DCIT", "Department of Computing and Information Technology")
        assert(newDepartment.departmentCode, newDepartment.departmentName) == ("DCIT", "Department of Computing and Information Technology")

    def test_department_toJSON(self):
        newDepartment = Department("DCIT", "Department of Computing and Information Technology")
        assert(newDepartment.get_json(), {"Department Code":"DCIT", "Department Name":"Department of Computing and Information Technology"})

"Integration Tests"
class DepartmentIntegrationTests(unittest.TestCase):
    def test_create_department(self):
        department_code = 'DCIT'
        department_name = 'Department of Computing and Technology'
        created_department = create_department(department_code, department_name)

        self.assertIsNotNone(created_department)
        retrieved_department = get_department_by_code(department_code)
        self.assertEqual(retrieved_department, created_department)
