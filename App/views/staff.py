from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user
from flask_login import current_user, login_required
from App.models import Program, ProgramCourses

from.index import index_views

from App.controllers import *

def staff_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not current_user.is_authenticated or not isinstance(current_user, Staff):
            return "Unauthorized", 401
        return func(*args, **kwargs)
    return wrapper

staff_views = Blueprint('staff_views', __name__, template_folder='../templates')


@staff_views.route('/staff/program', methods=['POST'])
@staff_required
def addProgram():
  data=request.json

  program = Program.query.filter_by(programName = data['programName'])
  if program:
    return jsonify(error = 'Program already exists'), 400

  newProgram = create_program(data['departmentCode'], data['programName'], data['coreCredits'], data['electiveCredits'], data['founCredits'])
  if newprogram:
    return jsonify(message = f"Program {newProgram.programName} added"), 201
  else:
     return jsonify(error = "Program creation unsucessful"), 400


@staff_views.route('/program-requirements', methods=['POST'])
@staff_required
def addProgramRequirements():
  data=request.json

  program = Program.query.filter_by(programName = data['programName']).first()
  if not program:
    return jsonify(error = 'Program does not exist'), 400

  #add core courses
  for core in data['coreCourses']:
    check = check_prerequisite_exists(data['programName'], core['course'])
    if check:
      add_program_prerequisites(data['programName'], core['course'], 'core')

  #add elective courses
  for elective in data['electiveCourses']:
    check = check_prerequisite_exists(data['programName'], elective['course'])
    if check:
      add_program_prerequisites(data['programName'], elective['course'], 'elective')

  #add foundation courses
  for foundation in data['foundationCourses']:
    check = check_prerequisite_exists(data['programName'], foundation['course'])
    if check:
      add_program_prerequisites(data['programName'], foundation['course'], 'foundation')
  return jsonify(message = 'Program pre-requisites added successfully'), 200

@staff_views.route('/staff/new-semester', methods=['POST'])
@staff_required
def addSemester():
  data = request.json

  semester = Semester.query.filter_by(year = data['year'], semesterType = data['semesterType'])
  if semester:
    return jsonify(message = 'Semester already exists!'),400

  newSemester = create_semester(data['year'], data['semesterType'])
  if newSemester:
    return jsonify(message = f'Success: {newSemester.__repr__()}'), 200
  return jsonify(error = 'Semester creation unsuccessful'), 400


@staff_views.route('/staff/offered-courses', methods=['GET'])
@staff_required
def getSemesterCourses():
  data = request.json
  listing = get_courses_in_semester(data['year'], data['semesterType']) #get semester courses
  if listing:
    return jsonify(message = f'Offered_courses {listing}'), 200
  return jsonify(error = 'Semester does not exist!'), 400


@staff_views.route('/staff/semester-courses', methods=['POST'])
@staff_required
def addSemesterCourse():
  data=request.json

  course = Course.query.get(data['course']).first()
  if not course:
    return jsonify(error = f'Course {course.courseCode} does not exist'), 400
  
  semester = Semester.query.filter_by(year = data['year'], semesterType = data['semesterType']).first()
  if not semester:
    return  jsonify(error = f'Semester does not exist'), 400

  offeredCourses = get_courses_in_semester(data['year'], data['semesterType'])
  if course in offeredCourses:
    return jsonify(message = f"{courseCode} already exists in the semester's offered courses"), 400

  course = add_semester_course(courseCode, semester.semesterID)
  if course:
     return jsonify(message = f'Added {course.courseCode} successfully'), 200
  return jsonify(error = "Course addition unsucessful"), 400



@staff_views.route('/staff/semester-courses', methods=['DEL'])
@staff_required
def removeSemesterCourse():
  data=request.json

  course = Course.query.get(data['course']).first()
  if not course:
    return jsonify(error = f'Course {course.courseCode} does not exist'), 400

  semester = Semester.query.filter_by(year = data['year'], semesterType = data['semesterType']).first()
  if not semester:
    return  jsonify(error = f'Semester does not exist'), 400

  offeredCourses = get_courses_in_semester(data['year'], data['semesterType'])
  if course in offeredCourses:
    return jsonify(message f"{courseCode} already exists in the semester's offered courses"), 400

  course = remove_semester_course(courseCode, semester.semesterID)
  if course:
     return jsonify(message = f'Deleted {course.courseCode} successfully'), 200
  return jsonify(error = "Course deletion unsucessful"), 400
