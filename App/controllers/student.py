from App.models import *
from App.controllers import *
from App.database import db

def verify_student(username):
  student=Student.query.get(username)
  if student:
      return True
  return False

# Controller to add a new student
def add_student(studentID, first_name, last_name, email, username, password, program1, program2):
    user = User.query.filter_by(username = username).first()
    if not user:
        new_student = Student(studentID, first_name,last_name,email, username, password)
        program = Program.query.filter_by(programName =program1).first()
        if program:
            new_student.programs.append(program)

            program = Program.query.filter_by(programName = program2).first()
            if program:
              new_student.programs.append(program)
            
            db.session.add(new_student)
            db.session.commit()
            return new_student
    return None

# Controller to get a student by username (student_id)
def get_student(studentID):
    student = Student.query.get(studentID).first()
    if student:
        return student
    return None

# Controller to get a list of all students
def get_all_students():
    students = Student.query.all()
    student_data = [{'studentID': student.studentID, 'firstName': student.firstName, 'lastName': student.lastName, 'email': student.email} for student in students]
    return student_data

  
# Controller to update a student
def update_student(studentID, new_first_name, new_last_name, new_email, new_username, new_password):
    student = Student.query.get(studentID)
    if student:
        student.firstName = new_first_name
        student.lastName = new_last_name
        student.email = new_email
        student.username = new_username
        student.password = new_password
        db.session.add(student)
        db.session.commit()
        return student
    return None



def create_semester_history(student_id, year, semester_type):
    new_semester_history = SemesterHistory(student_id=student_id, year=year, semester_type=semester_type)
    db.session.add(new_semester_history)
    db.session.commit()
    return new_semester_history


def get_student_history(student):
    history = student.studentHistory

    studentHist = []
    for h in history:
        studentHist.append(h.get_json())
    
    return studentHist


def get_student_plans(student):
    plans = student.coursePlans

    studentPlans = []
    for p in plans:
       studentPlans.append(p.get_json())


def addCoursetoHistory(studentid, semesterHistory, courseCode, gradeLetter, percent, courseType, semesterID):
    courseHist = CourseHistory(courseCode, gradeLetter, percent, courseType, semesterID)
    if courseHist not in semesterHistory.courses:
        db.session.add(courseHist)
        semesterHistory.courses.append(courseHist)   


def updateStudentHistory(student, year, semesterType, histories):
    semesterHist = create_semester_history(student.studentID, year, semesterType)
    if semesterHist:
        for hist in histories:
            courseHist = addCoursetoHistory(semesterHist, hist['courseCode'], hist['gradeLetter'], hist['percent'], hist['courseType'], semesterHist.historyID)

        
        student.studentHistory.append(semesterHist)
        db.session.add(semesterHist)
        db.session.commit()
        return True
    return False