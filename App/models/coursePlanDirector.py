from App.database import db
from App.models import *

class CoursePlanDirector(db.Model):
    directorID = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50), nullable = False)
    builderName = db.Column(db.String(50), nullable = False)
    # builderID = db.Column(db.Integer, db.ForeignKey('courseplanbuilder.builderID'), nullable = False)

    def __init__(self, builderName, category):
        self.builderName = builderName
        self.category = category

    def constructMinor(self, builder, semester, program, student):
        builder.reset(student)
        builder.setSemester(semster)
        builder.setProgram(program)
        builder.setCourses(2)
    
    def constructMajor(self, builder, semester, program, student):
        builder.reset(student)
        builder.setSemester(semster)
        builder.setProgram(program)
        builder.setCourses(3)
    
    def constructSpecial(self, builder, semester, program, student):
        builder.reset(student)
        builder.setSemester(semster)
        builder.setProgram(program)
        builder.setCourses(5)
