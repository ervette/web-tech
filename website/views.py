from flask import Blueprint, render_template
import json
from flask_login import login_required, logout_user, current_user

views = Blueprint('views', __name__)


@views.route('/')
@login_required
def home():
    with open('website/kanban.json', 'r') as file:
        data = json.load(file)
    return render_template("home.html", data=data, user=current_user)


@views.route('/progress')
@login_required
def progress():
    return render_template("progress.html", percentage=73, user=current_user)
