import datetime as dt
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import tzlocal
from flask import flash, redirect, render_template, request, session, url_for
from werkzeug.utils import secure_filename

from config import Config
from extensions import db
from main import UserSettings, app
from models import Guests, UserSettings


def format_greek_name(name):
    words = name.split()
    empty = []
    for word in words:
        if (
            word == "χρήστος"
            or word == "Χρήστος"
            or word == "χρηστος"
            or word == "Χρηστος"
            or word == "Πέτρος"
            or word == "πετρος"
            or word == "πέτρος"
            or word == "Πετρος"
            or word == "τάσος"
            or word == "Τάσος"
            or word == "τασος"
            or word == "Τασος"
            or word == "Γιώργος"
            or word == "γιωργος"
            or word == "Γιωργος"
            or word == "γιώργος"
            or word == "Νίκος"
            or word == "νίκος"
            or word == "νικος"
            or word == "Νικος"
            or word == "Σπύρος"
            or word == "σπύρος"
            or word == "Σπυρος"
            or word == "σπυρος"
            or word == "Αλέκος"
            or word == "Αλεκος"
            or word == "αλέκος"
            or word == "αλεκος"
            or word == "Κυριάκος"
            or word == "κυριάκος"
            or word == "Κυριακος"
            or word == "κυριακος"
        ):
            word = word[:-1]
        elif word[-2:] == "ος" or word[-2:] == "ός":
            word = word[:-2] + "ε"
        elif word[-1] == "ς":
            word = word[:-1]
        empty.append(word)
    return " ".join(empty)


def handle_file_upload(file_name, folder_name, flash_success_msg, flash_error_msg):
    if file_name in request.files:
        file = request.files[file_name]
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config["UPLOAD_FOLDER"], folder_name, filename)
            file.save(file_path)
            flash(flash_success_msg, "success")
            return get_image_files(folder_name)
        else:
            flash(flash_error_msg, "error")
    return None


def get_image_files(folder):
    folder_path = os.path.join(app.config["UPLOAD_FOLDER"], folder)
    files = os.listdir(folder_path)
    return [f"/static/{folder}/{file_name}" for file_name in files]


def send_response_mail(response_mail, new_guest):
    # Create a MIMEText object for the email body
    msg = MIMEMultipart()
    msg.attach(MIMEText(response_mail, "plain", "utf-8"))

    # Set the email subject
    msg["Subject"] = f"Wedding {UserSettings.query.first().user_name}"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=Config.my_email, password=Config.password)
        connection.sendmail(Config.my_email, new_guest.email, msg.as_string())


def allowed_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in app.config["ALLOWED_EXTENSIONS"]
    )


def create_response_mail(new_guest):
    # Create the response mail content
    greeting = f"Αγαπητέ/ή {format_greek_name(new_guest.name)},"
    if new_guest.total_people == 1:
        main_body = "\nΕίμαστε πολύ χαρούμενοι που θα παρευρεθείτε στον γάμο μας. Αδημονούμε να σας δούμε από κοντά!"
    elif new_guest.total_people is None:
        main_body = "\nΛυπούμαστε που δεν θα παρευρεθείτε στον γάμο μας"
    elif new_guest.total_people > 1:
        main_body = f"\nΕίμαστε πολύ χαρούμενοι που θα παρευρεθείτε στον γάμο μας. Αδημονούμε να σας δούμε και τους {new_guest.total_people} από κοντά!"
    groom_bride_names = UserSettings.query.first().user_name
    names = [name.capitalize() for name in groom_bride_names.split()]
    contact_line = "-" * 92
    mail_ending = f"\nΜε εκτίμηση,\n{groom_bride_names}\n\n\n{contact_line}\nΑυτό είναι ένα αυτοματοποιημένο μήνυμα, παρακαλούμε μην απαντάτε στο παρόν e-mail.\nΣτοιχεία επικοινωνίας:\n{names[0]}: {Config.groom_phone}\n{names[2]}: {Config.bride_phone}"
    response_mail = f"{greeting}{main_body}{mail_ending}"
    return response_mail


def handle_response(form, template):
    from utils import create_response_mail, send_response_mail

    with open("valid_emails.txt", "r") as f:
        email_list = {email.strip() for email in f.readlines()}

    if form.validate_on_submit():
        email = form.email.data
        name = form.name.data
        message = form.message.data
        total_people = (
            int(form.total_people.data) if hasattr(form, "total_people") else None
        )

        existing_guest = Guests.query.filter_by(email=email).first()
        if email in email_list and existing_guest:
            existing_guest.name = name
            existing_guest.email = email
            existing_guest.message = message
            existing_guest.total_people = total_people
            existing_guest.date = dt.datetime.now(tzlocal.get_localzone())
            db.session.commit()
            # Pass form data to create_response_mail
            response_mail = create_response_mail(existing_guest)
            response_mail = response_mail.encode("utf-8")
            send_response_mail(response_mail, existing_guest)

            # Clear the session data
            session.pop("response_form_data", None)
            flash("Your information has been successfully updated.", "success")
            return redirect(url_for("main.home"))
        elif email in email_list and not existing_guest:
            new_guest = Guests(
                email=email,
                name=name,
                message=message,
                total_people=total_people,
            )
            db.session.add(new_guest)
            db.session.commit()
            # Pass form data to create_response_mail
            response_mail = create_response_mail(new_guest)
            response_mail = response_mail.encode("utf-8")
            send_response_mail(response_mail, new_guest)

            # Clear the session data
            session.pop("response_form_data", None)
            flash("Your information has been successfully submitted.", "success")
            return redirect(url_for("main.home"))
        elif email not in email_list:
            flash(
                f"Your email was not found in the registered list. Please contact the host at {Config.my_email} and ask to be registered.",
                "error",
            )

    return render_template(template, form=form)
