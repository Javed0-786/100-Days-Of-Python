# import smtplib
# my_email = "altaf9120573582@gmail.com"
# password = "nnnkbwoghxvjizjf"


# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls()
# connection.login(user=my_email, password=password)
# connection.sendmail(from_addr=my_email,
#                     to_addrs="mohammad.altaf786@yahoo.com", msg="Subject:Hello\n\nIs everything fine")
# connection.close()

'''
import smtplib
my_email = "altaf9120573582@gmail.com"
password = "nnnkbwoghxvjizjf"


with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="mohammad.altaf786@yahoo.com", msg="Subject:Hello\n\nIs everything fine")
'''
import smtplib
import datetime as dt
import random

my_email = "altaf9120573582@gmail.com"
password = "nnnkbwoghxvjizjf"

with open("quotes.txt", "r") as file:
    lines = file.readlines()

Quote = random.choice([line.strip() for line in lines])
today = dt.datetime.now()
day = today.weekday()

if day == 0 or day == 2:
    with smtplib.SMTP("smtp.gmail.com")as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="alam9120573582@gmail.com", msg=f"Subject:Monday Motivation\n\n{Quote}")
