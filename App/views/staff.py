from flask import Blueprint,jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from functools import wraps
from App.models import *
from.index import index_views
from App.controllers import *


staff_views = Blueprint('staff_views', __name__, template_folder='../templates')


@staff_views.route('/staff/program', methods=['POST'])
@jwt_required()
def addProgram():
  data = request.json
  username = get_jwt_identity()
  
  if not verify_staff(username):
    return jsonify(error = 'You are unauthorized to perform this action. Please login with Staff credentials.'), 401

  program = Program.query.filter_by(programName = data['programName']).first()
  
  if program:
    return jsonify(error = 'Program already exists'), 400

  newProgram = create_program(data['departmentCode'], data['programName'], data['coreCredits'], data['electiveCredits'], data['founCredits'])
  print(newProgram)
  if newProgram:
    return jsonify(message = f"Program {newProgram.programName} added"), 201
  else:
     return jsonify(error = "Program creation unsucessful"), 400


@staff_views.route('/program-requirements', methods=['POST'])
@jwt_required()
def addProgramRequirements():
  data=request.json
  username = get_jwt_identity()
  
  if not verify_staff(username):
    return jsonify(error = 'You are unauthorized to perform this action. Please login with Staff credentials.'), 401

  program = Program.query.filter_by(programName = data['programName']).first()
  if not program:
    return jsonify(error = 'Program does not exist'), 400

  prereqs = "Program prerequisites : "

  #add core courses
  for core in data['coreCourses']:
    check = check_prerequisite_exists(data['programName'], core['course'])
    if not check:
      add_program_prerequisites(data['programName'], core['course'], 'core')
      prereqs += f"{core['course']} "

  #add elective courses
  for elective in data['electiveCourses']:
    check = check_prerequisite_exists(data['programName'], elective['course'])
    if not check:
      add_program_prerequisites(data['programName'], elective['course'], 'elective')
      prereqs += f"{elective['course']} "

  #add foundation courses
  for foundation in data['foundationCourses']:
    check = check_prerequisite_exists(data['programName'], foundation['course'])
    if not check:
      add_program_prerequisites(data['programName'], foundation['course'], 'foundation')
      prereqs += f"{foundation['course']} "
      
  return jsonify(message = f'{prereqs} added successfully'), 200

@staff_views.route('/staff/new-semester', methods=['POST'])
@jwt_required()
def addSemester():
  data = request.json
  username = get_jwt_identity()
  if not verify_staff(username):
    return jsonify(error = 'You are unauthorized to perform this action. Please login with Staff credentials.'), 401

  semester = Semester.query.filter_by(year = data['year'], semesterType = data['semesterType']).first()
  if semester:
    return jsonify(message = 'Semester already exists!'),400

  newSemester = create_semester(data['year'], data['semesterType'])
  if newSemester:
    return jsonify(message = f'Success: {newSemester.__repr__()}'), 200
  return jsonify(error = 'Semester creation unsuccessful'), 400


@staff_views.route('/staff/offered-courses', methods=['GET'])
@jwt_required()
def getSemesterCourses():
  data = request.json
  username = get_jwt_identity()
  if not verify_staff(username):
    return jsonify(error = 'You are unauthorized to perform this action. Please login with Staff credentials.'), 401

  semester = Semester.query.filter_by(year=data['year'], semesterType=data['semesterType']).first()
  if semester:
    listing = get_courses_in_semester(data['year'], data['semesterType'])
    
    if len(listing) == 0:
      return jsonify(message = 'There are no offered courses this semester'), 200
      
    if listing:
      courses = [l.get_json() for l in listing]
      return jsonify(message = f'Offered courses: {listing}'), 200
  return jsonify(error = 'Semester does not exist!'), 400


@staff_views.route('/staff/semester-courses', methods=['POST'])
@jwt_required()
def addSemesterCourse():
  data=request.json
  username = get_jwt_identity()
  if not verify_staff(username):
    return jsonify(error = 'You are unauthorized to perform this action. Please login with Staff credentials.'), 401

  for c in data['courses']:
    course = Course.query.get(c['course'])
    if not course:
      return jsonify(error = f"Course {data['course']} does not exist"), 400
    
    semester = Semester.query.filter_by(year = data['year'], semesterType = data['semesterType']).first()
    if not semester:
      return  jsonify(error = f'Semester does not exist'), 400

    added = add_semester_course(course.courseCode, semester.semesterID)
    if not added:
      return jsonify(error = "Course addition unsucessful"), 400
  
  return jsonify(message = f"Added courses successfully"), 200



@staff_views.route('/staff/semester-courses', methods=['DELETE'])
@jwt_required()
def removeSemesterCourse():
  data=request.json
  username = get_jwt_identity()
  if not verify_staff(username):
    return jsonify(error = 'You are unauthorized to perform this action. Please login with Staff credentials.'), 401

  course = Course.query.get(data['course'])
  if not course:
    return jsonify(error = f"Course {data['course']} does not exist"), 400

  semester = Semester.query.filter_by(year = data['year'], semesterType = data['semesterType']).first()
  if not semester:
    return  jsonify(error = f'Semester does not exist'), 400

  offeredCourses = get_courses_in_semester(data['year'], data['semesterType'])
  if course in offeredCourses:
    course = remove_semester_course(data['course'], semester.semesterID)
    if course:
       return jsonify(message = f"Deleted {data['course']} successfully"), 200
    return jsonify(error = "Course deletion unsucessful"), 400
  