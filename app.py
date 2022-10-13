from flask import Flask
from multiprocessing import Queue, Process
from logic.internal_class import check_website

def create_app():
    app = Flask(__name__)
    
    @app.route('/')
    def index():
        return "<h1>Index page</h1><p>This is not an app with user interface.</p>"
        

    if __name__ == '__main__':
        app.run()
    return app
