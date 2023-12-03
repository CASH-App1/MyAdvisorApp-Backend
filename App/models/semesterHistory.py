from App.database import db
from App.models import Student

class SemesterHistory(db.Model):
    historyID = db.Column(db.Integer, primary_key=True)
    studentID = db.Column(db.ForeignKey('student.studentID'))
    year = db.Column(db.Integer, nullable = False)
    semeterType = db.Column(db.Integer, nullable= False)
    courses = db.relationship('CourseHistory', backref = 'semesterHistory', lazy = True)

    def __init__(self, id, year, semesterType):
        self.studentID = id
        self.year = year
        self.semesterType = semesterType
    
    def get_json(self):
        courseInfo = []
        for c in self.courses:
            courseInfo.append(c.get_json())

        return{
            'Student ID': self.studentID, #is this suppose to be id or program_id alone 
            'Semester Date': f'{self.year} - Semester {self.semesterType}',
            'Courses': courseInfo
        }