from flask_wtf import FlaskForm
from wtforms import EmailField, IntegerField, StringField, SubmitField
from wtforms.validators import DataRequired, Email

class Attending(FlaskForm):
    name = StringField("Ονοματεπώνυμο", [DataRequired()])
    email = EmailField("Διεύθυνση email", [DataRequired(), Email()])
    total_people = IntegerField("Άτομα (συνολικά)", [DataRequired()])
    message = StringField("Το μήνυμα σας στο ζευγάρι (προαιρετικό)")
    submit = SubmitField("Επιβεβαίωση")


class NotAttending(FlaskForm):
    name = StringField("Ονοματεπώνυμο", [DataRequired()])
    email = EmailField("Διεύθυνση email", [DataRequired(), Email()])
    message = StringField("Το μήνυμα σας στο ζευγάρι (προαιρετικό)")
    submit = SubmitField("Επιβεβαίωση")