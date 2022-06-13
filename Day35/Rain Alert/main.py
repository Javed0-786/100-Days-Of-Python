import requests
from twilio.rest import Client

OWN_EndPoint = "https://api.openweathermap.org/data/2.5/onecall?"
api_key = "d35f98f7bd41b8edbe31e39fe5afa888"

# AC7c1e84976efcaf0b1f60f5b323ca4692
account_sid = "AC7c1e84976efcaf0b1f60f5b323ca4692"
# 81a56a30224f6c048e9c4f3365e16aac
account_token = "81a56a30224f6c048e9c4f3365e16aac"
api_key_twilio = "SK8b35f4deb9d3b945ee3a8f2a553c2a7d"
# sid = SKfab2f393533fb1e7b361401de6219362

# GYKgtDxjdePCK5RZWkM9TXqkKoxEkQ2X || f6BMjgZp0UaJZQchBaarxYutZM36vo0N


weather_params = {
    "lat": 25.7,
    "lon": 92.45,
    "exclude": "current,minutely,daily",
    "appid": api_key
}

response = requests.get(OWN_EndPoint, params=weather_params)
data = response.json()["hourly"]


records = [record for record in data if data.index(record) < 12]
ids = [id['weather'][0]["id"] for id in records]
for id in ids:
    if id <= 700:
        check = True

if check == True:
    client = Client(account_sid, account_token, api_key_twilio)
    message = client.messages.create(
        body="It's going to rain 🌦️ today. Remember to bring an 🌂☂️☔", from_="+19895141558", to="+917076759685")
    print(message.status)

# from='+19895141558'
# body = "It's going to rain 🌦️ today. Remember to bring an ☔🌂☂️"
# to = "+918887876270"
