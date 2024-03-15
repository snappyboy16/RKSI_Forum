from flask import Flask
from flask_migrate import Migrate
from flask_login import LoginManager
from RKSI_Forum.auth import auth as auth_blueprint
from RKSI_Forum.main import main as main_blueprint
from RKSI_Forum.models import Student, db

app = Flask(__name__)

app.config['SECRET_KEY'] = 'VERYSECRET'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

db.init_app(app)
migrate = Migrate(app, db)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)


@login_manager.user_loader
def add_user(student_id):
    return Student.query.get(int(student_id))


app.register_blueprint(auth_blueprint)
app.register_blueprint(main_blueprint)
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True)
