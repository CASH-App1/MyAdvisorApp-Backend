import pytest, unittest
from App.models import Course, Prerequisites
from App.controllers import *
from App.main import create_app
from App.database import db, create_db

class CourseUnitTests(unittest.TestCase):

    def test_new_course(self):
        courseCode = "INFO2605"
        courseName = "Professional Ethics and Law"
        credits = 3
        rating = 4 

        course = Course(courseCode, courseName, rating, credits)

        self.assertEqual(course.courseCode, courseCode)
        self.assertEqual(course.courseName, courseName)
        self.assertEqual(course.credits, credits)
        self.assertEqual(course.rating, rating)

    def test_course_json(self):
        courseCode = "INFO2605"
        courseName = "Professional Ethics and Law"
        credits = 3
        rating = 4 
        
        course = Course(courseCode, courseName, rating, credits)
        course_json = course.get_json()

        self.assertDictEqual(course_json, {
            'Course Code:': courseCode,
            'Course Name: ': courseName,
            'Course Rating: ': rating,
            'No. of Credits: ': credits
            })


    def test_new_prerequisite(self):
        prereq=Prerequisites("INFO2605","Introduction to Information Technology Concepts")
        assert prereq.prereq_courseCode=="INFO2605"

    def test_prerequisite_toJSON(self):
        prereq=Prerequisites("INFO2605","Introduction to Information Technology Concepts")
        prereq_json=prereq.get_json()
        self.assertDictEqual(prereq_json,{
            'prereq_id': None, 
            'prerequisite_courseCode': 'INFO2605', 
            'prerequisite_course': 'Introduction to Information Technology Concepts'
            })
    

@pytest.fixture(autouse=True, scope="module")
def empty_db():
    app = create_app({'TESTING': True, 'SQLALCHEMY_DATABASE_URI': 'sqlite:///test.db'})
    create_db()
    yield app.test_client()
    db.drop_all()

def test_create_course():
    courseCode = "INFO2605"
    courseName = "Professional Ethics and Law"
    credits = 3
    rating = 4 
    prereqs=[]

    course = create_course(courseCode, courseName, rating, credits, prereqs)

    assert get_course_by_courseCode("INFO2605") != None


class CourseIntegrationTests(unittest.TestCase):

    def test_create_course(self):
        course = create_course("COMP1601","Computer Programming I", 3, 3)
        retrieved_course = get_course_by_courseCode(course.code)
        
        self.assertEqual((retrieved_course.code, retrieved_course.courseName, retrieved_course.credits, retrieved_course.difficulty),
                         ("COMP1601", "Computer Programming I", 3, 3)) 