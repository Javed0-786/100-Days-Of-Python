##################### Extra Hard Starting Project ######################
import smtplib
import random
import datetime as dt
import pandas

records = []
contents = []
# 1. Update the birthdays.csv
data = pandas.read_csv("birthdays.csv")

today = dt.datetime.today()
birthday = dt.datetime(year=2022, month=6, day=9)


# 2. Check if today matches a birthday in the birthdays.csv
check = False
for (index, row) in data.iterrows():
    birthday = dt.datetime(year=row.year, month=row.month, day=row.day)
    # print(birthday.date())
    if today.date() == birthday.date():
        check = True
        records.append(row)


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
files = ["letter_templates/letter_1.txt",
         "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]

if check == True:
    for record in records:
        with open(random.choice(files)) as file:
            content = file.read()
            new_content = content.replace("[NAME]", record.Name, 1)
            contents.append(new_content)


# 4. Send the letter generated in step 3 to that person's email address.
my_email = "altaf9120573582@gmail.com"
password = "nnnkbwoghxvjizjf"
i = 0
for content in contents:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=records[i].email, msg=f"Subject:Happy Birthday\n\nto\n\n{records[i].Name}\n\n{content}")
        print("done")

    i += 1

print("Javed Not Done")
