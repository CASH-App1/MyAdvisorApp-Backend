import unittest, pytest
from App.main import create_app
from App.database import db, create_db
from App.models import Staff
from App.controllers import create_staff, get_staff_by_id, update_staff
from werkzeug.security import generate_password_hash

'''
Staff Unit Tests 
'''

class StaffUnitTests(unittest.TestCase):

    def test_new_staff(self):
        #newUser = User()
        newStaff = Staff(101, "DCIT", "Bobby", "Smith", "bob@mail.com", "bob", "bobpass")
        assert (newStaff.staffID, newStaff.departmentCode, newStaff.firstName,  newStaff.lastName, newStaff.email, newStaff.username) == (101, "DCIT", "Bobby", "Smith", "bob@mail.com", "bob")

    # pure function no side effects or integrations called
    def test_staff_toJSON(self):
        newStaff = Staff(101, "DCIT", "Bobby", "Smith", "bob@mail.com", "bob", "bobpass")
        self.assertDictEqual(newStaff.get_json(), {"Staff ID":101, "First Name":"Bobby", "Last Name":"Smith", "Email":"bob@mail.com", "Department Code":"DCIT", "Username":"bob"})
    

    def test_hashed_password(self):
        password = "pass123"
        hashed = generate_password_hash(password, method='sha256')
        newStaff = Staff(101, "DCIT", "Bobby", "Smith", "bob@mail.com", "bob", "bobpass")
        assert newStaff.password != password

    def test_check_password(self):
        password = "pass123"
        newStaff = Staff(101, "DCIT", "Bobby", "Smith", "bob@mail.com", "bob", password)
        assert newStaff.check_password(password) 

'''
Staff Integration Tests
'''

@pytest.fixture(autouse=True, scope="module")
def empty_db():
    app = create_app({'TESTING': True, 'SQLALCHEMY_DATABASE_URI': 'sqlite:///test.db'})
    create_db()
    yield app.test_client()
    db.drop_all()

class StaffIntegrationTests(unittest.TestCase):

    # def test_create_staff(self):
    #     staff = create_staff(101, "CLL", "Jane", "Austin", "jane101@mail.com", "jane", "janepass")
    #     retrieved_staff = get_staff_by_id(staff.staffID)
        
    #     self.assertEqual((retrieved_staff.departmentCode, retrieved_staff.firstName, retrieved_staff.lastName, 
    #                     retrieved_staff.email, retrieved_staff.username),
    #                      ("CLL", "Jane", "Austin", "jane101@mail.com", "jane"))

    # def test_create_staff(self):
    #     # Arrange
    #     staff_id = 101
    #     department_code = "CLL"
    #     first_name = "Jane"
    #     last_name = "Austin"
    #     email = "jane101@mail.com"
    #     username = "jane"
    #     password = "janepass"

    #     # Act
    #     staff = create_staff(
    #         staff_id=staff_id,
    #         department_code=department_code,
    #         first_name=first_name,
    #         last_name=last_name,
    #         email=email,
    #         username=username,
    #         password=password,
    #     )

    #     # Assert
    #     assert staff is not None, "Staff creation failed"

    #     # Check if staff attributes match the expected values
    #     assert (
    #         staff.departmentCode,
    #         staff.firstName,
    #         staff.lastName,
    #         staff.email,
    #         staff.username,
    #     ) == (department_code, first_name, last_name, email, username), "Staff attributes do not match"

    #     # Additional check by retrieving the staff from the database
    #     retrieved_staff = get_staff_by_id(staff.staffID)

    #     # Assert the retrieved staff has the same attributes
    #     assert (
    #         retrieved_staff.departmentCode,
    #         retrieved_staff.firstName,
    #         retrieved_staff.lastName,
    #         retrieved_staff.email,
    #         retrieved_staff.username,
    #     ) == (department_code, first_name, last_name, email, username), "Retrieved staff attributes do not match"

    def test_create_staff(self):
        # Arrange
        staff_id = 101
        department_code = "CLL"
        first_name = "Jane"
        last_name = "Austin"
        email = "jane101@mail.com"
        username = "jane"
        password = "janepass"

        try:
            # Act
            staff = create_staff(
                staff_id=staff_id,
                department_code=department_code,
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password=password,
            )

            # Assert
            assert staff is not None, "Staff creation failed"

        except Exception as e:
            print(f"Exception during staff creation: {e}")
            raise  # Re-raise the exception to fail the test

        # Additional check if needed
        retrieved_staff = get_staff_by_id(staff.staffID)
        assert (retrieved_staff.departmentCode, retrieved_staff.firstName, retrieved_staff.lastName,
                retrieved_staff.email, retrieved_staff.username) == (
                "CLL", "Jane", "Austin", "jane101@mail.com", "jane")

    def test_update_staff(self):
        staff = create_staff(101, "CLL", "Jane", "Austin", "jane101@mail.com", "jane", "janepass")
        updated_staff = update_staff(staff.staff_id, "DCIT", "Janice", "Dottin", "janice@example.com", "jan_dot", "newjanepass")
        retrieved_staff = get_staff_by_id(updated_staff.staff_id)

        assert(retrieved_staff.department_code, retrieved_staff.first_name, retrieved_staff.last_name, retrieved_staff.email, retrieved_staff.username) == flask("DCIT", "Janice", "Dottin", "janice@example.com", "jan_dot")

