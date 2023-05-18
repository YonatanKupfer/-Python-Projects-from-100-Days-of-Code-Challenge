import smtplib
from email.mime.text import MIMEText


MY_EMAIL = "testyonatan100@gmail.com"
MY_PASSWORD = "sbbztjscjvppigkf"


class NotificationManager:
    def send_mail(self, body):
        msg = MIMEText(body.encode("utf-8"), 'plain', 'utf-8')
        msg["Subject"] = "Flight Alert"
        msg["From"] = MY_EMAIL
        msg["To"] = "yonatank50@gmail.com"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs="yonatank50@gmail.com",
                                msg=msg.as_string()
                                )

