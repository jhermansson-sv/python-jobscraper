from flask import Flask
from .routes import main

def create_app():
    app = Flask(__name__)

    app.config.from_object('config')
    app.config['SECRET_KEY'] = app.config.get('SECRET_KEY')

    app.register_blueprint(main)
    
    return app 