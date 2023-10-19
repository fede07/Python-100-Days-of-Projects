import random
import smtplib
import datetime as dt

my_email = "dummy@gmail.com"
password = "testingpass"

today = dt.datetime.now()
day_of_week = today.weekday()

if day_of_week == 0:

    quote = ""

    with open("quotes.txt") as quotes_file:
        quotes = quotes_file.readlines()
        quote = random.choice(quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="dummy2@gmail.com",
            msg="Subject:Hello\n\n" + quote
        )





