from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from App.models import db
from App.controllers import *

index_views = Blueprint('index_views', __name__, template_folder='../templates')

@index_views.route('/', methods=['GET'])
def index_page():
    return render_template('index.html')

@index_views.route('/init', methods=['GET'])
def init():
    db.drop_all()
    db.create_all()

    with open('Mock Data/Department Data.csv') as file:
        reader = csv.DictReader(file)
        for row in reader:
            newDept = create_department(row['departmentCode'], row['departmentName'])
            if newDept:
                db.session.add(newDept)
    db.session.commit() 

    with open('Mock Data/Staff Data.csv') as file:
        reader = csv.DictReader(file)
        for row in reader:
            newStaff = create_staff(row['staffID'], row['departmentCode'],row['firstName'], row['lastName'], row['email'],row['username'], row['password'])
            if newStaff:
                db.session.add(newStaff)
    db.session.commit() 


    with open('Mock Data/Program Data.csv') as file:
        reader = csv.DictReader(file)
        for row in reader:
            newProgram = create_program(row['departmentCode'],row['programName'], row['coreCredits'], row['electiveCredits'],row['founCredits'])
            if newProgram:
                db.session.add(newProgram)
    db.session.commit() 


    with open('Mock Data/Course Data.csv') as file:
        reader = csv.DictReader(file)
        for row in reader:
            newCourse = create_course(row['courseCode'], row['courseName'], row['credits'], row['difficulty'])
            if newCourse:
                db.session.add(newCourse)
    db.session.commit() 


    with open('Mock Data/Program Requirements Data.csv') as file:
        reader = csv.DictReader(file)
        for row in reader:
            check = check_prerequisite_exists(row['programName'], row['courseCode'])
            if check:
                add_program_prerequisites(row['programName'], row['courseCode'], row['courseType'])
        db.session.commit() 


    with open('Mock Data/Student Data.csv') as file:
        reader = csv.DictReader(file)
        for row in reader:
            newStudent = add_student(row['studentID'], row['firstName'],row['lastName'], row['email'], row['username'],row['password'], row['program1'], row['program2'])
            if newStudent:
                db.session.add(newStudent)
    db.session.commit() 

    return jsonify('database intialized')