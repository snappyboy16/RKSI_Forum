from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from RKSI_Forum.models import Student, db

auth = Blueprint('auth', __name__)


@auth.route('/profile')
def profile():
    return render_template('profile.html', url='profile')


@auth.route('/login')
def login():
    return render_template('auth.html', url='login')


@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')

    student = Student.query.filter_by(email=email).first()
    print(student)
    if not student or not password:
        flash('Пожалуйста, проверьте свои данные для входа и повторите попытку.')
        return redirect(url_for('auth.login'))

    login_user(student)
    print(student)
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
    print(student)
    if student:
        flash('Адрес электронной почты уже существует')
        return redirect(url_for('auth.signup'))

    add_student = Student(nickname=nickname, name=name, group_rksi=group, email=email,
                          password=password)

    db.session.add(add_student)
    db.session.commit()

    return redirect(url_for('auth.login'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.home'))
