import os, tempfile, pytest, logging, unittest

from App.models import Department
from App.main import create_app
from App.database import db, create_db


class DepartmentUnitTests(unittest.TestCase):

    def test_new_department(self):
        newDepartment = Department("DCIT", "Department of Computing and Information Technology")
        assert(newDepartment.departmentCode, newDepartment.departmentName) == ("DCIT", "Department of Computing and Information Technology")

    def test_department_toDict(self):
        newDepartment = Department("DCIT", "Department of Computing and Information Technology")
        assert(newDepartment.toDict(), {"Department Code":"DCIT", "Department Name":"Department of Computing and Information Technology"})
