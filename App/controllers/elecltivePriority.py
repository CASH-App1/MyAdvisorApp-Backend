from App.models import ElectivePriority, CoursePlan, Program, SemesterCourse, Student
from App.database import db


    def create_elective_priority_plan(student_id):
        elective_priority = ElectivePriority(student_id)
        return elective_priority

    
    def update_elective_priority_plan(elective_priority, semester_id, program_id, num_courses):
        elective_priority.reset(student_id)
        elective_priority.set_semester(semester_id)
        elective_priority.set_program(program_id)
        elective_priority.set_courses(num_courses)

 
    def get_elective_priority_plan(elective_priority):
        return elective_priority.get_plan()


   
    def get_elective_priority_plan_json(elective_priority):
        return elective_priority.get_json()

   
   
