from flask import Flask
import requests
from bs4 import BeautifulSoup
import re
import os


def create_app():
    app = Flask(__name__)

    # region Daemon
    # Getting the HTML from the page
    auslander_path = "https://auslaenderbehoerdeonline.hannover-stadt.de/index.cfm?CFID=1191255&CFTOKEN=ad7fa839fad70672-EEFB617A-A3C7-DC0D-6B61823C37AC16EC"
    response = requests.get(auslander_path)
    token = os.getenv("token")
    bot_url = f"https://api.telegram.org/bot{token}"
    params = {"chat_id": os.getenv("chat_id"), "text": f'There seems to be appointments in the Ausländerbehörde. <a href="{auslander_path}">Click here to check!</a>'}

    # Find the paragraph that says there are no appointments
    pattern = r".*(Bitte versuchen Sie es am).*( Montag erneut).*"
    soup = BeautifulSoup(response.content)
    text = soup.find('p').get_text()
    matches = re.findall(pattern, text, re.IGNORECASE)
    if(len(matches) == 0):
        r = requests.get(bot_url + "/sendMessage", params=params)
    # endregion
    
    @app.route('/')
    def index():
        return "<h1>Index page</h1><p>This is not an app with user interface.</p>"
        

    if __name__ == '__main__':
        app.run()
    return app
