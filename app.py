from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return 'Главная страница'


@app.route('/news')
def news():
    return 'Новости страница'


@app.route('/students')
def students():
    return 'Студенты страница'


@app.route('/schedule')
def schedule():
    return 'Расписание страница'


@app.route('/profile')
def profile():
    return 'Профиль страница'


@app.route('/profile/edit')
def profile():
    return 'Профиль страница'


@app.route('/admin')
def admin():
    return 'Новости страница'


@app.route('/admin/add_news')
def add_news():
    return 'Добавление новости страница'


@app.route('/admin/edit_news')
def edit_news():
    return 'Редактирование новости страница'


@app.route('/admin/del_news')
def del_news():
    return 'Удаление новости страница'


@app.route('/admin/edit_student')
def edit_news():
    return 'Редактирование новости страница'


@app.route('/admin/del_student')
def del_news():
    return 'Удаление новости страница'


@app.route('/admin/stat')
def stat():
    return 'Статистика страница'


@app.route('/auth')
def auth():
    return 'Авторизация страница'


@app.route('/reg')
def reg():
    return 'Регистрация страница'


if __name__ == '__main__':
    app.run()
