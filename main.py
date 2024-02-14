import os

from dotenv import load_dotenv
from flask import Flask
from flask_bootstrap import Bootstrap5

from blueprints.bp import login_bp
from extensions import db
from models import UserSettings

# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
load_dotenv()
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DB_URI", "sqlite:///guests.db")
app.config["SECRET_KEY"] = os.getenv("FLASK_KEY")
app.config["UPLOAD_FOLDER"] = "./static"
app.config["ALLOWED_EXTENSIONS"] = {"png", "jpg", "jpeg", "gif", "mp3"}
Bootstrap5(app)

# initialize the app with the extension
db.init_app(app)


with app.app_context():
    db.create_all()
    # Check if there are any rows in the UserSettings table
    if not UserSettings.query.first():
        # If not, add a default row
        default_settings = UserSettings(
            user_name="George & Samantha",
            wedding_date="Friday 23, May 2024",
            wedding_address="Ktima Deda, Pylaia 555 35",
            time="6:30PM EEST",
            address_link="https://www.google.com/",
            honorary_guests_groom="Joe Doe",
            honorary_guests_bride="Elen Gray",
            iban="GR45 4575 4575 4575 4575 4575 377",
        )
        db.session.add(default_settings)
        db.session.commit()

app.register_blueprint(login_bp)


if __name__ == "__main__":
    app.run(debug=True)
