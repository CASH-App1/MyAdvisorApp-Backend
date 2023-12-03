from App.database import db
from App.models import SemesterHistory, Course

class CourseHistory(db.Model):
    courseHistoryID = db.Column(db.Integer, primary_key=True)
    courseCode = db.Column(db.String(50), db.ForeignKey('course.courseCode'))
    semesterID = db.Column(db.Integer, db.ForeignKey('semesterhistory.historyID'))
    gradeLetter = db.Column(db.String(2), nullable = False)
    percent = db.Column(db.Float, nullable= False)
    courseType = db.Column(db.String(50), nullable = False)

    def __init__(self, id, courseCode, gradeLetter, percent, courseType, semID):
        self.courseHistoryID = id
        self.courseCode = courseCode
        self.gradeLetter = gradeLetter
        self.percent = percent
        self.semesterID = semID
    

    def get_json(self):
        return{
            'CourseHistory ID': self.courseHistoryID,
            'Course Code': self.courseCode,
            'Course Grade': f'{self.gradeLetter} : {self.percent}',
            'Course Type': self.courseType
        }
