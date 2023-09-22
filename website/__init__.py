from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
from flask_login import LoginManager


db = SQLAlchemy()


def create_app():
    load_dotenv()
    app = Flask(__name__)    
    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.getenv("DB_NAME")}'
    db.init_app(app)
    
    @app.route('/')
    def halo():
        return "<h1>" + os.getenv("TEST") + "</h1>"
        
    
    return app
   

