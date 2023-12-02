from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user
from flask_login import login_required, login_user, current_user, logout_user

from.index import index_views

from App.controllers import (
    create_user,
    jwt_authenticate,
    login,
    get_all_users
)

auth_views = Blueprint('auth_views', __name__, template_folder='../templates')

'''
Page/Action Routes
'''

@auth_views.route('/login', methods=['POST'])
def login_action():
    data = request.json
    user = login(data['username'], data['password'])
    if user:
        staff = Staff.query.filter_by(data['username']).first()
        if staff:
            return jsonify({"Staff token":jwt_authenticate(data['username'],data['password'])}), 200
        return jsonify({"Student token":jwt_authenticate(data['username'],data['password'])}), 200

    return jsonify({"error":"invalid credentials"}), 401


@app.route('/signup-student', methods=['POST'])
def signup_student():
    data = request.json
    
    student = Student.query.filter_by(username = data['username'])
    staff = Staff.query.filter_by(username = data['username'])
    if staff or student:
        return jsonify(message='username already taken!'), 401

    newStudent = Student(id = data['studentID'], firstName = data['firstName'], lastName = data['lastName'], email = data['email'], username = data['username'], password = data['password']) 
    program = Program.query.filter_by(programName = data['program1'])
    if not program:
        return jsonify(error= f'The degree program {data['program1']} does not exist'), 401
    newStudent.programs.append(program)

    if data['program2']:
    program = Program.query.filter_by(programName = data['program2'])
        if not program:
            return jsonify(error= f'The degree program {data['program1']} does not exist'), 401
        newStudent.programs.append(program)

    db.session.add(newStudent)
    db.session.commit()
    return jsonify(message=f'Student {newStudent.studentID} - {newStudent.username} created!'), 201


