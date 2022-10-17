import requests
from bs4 import BeautifulSoup
import re
import os
import time
import json
import logging

# region variables
auslander_path = "https://auslaenderbehoerdeonline.hannover-stadt.de/index.cfm?CFID=1191255&CFTOKEN=ad7fa839fad70672-EEFB617A-A3C7-DC0D-6B61823C37AC16EC"
token = os.getenv("TOKEN")
bot_url = f"https://api.telegram.org/bot{token}"
params = {"chat_id": os.getenv("CHAT_ID"),
          "text": f'There seems to be appointments in the Ausländerbehörde. {auslander_path}'}
pattern = r".*(Bitte versuchen Sie es am).*( Montag erneut).*"
daemon_status_file = "static/daemon_status.json"
# endregion

# initialize log
logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s', filename="daemon_log.log")


def check_website():
    while True:
        with open(daemon_status_file, "r") as f:
            status = json.load(f)
        should_continue = status["on"]
        if should_continue:
            # region Daemon
            # Getting the HTML from the page
            response = requests.get(auslander_path)
            # Find the paragraph that says there are no appointments
            soup = BeautifulSoup(response.content)
            text = soup.find('p').get_text()
            matches = re.findall(pattern, text, re.IGNORECASE)
            if len(matches) == 0:
                app_url = status["app_url"]
                params["text"] += f'. If you wish to check the daemon counter {app_url}/check_counter' \
                                  f' . If you want to turn it off {app_url}/switch_status'
                requests.get(bot_url + "/sendMessage", params=params)
                logging.info("found appointments")
        # TODO increase the counter
        time.sleep(60)
        # endregion


