from App.database import db

class CoursePlanDirector(db.Model):
    directorID = db.Column(db.Integer, primary_key=True)
    # builderID = db.Column(db.Integer, db.ForeignKey('courseplanbuilder.builderID'), nullable = False)

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
