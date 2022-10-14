import requests
from bs4 import BeautifulSoup
import re
import os
import time
import json

# region variables
auslander_path = "https://auslaenderbehoerdeonline.hannover-stadt.de/index.cfm?CFID=1191255&CFTOKEN=ad7fa839fad70672-EEFB617A-A3C7-DC0D-6B61823C37AC16EC"
token = os.getenv("TOKEN")
bot_url = f"https://api.telegram.org/bot{token}"
params = {"chat_id": os.getenv("CHAT_ID"),
          "text": f'There seems to be appointments in the Ausländerbehörde. <a href="{auslander_path}">Click here to check!</a>'}
pattern = r".*(Bitte versuchen Sie es am).*( Montag erneut).*"
daemon_status_file = "static/daemon_status.json"
# endregion


def check_website():
    while True:
        with open(daemon_status_file, "r") as f:
            status = json.load(f)
        should_continue = status["on"] == "on"
        if should_continue:
            # region Daemon
            # Getting the HTML from the page
            response = requests.get(auslander_path)
            # Find the paragraph that says there are no appointments
            soup = BeautifulSoup(response.content)
            text = soup.find('p').get_text()
            matches = re.findall(pattern, text, re.IGNORECASE)
            if len(matches) == 0:
                requests.get(bot_url + "/sendMessage", params=params)
        time.sleep(60)
        # endregion


