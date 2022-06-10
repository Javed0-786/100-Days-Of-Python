import requests
from datetime import datetime
import smtplib
import time


MY_LAT = 27.2046  # Your latitude
MY_LONG = 77.4977  # Your longitude

my_email = "altaf9120573582@gmail.com"
password = "nnnkbwoghxvjizjf"


response1 = requests.get(url="http://api.open-notify.org/iss-now.json")
response1.raise_for_status()
data = response1.json()


iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response2 = requests.get(
    "https://api.sunrise-sunset.org/json", params=parameters)
response2.raise_for_status()
data = response2.json()
print(data)
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

# If the ISS is close to my current position


def check_position():
    if (MY_LAT <= (iss_latitude + 5) and MY_LAT >= (iss_latitude-5)):
        if (MY_LONG <= (iss_longitude + 5) and MY_LONG >= (iss_longitude - 5)):
            return True

        else:
            return False

    else:
        return False

# and it is currently dark


def is_dark():
    if (time_now.hour >= sunset or time_now.hour <= sunrise):
        return True

    else:
        return False


# Then send me an email to tell me to look up.

def send_mail():
    with smtplib.SMTP("smtp.gmail.com")as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="alam9120573582@gmail.com", msg=f"Subject: My Details\n\nSunrise: {sunrise} \nSunset: {sunset}\nTime: :{time_now.hour}\nCoordinates: {iss_latitude, iss_longitude}\nHurrey the ISS is above you")


# BONUS: run the code every 60 seconds.
while True:
    if is_dark():
        if check_position():
            send_mail()
            quit()
    time.sleep(60)
