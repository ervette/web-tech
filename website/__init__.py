from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
from flask_login import LoginManager
import openai
import requests

db = SQLAlchemy()  # Initializing database
DB_NAME = "database.db"

def create_app():
    load_dotenv()  # Loading .env variables

    # Flask settings
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")

    # Database settings
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.getenv("DB_NAME")}'
    db.init_app(app)

    # ---------------------------------------------------------------
    # OpenAI API settings + data gathering

    # openai.api_key = os.getenv("OPENAI_API_KEY")
    # openai.api_version

    # completion = openai.ChatCompletion.create(
    #     model="gpt-3.5-turbo",
    #     messages=[{"role": "user", "content": "Hello!"}]
    #     )

    # print(completion)

    # TO RETRIEVE DATA => str(completion.choices[0].message.content)

    # ---------------------------------------------------------------

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
