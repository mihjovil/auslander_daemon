from flask import Flask
from logic.internal_class import check_website
from multiprocessing import Process
import json


def create_app():
    app = Flask(__name__)
    # Variables
    daemon_status_file = "static/daemon_status.json"

    # region Daemon declaration
    p = Process(target=check_website)
    p.start()
    # endregion

    @app.route('/')
    def index():
        return "<h1>Index page</h1><p>This is not an app with user interface.</p>"

    @app.route("/switch_status", methods=["GET"])
    def change_daemon_status():
        # Read the current status
        with open(daemon_status_file, "r") as f:
            status = json.load(f)
        current_status = status["on"]
        # Change the status
        with open(daemon_status_file, "w") as f:
            json.dump({"on": not current_status}, f)
        return f"<h1>The Daemon status has been changed to {not current_status}</h1>"

    @app.route("check_counter", methods=["GET"])
    def show_daemon_counter():
        with open(daemon_status_file, "r") as f:
            status = json.load(f)
        return f"<h1>The daemon has been executed {status['daemon_counter']}</h1>"
    return app
