from flask import Flask, render_template
from flask import Blueprint
from flask_login import login_required, current_user

main = Blueprint('main', __name__)


@main.route('/')
def home():
    return render_template('index.html', url='home')


@main.route('/news')
def news():
    return render_template('news.html', url='news')


@main.route('/students')
def students():
    return render_template('students.html', url='students')


@main.route('/schedule')
def schedule():
    return render_template('schedule.html', url='schedule')


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', url='profile', name=current_user.name)


@main.route('/profile/edit')
def edit_profile():
    return render_template('edit_profile.html', url='profile')


@main.route('/admin')
def admin():
    return 'Новости страница'


@main.route('/admin/add_news')
def add_news():
    return 'Добавление новости страница'


@main.route('/admin/edit_news')
def edit_news():
    return 'Редактирование новости страница'


@main.route('/admin/del_news')
def del_news():
    return 'Удаление новости страница'


@main.route('/admin/edit_student')
def edit_student():
    return 'Редактирование новости страница'


@main.route('/admin/del_student')
def del_student():
    return 'Удаление новости страница'


@main.route('/admin/stat')
def stat():
    return 'Статистика страница'
