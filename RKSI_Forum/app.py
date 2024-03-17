from flask.cli import FlaskGroup
from RKSI_Forum import app
from RKSI_Forum.models import db

cli = FlaskGroup(app)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True)
