import smtplib, ssl
import json

path = "configuration.json"

with open(path, "r") as handler:
    info = json.load(handler)

user = info["user"]
passw = info["password"]


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = user
    password = passw

    receiver = user
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)