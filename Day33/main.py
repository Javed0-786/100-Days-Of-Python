import requests
import json

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response.status_code)
# data = response.json()
# print(data)
# latitude = data["iss_position"]["latitude"]
# longitude = data["iss_position"]["longitude"]
# print(f"Latitude: {latitude}\nLongitude: {longitude}")

# # if response.status_code == 404:
# #     raise Exception("That resourse does not exists.")
# # elif response.status_code == 401:
# #     raise Exception("You are not authourised to excess this data")


# response.raise_for_status()

parameters = {
    "lat": "31.253648",
    "lng": "75.697708",
    "formatted": 0
}


response = requests.get(
    "https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise, sunset)
# print()
