from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from App.models import db
from App.controllers import (create_course, create_staff,createCoursesfromFile)

index_views = Blueprint('index_views', __name__, template_folder='../templates')


@index_views.route('/init', methods=['GET'])
def init():
    db.drop_all()
    db.create_all()

    with open('Mock Data/Department Data.csv') as file:
        reader = csv.DictReader(file)
        for row in reader:
            newDept = Department(departmentCode =row['departmentCode'], departmentName = row['departmentName'])
            db.session.add(newDept)
    db.session.commit() 

    with open('Mock Data/Staff Data.csv') as file:
        reader = csv.DictReader(file)
        for row in reader:
            newStaff = new_staff(staffID = row['staffID'], departmentCode = row['departmentCode'], firstName = row['firstName'], lastName = row['lastName'], email = row['email'], username = row['username'], password = row['password'])
            if newStaff:
                db.session.add(newStaff)
    db.session.commit() 


    with open('Mock Data/Program Data.csv') as file:
        reader = csv.DictReader(file)
        for row in reader:
            newProgram = Program(department_code = row['departmentCode'], program_name = row['programName'], core_credits = row['coreCredits'], elective_credits = row['electiveCredits'], foun_credits = row['founCredits'])
            department = Department.query.get(row['departmentCode']).first()
            department.programs.append(newProgram)
            db.session.add(newProgram)
    db.session.commit() 

    with open('Mock Data/Course Data.csv') as file:
        reader = csv.DictReader(file)
        for row in reader:
            prereq = Prerequisite(row['courseCode'])
            newCourse = Course(courseCode = row['courseCode'], prereqID = prereq.prereqID, courseName = row['courseName'], credits = row['credits'], difficulty = row['difficulty'])
            db.session.add(newCourse)
    db.session.commit() 

    with open('Mock Data/Program Requirements Data.csv') as file:
        reader = csv.DictReader(file)
        for row in reader:
            program = Program.query.filter_by(programName = row['programName'])
            program.add_course(row['courseCode'], row['courseType'])
    db.session.commit() 


    with open('Mock Data/Student Data.csv') as file:
        reader = csv.DictReader(file)
        for row in reader:
            newStudent = add_student(id = row['studentID'], firstName = row['firstName'], lastName = row['lastName'], email = row['email'], username = row['username'], password = row['password'], program1 = row['program1'], program2 = row['program2'])
            if newStudent:
                db.session.add(newStudent)
    db.session.commit() 

    return jsonify({'database intialized'})
