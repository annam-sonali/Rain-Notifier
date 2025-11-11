import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

parameters = {
    "latitude": 17.2502,
    "longitude": 80.1760,
    "hourly":"weathercode",
    "forecast_hours":12,
    "timezone":"auto"
}

response = requests.get(f"https://api.open-meteo.com/v1/forecast", params=parameters)

data = response.json()
weather_list = data['hourly']['weathercode']

will_rain =False

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

client = Client(account_sid, auth_token)


for code in weather_list:
    if (
    (code > 50 and code < 67) or
    (code > 79 and code < 83) or
    (code > 94 and code < 100)
):
        will_rain = True


if will_rain:
    client.api.account.messages.create(
    to="+918185956526",
    from_="+17628883527",
    body = "Hey Sunny, heads up: rain is coming today. Don't forget your umbrella! ☂️")
    print("SMS SENT SUCCESSFULLY")

