from App.database import db

class CoursePlanBuilder(db.Model):
    __abstract__ = True
    builderID = db.Column(db.Integer, primary_key=True)

    def reset(self, studentID):
        raise NotImplementedError("Subclass must implement this method")

    def setSemester(self, semesterID):
        raise NotImplementedError("Subclass must implement this method") 
    
    def setProgram(self, programID):
        raise NotImplementedError("Subclass must implement this method")
    
    def setCourses(self, numCourses):
        raise NotImplementedError("Subclass must implement this method")

    def getPlan(self):
        raise NotImplementedError("Subclass must implement this method")
    