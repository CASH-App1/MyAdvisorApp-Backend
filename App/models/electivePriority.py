from App.database import db
from App.models import CoursePlanBuilder

class ElectivePriority(CoursePlanBuilder):
    electivePlanID = db.Column(db.Integer, primary_key=True),
    electivePlan = db.Column(db.Integer,  db.ForeignKey('courseplan.planID'), nullable=False),

    def __init__(self, studentID):
        self.reset(studentID)

    def reset(self, studentID):
        plan = CoursePlan(studentID)
        self.electivePlan = plan.planID

    def setSemester(self, semesterID):
        plan = CoursePlan.query.get(electivePlan).first()
        plan.semesterID = semesterID
    
    def setProgram(self, programID):
        plan = CoursePlan.query.get(electivePlan).first()
        plan.programID = programID
    
    def setCourses(self, numCourses):
        plan = CoursePlan.query.get(electivePlan).first()
        program = Program.query.get(self.electivePlan.programID).first()
        semesterCourses = SemesterCourse.query.filter_by(semesterID = self.electivePlan.semesterID).all()
        courses = [course for course in program.electiveCourses if course in semesterCourses]

        student = Student.query.get(self.easiestPlan.studentID).first()
        electives = []

        for c in courses:
            found = False
            for sem in student.studentHistory:
                for course in sem.courses:
                    if c.courseCode == course.courseCode:
                        found = True
            if not found: 
                electives.append(c)

        for x in range(0, min(numCourses, len(easiest)), 1):
            plan.courses.append(electives[x])
        
        db.session.add(self.electivePlan)
        db.session.commit()

    def getPlan(self):
        return self.electivePlan

    def get_json(self):
        return{
            'Degree Plan ID': self.electivePlanID,
            'Plan': self.electivePlan
        }
    
