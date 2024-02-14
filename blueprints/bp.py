import datetime as dt

from flask import Blueprint, flash, redirect, render_template, request, session, url_for

from config import Config
from extensions import db
from forms import Attending, NotAttending
from models import UserSettings

# from main import groom_username, groom_password
login_bp = Blueprint("main", __name__)


# Route for login
@login_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == Config.groom_username and password == Config.groom_password:
            session["logged_in"] = True
            flash("Login successful!", "success")
            return redirect(url_for("main.home"))
        else:
            flash("Invalid credentials. Please try again.", "error")
    return render_template("login.html")


@login_bp.route("/", methods=["GET", "POST"])
def home():
    from utils import get_image_files, handle_file_upload

    images = get_image_files("carousel")
    inv_img = get_image_files("invitation")
    back_img = get_image_files("background")
    song = get_image_files("music")

    # Get the current year dynamically
    current_year = dt.datetime.today().year

    # Fetch user settings from the database
    user_settings = UserSettings.query.first()
    if request.method == "POST":
        # Update user settings in the database
        user_settings.user_name = request.form.get("user_name", user_settings.user_name)
        user_settings.wedding_date = request.form.get(
            "wedding_date", user_settings.wedding_date
        )
        user_settings.wedding_address = request.form.get(
            "wedding_address", user_settings.wedding_address
        )
        user_settings.time = request.form.get("time", user_settings.time)
        user_settings.address_link = request.form.get(
            "address_link", user_settings.address_link
        )
        user_settings.honorary_guests_bride = request.form.get(
            "honorary_guests_bride", user_settings.honorary_guests_bride
        )
        user_settings.honorary_guests_groom = request.form.get(
            "honorary_guests_groom", user_settings.honorary_guests_groom
        )
        user_settings.iban = request.form.get("iban", user_settings.iban)
        # Handle file upload for carousel
        images = handle_file_upload(
            "carousel_file",
            "carousel",
            "Carousel File uploaded successfully",
            "Invalid file type for Carousel. Please upload an image",
        )

        # Handle file upload for invitation
        last_uploaded_invitation = handle_file_upload(
            "invitation_file",
            "invitation",
            "Invitation File uploaded successfully",
            "Invalid file type for Invitation. Please upload an image",
        )

        # Update invitation images list after handling invitation file upload
        if last_uploaded_invitation:
            inv_img = [last_uploaded_invitation]
        # Handle file upload for background
        last_uploaded_background = handle_file_upload(
            "background_file",
            "background",
            "Background File uploaded successfully",
            "Invalid file type for Background. Please upload an image",
        )
        if last_uploaded_background:
            back_img = [last_uploaded_background]
        db.session.commit()
        return redirect(url_for("main.home"))

    return render_template(
        "index.html",
        images=images,
        year=current_year,
        inv_img=inv_img,
        back_img=back_img,
        song=song,
        user_name=user_settings.user_name,
        wedding_date=user_settings.wedding_date,
        wedding_address=user_settings.wedding_address,
        iban=user_settings.iban,
        time=user_settings.time,
        address_link=user_settings.address_link,
        honorary_guests_bride=user_settings.honorary_guests_bride,
        honorary_guests_groom=user_settings.honorary_guests_groom,
    )


@login_bp.route("/logout")
def logout():
    # Clear the session
    session.clear()
    # Set session.logged_in to False
    session["logged_in"] = False
    # Flash a logout message
    flash("You have been successfully logged out.", "info")

    # Redirect to the login page
    return redirect(url_for("main.home"))


@login_bp.route("/attend", methods=["POST", "GET"])
def attend():
    from utils import handle_response

    form = Attending()
    return handle_response(form=form, template="attend.html")


@login_bp.route("/not_attend", methods=["POST", "GET"])
def not_attend():
    from utils import handle_response

    form = NotAttending()
    return handle_response(form=form, template="not_attend.html")
