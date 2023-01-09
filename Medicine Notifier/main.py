import requests
import schedule
import os
import time
from datetime import datetime
from Medicine import moxidexa, maquidry, rohta
import json

with open("config.json") as f:
    data = json.load(f)


os.environ["TZ"] = "Asia/Istanbul"
time.tzset()

all_medicine = [moxidexa, rohta, maquidry]


def send_to_telegram(message):
    apiToken = data["apiToken"]
    chatID = data["chatID"]
    apiURL = f"https://api.telegram.org/bot{apiToken}/sendMessage"

    try:
        response = requests.post(apiURL, json={"chat_id": chatID, "text": message})
        print(response.text)
    except Exception as e:
        print(e)


for i in all_medicine:
    for j in i.getPeriod:
        schedule.every().day.at(j).do(send_to_telegram, i.content)

while True:
    schedule.run_pending()
    time.sleep(1)
