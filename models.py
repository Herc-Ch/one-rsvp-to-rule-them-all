import tzlocal
import datetime as dt
from extensions import db


class Guests(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=False, nullable=False)
    email = db.Column(db.String(500), nullable=False, unique=True)
    total_people = db.Column(db.Integer, nullable=True)
    message = db.Column(db.String(500), nullable=True)
    date = db.Column(
        db.DateTime, nullable=False, default=dt.datetime.now(tzlocal.get_localzone())
    )


class UserSettings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(255))
    wedding_date = db.Column(db.String(255))
    wedding_address = db.Column(db.Text)
    time = db.Column(db.String(255))
    address_link = db.Column(db.String(255))
    honorary_guests_groom = db.Column(db.Text)
    honorary_guests_bride = db.Column(db.Text)
    iban = db.Column(db.String(255))