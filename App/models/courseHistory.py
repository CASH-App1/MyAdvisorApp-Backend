from App.database import db
from App.models import *

class CourseHistory(db.Model):
    courseHistoryID = db.Column(db.Integer, primary_key=True)
    courseCode = db.Column(db.String(50), db.ForeignKey('course.courseCode'))
    semesterID = db.Column(db.Integer, db.ForeignKey(SemesterHistory.historyID))
    gradeLetter = db.Column(db.String(2), nullable = False)
    percent = db.Column(db.Float, nullable= False)
    courseType = db.Column(db.String(50), nullable = False)

    def __init__(self, courseCode, gradeLetter, percent, courseType, semID):
        self.courseCode = courseCode
        self.gradeLetter = gradeLetter
        self.percent = percent
        self.courseType = courseType
        self.semesterID = semID
        self.courseType = courseType
    

    def get_json(self):
        return{
            'Course History ID': self.courseHistoryID,
            'Course Code': self.courseCode,
            'Course Grade': self.gradeLetter,
            'Percentage' : self.percent,
            'Course Type': self.courseType,
            'Semester ID': self.semesterID
        }
