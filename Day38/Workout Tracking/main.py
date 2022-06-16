import requests
import datetime
from requests.auth import HTTPBasicAuth


API_ID = "**********"
API_KEY = "*************************************"
SHEET_ENDPOINT = "***************************************************************"
USERNAME = '**********'
PASSWORD = '************'

GENDER = "male"
WEIGHT_KG = "65"
HEIGHT_CM = "155"
AGE = "18"

exercise_text = input("Tell about your Excercise Today: ")


excercise_config = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

headers = {
    "x-app-key": API_KEY,
    "x-app-id": API_ID
}


response = requests.post(
    url="https://trackapi.nutritionix.com/v2/natural/exercise", json=excercise_config, headers=headers)

print(response.status_code)

date = datetime.datetime.now().date()
time = datetime.datetime.now().time()
date = date.strftime("%d/%m/%Y")
time = time.strftime("%H:%M:%S")


feed = response.json()
for data in feed['exercises']:
    name = data['name'].title()
    duration = data['duration_min']
    calories = data['nf_calories']

    workouts = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": name,
            "duration": duration,
            "calories": calories,
        }
    }

    response_sheety = requests.post(
        url=SHEET_ENDPOINT, json=workouts, auth=HTTPBasicAuth(USERNAME, PASSWORD))

response_sheety = requests.get(
    url=SHEET_ENDPOINT, auth=HTTPBasicAuth(USERNAME, PASSWORD))
nutritionix
