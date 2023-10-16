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
<<<<<<< HEAD
    return render_template("progress.html", percentage = 31.99999)
=======
    return render_template("progress.html", percentage = 41)
>>>>>>> 21e9e79ce20bade5b79b6399cec4939dc468c312
