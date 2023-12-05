from App.database import db
from App.models import *

class EasiestCourses(CoursePlanBuilder):
    easiestCourseID = db.Column(db.Integer, primary_key=True)
    easiestPlan = db.Column(db.Integer,  db.ForeignKey(CoursePlan.planID), nullable=False)
    semesterID = db.Column(db.Integer,  db.ForeignKey(Semester.semesterID))
    programID = db.Column(db.Integer, db.ForeignKey(Program.programID))

    def __init__(self, semesterID, programID):
        self.semesterID = semesterID
        self.programID = programID

    def reset(self, studentID):
        plan = CoursePlan(studentID)
        self.easiestPlan = plan.planID

    def setSemester(self, semesterID):
        plan = CoursePlan.query.get(easiestPlan).first()
        plan.semesterID = semesterID
    
    def setProgram(self, programID):
        plan = CoursePlan.query.get(easiestPlan).first()
        plan.programID = programID
    
    def setCourses(self, numCourses):
        plan = CoursePlan.query.get(easiestPlan).first()

        program = Program.query.get(self.easiestPlan.programID).first()
        semesterCourses = SemesterCourse.query.filter_by(self.easiestPlan.semesterID).all()
        programCourses = ProgramCourse.query.filter_by(programID = self.easiestPlan.programID).all()
        courses = [course for course in programCourses if course in semesterCourses]
        courses.sort(key = sortKey)

        student = Student.query.get(self.easiestPlan.studentID).first()
        easiest = []
        for c in courses:
            found = False
            for sem in student.studentHistory:
                for course in sem.courses:
                    if c.courseCode == course.courseCode:
                        found = True
            if not found: 
                easiest.append(c)

        for x in range(0, min(numCourses, len(easiest)), 1):
            plan.courses.append(easiest[x])

        db.session.add(self.easiestPlan)
        db.session.commit()

    def getPlan(self):
        return self.easiestPlan

    def get_json(self):
        return{
            'Easiest Courses ID': self.easiestCourseID,
            'Semester ID': self.semesterID,
            'Program ID': self.programID
        }
    
    def sortKey(self, courses):
        return courses.difficulty
