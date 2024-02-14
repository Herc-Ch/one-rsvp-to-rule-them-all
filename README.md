# One RSVP to Rule Them All 🎉

## Overview 🤵👰

Welcome to the Wedding (LOTR themed) RSVP Web App! This application allows guests to RSVP for a wedding, and the hosts can manage the RSVPs.

🧙‍♂️ Motivation Behind the Project

As a passionate fan of the enchanting world of Lord of the Rings, I found myself searching for a unique and personalized way to handle RSVPs for my wedding. However, the available choices in the market were not only lacking the magical touch of Middle-earth but also came with hefty price tags.

Driven by the desire to create something truly special and cater to fellow LOTR enthusiasts, I embarked on the journey to build this RSVP Wedding Project. This project isn't just a practical solution; it's a labor of love inspired by the rich tapestry of Tolkien's universe.

🎊 Join the Fellowship of Unforgettable Weddings

I invite you to join the fellowship of couples who dare to make their wedding day truly unforgettable. Let this project be a testament to the love shared between two souls and the shared passion for the wonders of Middle-earth.

May your wedding be a journey filled with joy, love, and the magic that only Tolkien's world can inspire. Happy planning! 🌈💍🏹

## Table of Contents 📜

<details open>
<summary><b>(click to expand or hide)</b></summary>
<!-- MarkdownTOC -->

1. [Installation](#install)

1. [Running the App](#running)
1. [Dependencies](#depend)
1. [Usage](#usage)
   1. [Features](#features)
   1. [Uploads](#uploads)
   1. [Interaction](#interaction)
   1. [Emails](#important-note)
1. [Deployment](#deploy)
<!-- /MarkdownTOC -->
</details>

<a id="installation"></a>

## 1. Installation 🛠️

Clone the repository:

```bash

git clone https://github.com/Herc-Ch/wedding.git

```

and

```bash

cd wedding

```

Before running the app, you need to install the required packages. Open the terminal and run the following commands:

- On Windows:

```bash

python -m pip install -r requirements.txt

```

- On MacOS:

```bash

pip3 install -r requirements.txt

```

This will install the necessary packages for the project.

<a id="running"></a>

## 2. Running the App 🚀

To run the app, execute the following command:

```bash
python main.py
```

<a id="depend"></a>

## 3. Dependencies 📚

The Wedding RSVP Web App relies on the following libraries and frameworks:

- Flask

- Flask-Bootstrap

- Flask-SQLAlchemy

- Flask-WTF

- jQuery (JavaScript library for developing)

- python-dotenv

- Howler.js (JavaScript library for audio)

All required dependencies are listed in the `requirements.txt` file. Ensure that you have these packages installed before running the application.

### .env File Setup 🔐

Create a `.env` file in the project's root directory with the following configurations:

```env
# Flask App Secret Key
FLASK_SECRET_KEY=your_own_secret_key (it can be whatever u wish it to be, but strong keys are encouraged)
e.g. FLASK_SECRET_KEY = "12hsH6d98h7s8r7ghw9eg98w3"

# Host Email and App Password (Create an App Password in Google for security)
MY_EMAIL=your_email
PASSWORD=your_app_password

# Host Credentials
HOST_USERNAME=groom
HOST_PASSWORD=wedding2024

# Means of communication with the bride and groom
GROOM_PHONE= grooms_telephone_number or any other means of communication
BRIDE_PHONE = brides_telephone_number or any other means of communication

```

How to Set Up Google App Password:

1. Go to your Google Account's Security page.
2. Under "Signing in to Google," enable "2-Step Verification."
3. Go to the "App passwords" section.
4. Select "Mail" and "Other (Custom Name)" as the app.
5. Enter a custom name (e.g., "Wedding RSVP App").
6. Generate the app password.
7. Use the generated app password for the PASSWORD field in the .env file.

<a id="usage"></a>

## 4. Usage 🎊

<a id="features"></a>

## 4.1 Features 🌟

### Home Page 🏠

- The main page (`/`) displays essential information about the wedding, including images, invitation details, background images, and music.

- Hosts can customize wedding details by clicking the "Edit" button.

### Login 🔐

- Access the login page by navigating to `/login`.

- Enter the provided username and password to log in as the host.

   ![login_gif](https://github.com/Herc-Ch/wedding/assets/134635471/b9635e05-8960-4c9f-9cbb-c73707dc62fe)

### Logout 🚪

- Hosts can log out by navigating to `/logout`.

   ![logout_gif](https://github.com/Herc-Ch/wedding/assets/134635471/9d1e2b8f-b793-4111-b6a4-22766206d102)

  Upon logging out, the web app reverts to the guest view, rendering it incapable of editing any information or images.

### Attendance Confirmation ✅

- Guests can confirm attendance by filling out the form on `/attend`.

- Guests can decline the invitation by using the form on `/not_attend`.

   ![attend_gif](https://github.com/Herc-Ch/wedding/assets/134635471/99b4c9be-8404-47eb-a600-36b0bd75ca9a)


### Customization

- Hosts can customize the application's settings, such as wedding date, location, and honorary guests, while logged in.

- When editing the host name aka the bride's and groom's name, use something like 'and', or '&' in between their first names . Do not use any last names and keep the groom's name first (for correct assignments to the respectable phone numbers.)

  e.g. George and Samantha (This are the names that are going to appear at the automatic email response to your guests.)

  In case you want the bride's name to be first, just reassign the phone numbers of the .env file to the opposite initial assignment (in the position of the groom's number put the bride's and vice versa).

   ![custom_gif](https://github.com/Herc-Ch/wedding/assets/134635471/211e954e-88f6-411a-ab8c-47b27a5d5717)


<a id="uploads"></a>

## 4.2 File Uploads 📤

Hosts can upload images for the carousel, invitation, and background sections. Uploaded images are displayed on the home page.

💡 Please note that after uploading photos in the background and invitation folder, make sure to delete the images you do not want showing, only leaving the chosen ones. 🚫

- Select the mp3 of your choosing and place it into the static/music file.
- Canvas is a great choice to customise a unique wedding invitation.

<a id="interaction"></a>

## 4.3 Database Interaction 🗃️

The application uses a SQLite database to store guest information and user settings.

### Checking the Number of People Attending

To retrieve the total number of people attending the wedding from the SQLite database, you can use a program like DB Browser for SQLite. Follow these steps:

1. Open DB Browser for SQLite.
2. Navigate to the `instance/guests` directory in the database file (`guests.db`).
3. Execute the following SQL query to get the sum of the `total_people` column:

   ```sql
   SELECT sum(total_people) FROM guests;
   ```

4. The result will display the total number of people attending the wedding.

<a id="important-note"></a>

## 4.4. Important Note Regarding Valid Emails 📧

To ensure the security and integrity of the RSVP system, it is crucial to maintain a list of valid guest emails in the `valid_emails.txt` file. This file should be located in the root directory of the project. Follow these guidelines when populating the `valid_emails.txt` file:

1. **One Email Per Line:** Add each valid email address on a separate line. For example:

   ```plaintext
   guest1@example.com
   guest2@example.com
   ```
   Add your own email here, to be able to play around with the attend/not_attend features.
2. **Avoid Blank Lines:** Do not include any blank lines in the file.

3. **Prevent Spam and Bot Attacks:** Adding valid emails helps prevent spam submissions and potential bot attacks. Only guests with emails listed in this file will be able to use the RSVP functionality.

4. **Regularly Update the List:** Keep the `valid_emails.txt` file up-to-date with the latest guest emails.

Remember, any email not found in this list during RSVP submission will result in an error message, guiding guests to contact the host for registration. This measure adds an extra layer of security to your RSVP system.

Thank you for maintaining the integrity of your RSVP system!

<a id="deploy"></a>
## 5. Deployment

## 1. Update Debug Mode

Before deploying your web app, ensure that the Flask app's debug mode is set to `False`. Open the `main.py` and locate the line:

```python
app.run(debug=True)
```
Change it to:
```python
app.run(debug=False)
```

## 2. Procfile
A Procfile is included to specify the commands that are executed by the app on startup. Ensure that it is configured correctly for your application.
Feel free to explore and modify the code to suit your specific requirements. If you encounter any issues or have suggestions for improvements, please refer to the GitHub repository or contact the project contributors.
## 3. Deploying
Follow the deployment instructions for your chosen platform (e.g., Heroku, AWS, onrender etc.). Make sure to check the platform-specific documentation for any additional configuration or requirements.

Happy wedding planning! 🎉
