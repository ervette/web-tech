from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
from flask_login import LoginManager
import openai





db = SQLAlchemy()


def create_app():
    load_dotenv()
    app = Flask(__name__)    
    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.getenv("DB_NAME")}'
    db.init_app(app)
    openai.api_key= os.getenv("OPENAI_API_KEY")
    openai.api_version

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[{"role": "user", "content": "Write me a 50 words essay about ChatGPT 3.5 Turbo greeting the customer"}]
        )

    print(completion)
    
    
    @app.route('/')
    def halo():
        # return "<h1><a href=" + "/hello" + ">say hello</a></h1>"
        return "<h1>" + completion + "</h1>"
        
        
    @app.route('/hello')
    def hallowor():
        return "<h1>Heloo world</h1>"
    
    return app
   

