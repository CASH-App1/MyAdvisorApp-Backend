from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from.index import index_views

from App.controllers import *


student_views = Blueprint('student_views', __name__, template_folder='../templates')

@student_views.route('/student/autogenerated-plan', methods=['POST'])
@jwt_required()
def autogenerate_course_plan():
    data = request.json
  
    username = get_jwt_identity()
    print(username)
  
    if not verify_student(username):
      return jsonify(error = 'You are unauthorized to perform this action. Please login with Student credentials.'), 401

    student = Student.query.get(username)
    valid_plans = ["Elective Priority", "Easiest Courses", "Fastest Graduation"]
    valid_degree_types = ['Major', 'Minor', 'Special']

    if data['planType'] in valid_plans and data['degreeType'] in valid_degree_types:
        semester =  get_upcoming_semester()
        plan = autogenerator(student, data['planType'], data['degreeType'], data['programID'], semester.semesterID)
        if plan:
            return jsonify(message = f"{command} plan created & added to student plans! \n {student.firstName} {student.lastName} - {data['planType']} \n Course Plan {plan.get_json()}"), 201
            
    return jsonify(error = 'Invalid plan type'), 401


@student_views.route('/student/course-plan', methods=['POST'])
@jwt_required()
def add_course_to_plan():
    data = request.json
    username = get_jwt_identity()
    if not verify_student(username):
      return jsonify(error = 'You are unauthorized to perform this action. Please login with Student credentials.'), 401

    student = Student.query.get(username)

    semester = Semester.query.order_by(SemesterHistory.historyID.desc()).first()
    if data['year']  != semester.year and data['semesterType'] != semseter.semesterType:
        return jsonify(error = f'Invalid semester entered'), 400

    if data['planID'] == 0:
        plan = create_course_plan(student.studentID)

    if data['planID'] != 0:
        plan = get_course_plan(data['planID'])
        if not plan:
            return jsonify(error = f'Course Plan does not exist'), 400

    course = get_course_by_courseCode(data['course'])
    if not course:
        return jsonify(error = f"Course {data['course'].courseCode} does not exist"), 400 

    if course in plan.courses:
        return jsonify(message = 'Course already exists in plan'), 200
                     
    if check_prerequisites(course, student):
        added = add_course_to_plan(course, plan)
        if added:
            return jsonify(message = 'Course(s) added successfully'), 200
    return jsonify(error = f"The pre-requisites for {course.courseCode} have not been met!"), 400
    
    
@student_views.route('/student/course-plan', methods=['DELETE'])
@jwt_required()
def remove_course_from_plan():
    data = request.json
    username = get_jwt_identity()
    if not verify_student(username):
      return jsonify(error = 'You are unauthorized to perform this action. Please login with Student credentials.'), 401 
 
    student = Student.query.get(username)

    semester = Semester.query.order_by(SemesterHistory.historyID.desc()).first()
    if data['year']  != semester.year and data['semesterType'] != semseter.semesterType:
        return jsonify(error = f'Invalid semester entered'), 400

    if data['planID'] != 0:
        plan = get_course_plan(data['planID'])
        if not plan:
            return jsonify(error = f'Course Plan does not exist'), 400

    course = get_course_by_courseCode(data['course'])
    if not course:
        return jsonify(error = f"Course {data['course'].courseCode} does not exist"), 400 

    if course not in plan.courses:
        return jsonify(message = 'Course does not exist in plan'), 200
    
    removed = remove_course_to_plan(course, plan)
    if removed:
        return jsonify(message = f'Course {course.courseCode} removed successfully'), 200
    return jsonify(error = f'Course {course.courseCode} removal was unsuccessful!'), 400
    


@student_views.route('/student/course-plans', methods=['GET'])
@jwt_required()
def view_course_plans():
    username = get_jwt_identity()
    if not verify_student(username):
      return jsonify(error = 'You are unauthorized to perform this action. Please login with Student credentials.'), 401
      
    student = Student.query.get(username)
    coursePlans = get_student_plans(student)

    if coursePlans:
        return jsonify(message = f'Student {student.firstName} {student.lastName} Course Plans: {coursePlans}'), 200
    return jsonify(error = f'Student {student.firstName} {student.lastName} has no created course plans.'), 200



@student_views.route('/student/academic-history', methods=['POST'])
@jwt_required()
def update_academic_history():
    data = request.json
    username = get_jwt_identity()
    if not verify_student(username):
      return jsonify(error = 'You are unauthorized to perform this action. Please login with Student credentials.'), 401
    print(username)
    semester = get_upcoming_semester()
    if data['year']  >= semester.year and data['semesterType'] >= semseter.semesterType:
        return jsonify(error = f'Invalid semester entered'), 400

    semesterHist = SemesterHistory.query.filter_by(year = data['year'], semesterType = data['semesterType']).first()
    if semesterHist:
        return jsonify(error = f"Semester {data['semesterType']} - {data['year']} already exists!"), 200
    
    student = Student.query.get(username)
    print(student)
    updatedHistory = updateStudentHistory(student, data['year'],  data['semesterType'],  data['histories'])
    if updatedHistory:
        return jsonify(message = 'Semester History addition successful'), 200
    return jsonify(error = 'Semester History addition unsuccessful'), 400


@student_views.route('/student/academic-history', methods=['GET'])
@jwt_required()
def view_academic_history():
    username = get_jwt_identity()
    if not verify_student(username):
      return jsonify(error = 'You are unauthorized to perform this action. Please login with Student credentials.'), 401
      
    student = Student.query.get(username)
    history = get_student_history(student)

    if history:
        return jsonify(message = f'{student.firstName} {student.lastName} Academic History: \n {history}'), 200
    return jsonify(error = f'There is no academic history for {student.firstName} {student.lastName}'), 200
    
