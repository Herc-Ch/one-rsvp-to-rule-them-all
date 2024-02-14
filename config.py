import os


class Config:
    my_email = os.getenv("MY_EMAIL")
    password = os.getenv("PASSWORD")
    groom_phone = os.getenv("GROOM_PHONE")
    bride_phone = os.getenv("BRIDE_PHONE")
    groom_username = os.getenv("HOST_USERNAME")
    groom_password = os.getenv("HOST_PASSWORD")
