from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user
from flask_login import login_required, login_user, current_user, logout_user

from.index import index_views

from App.controllers import *

auth_views = Blueprint('auth_views', __name__, template_folder='../templates')

'''
Page/Action Routes
'''

@auth_views.route('/staff-login', methods=['POST'])
def stafflogin_action():
    data = request.json
    user = staff_login(data['username'], data['password'])
    if user:
        token = jwt_authenticate(data['username'],data['password'])
        return jsonify(staff_token = token), 200
    return jsonify(error = "Unauthorized. Invalid Credentials"), 401


@auth_views.route('/student-login', methods=['POST'])
def studentlogin_action():
    data = request.json
    user = student_login(data['username'], data['password'])
    if user:
      print("hello")
    if user:
        token = jwt_authenticate(data['username'],data['password'])
        return jsonify(student_token = token), 200
    return jsonify(error = "Unauthorized. Invalid Credentials"), 401


@auth_views.route('/signup-student', methods=['POST'])
def signup_student():
    data = request.json
    user = User.query.filter_by(username = data['username']).first()
    if user:
      print(user.get_json())
      return jsonify(error='username already taken!'), 401

    program = Program.query.filter_by(programName = data['program1']).first()
    if not program:
        return jsonify(error= f"The degree program {data['program1']} does not exist"), 401

    if data['program2']:
        program = Program.query.filter_by(programName = data['program2']).first()
        if not program:
            return jsonify(error= f"The degree program {data['program2']} does not exist"), 401

    newStudent = add_student(data['studentID'], data['firstName'], data['lastName'], data['email'], data['username'],data['password'], data['program1'], data['program2']) 
    db.session.add(newStudent)
    db.session.commit()
    return jsonify(message=f'Student {newStudent.studentID} - {newStudent.username} created!'), 201


