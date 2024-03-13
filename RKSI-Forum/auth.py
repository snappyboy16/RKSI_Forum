from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import Student
from . import db

auth = Blueprint('profile', __name__)


@auth.route('/profile')
def profile():
    return render_template('profile.html', url='profile')


@auth.route('/login')
def login():
    login_user(Student)
    return render_template('auth.html', url='login')


@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')

    student = Student.query.filter_by(email=email).first()

    if not student or not check_password_hash(student.password, password):
        flash('Пожалуйста, проверьте свои данные для входа и повторите попытку.')
        return redirect(url_for('auth.login'))

    return redirect(url_for('main.profile'))


@auth.route('/signup')
def signup():
    return render_template('reg.html', url='signup')


@auth.route('/signup', methods=['POST'])
def signup_post():
    nickname = request.form.get('nickname')
    name = request.form.get('name')
    group = request.form.get('group')
    email = request.form.get('email')
    password = request.form.get('password')

    student = Student.query.filter_by(email=email).first()

    if student:
        flash('Адрес электронной почты уже существует')
        return redirect(url_for('auth.signup'))

    add_student = Student(nickname=nickname, name=name, group_rksi=group, email=email,
                          password=generate_password_hash(password=password, method="sha256"))

    db.session.add(add_student)
    db.session.commit()

    return redirect(url_for('auth.login'))


@auth.route('/logout')
def reg():
    return render_template('reg.html', url='logout')
