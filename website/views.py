from flask import Blueprint, render_template
import json

views = Blueprint('views', __name__)


@views.route('/')
def home():
    with open('website/kanban.json', 'r') as file:
        data = json.load(file)
    return render_template("home.html", data=data)


@views.route('/progress')
def progress():
    return render_template("progress.html", percentage = 31.99999)
