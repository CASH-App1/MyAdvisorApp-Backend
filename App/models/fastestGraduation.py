from App.database import db
from App.models import CoursePlanBuilder

class FastestGraduation(CoursePlanBuilder):
    fastestGraduationID = db.Column(db.Integer, primary_key=True),
    fastestPlan = db.Column(db.Integer,  db.ForeignKey('courseplan.planID'), nullable=False),

    def __init__(self, studentID):
        self.reset(studentID)

    def reset(self, studentID):
        plan = CoursePlan(studentID)
        self.fastestPlan = plan.planID

    def setSemester(self, semesterID):
        plan = CoursePlan.query.get(fastestPlan).first()
        plan.semesterID = semesterID
    
    def setProgram(self, programID):
        plan = CoursePlan.query.get(fastestPlan).first()
        plan.programID = programID
    
    def setCourses(self, numCourses):
        plan = CoursePlan.query.get(fastestPlan).first()
        program = Program.query.get(self.fastestPlan.programID).first()
        semesterCourses = SemesterCourse.query.filter_by(semesterID = self.fastestPlan.semesterID).all()
        programCourses = ProgramCourse.query.filter_by(programID = self.fastestPlan.programID).all()
        courses = [course for course in programCourses if course in semesterCourses]

        student = Student.query.get(self.fastestPlan.studentID).first()
        core = []
        foundation = []
        elective = []
        for c in courses:
            found = False
            for sem in student.studentHistory:
                for course in sem.courses:
                    if c.courseCode == course.courseCode:
                        found = True

            if not found: 
                if c in program.coreCourses:
                    core.append(c)
                if c in program.founCourses:
                    foundation.append(c)
                if c in program.electiveCourses:
                    elective.append(c)

        #add foundation courses
        increment = 0
        while numCourses >= 0 and len(foundation - 1) >= increment:
            plan.courses.append(foundation[increment])
            increment += 1
            numCourses -=1
        
        #add core courses
        increment = 0
        while numCourses >= 0 and len(core) - 1 >= increment:
            plan.courses.append(core[increment])
            increment += 1
            numCourses -=1

        # add elective courses
        increment = 0
        while numCourses >= 0 and len(elective) - 1 >= increment:
            plan.courses.append(elective[increment])
            increment += 1
            numCourses -=1
        
        db.session.add(self.fastestPlan)
        db.session.commit()

    def getPlan(self):
        return self.fastestPlan
        
    def get_json(self):
        return{
            'Degree Plan ID': self.fastestGraduationID,
            'Plan': self.fastestPlan
        }