from App.database import db
from App.models import Course, CoursePlan

class CoursePlanCourses(db.Model):
    coursePlanCourseID = db.Column(db.Integer, primary_key=True)
    coursePlanID = db.Column(db.Integer, db.ForeignKey('courseplan.planID'))
    courseCode = db.Column(db.Integer, db.ForeignKey('course.courseCode'))
    coursePlan = db.relationship('CoursePlan', backref = 'courses', lazy = True)
    course = db.relationship('Course', backref = 'coursePlans', lazy = True)

    def __init__(self, plan, courseCode):
        self.coursePlanID = plan
        self.courseCode = courseCode
        

    def get_json(self):
        return{
            'Course Plan ID': self.coursePlanID,
            'Course': self.courseCode
        }

