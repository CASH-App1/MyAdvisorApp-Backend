from App.models import FastestGraduation, CoursePlan, Program, SemesterCourse, Student
from App.database import db


    
    def create_fastest_graduation_plan(student_id):
        fastest_graduation = FastestGraduation(student_id)
        db.session.add(fastest_graduation)
        db.session.commit()
        return fastest_graduation

    
    def update_fastest_graduation_plan(fastest_graduation, semester_id, program_id, num_courses):
        fastest_graduation.reset(student_id)
        fastest_graduation.set_semester(semester_id)
        fastest_graduation.set_program(program_id)
        fastest_graduation.set_courses(num_courses)
        db.session.commit()

    
    def get_fastest_graduation_plan(fastest_graduation):
        return fastest_graduation.get_plan()

    
    def get_fastest_graduation_plan_json(fastest_graduation):
        return fastest_graduation.get_json()
