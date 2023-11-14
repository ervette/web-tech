from flask import Blueprint, render_template, request, url_for, redirect, flash, jsonify
import json
from werkzeug.utils import secure_filename
import os
from flask_login import login_required, logout_user, current_user
from openai import OpenAI
from . import db
from .models import User, Kanban
from sqlalchemy import Table, select
from dotenv import load_dotenv
client = OpenAI()

views = Blueprint('views', __name__)


@views.route('/')
@login_required
def home():
    # change to db gathering if applicable. if not just leave empty string.
    # with open('website/kanban.json', 'r') as file:
    #     data = json.load(file)
    data = Kanban.query.all()
    return render_template("home.html", data=data, user=current_user)


@views.route('/upload', methods=['GET', 'POST'])
def upload_file():
    load_dotenv()
    all_users = User.query.all()
    users_as_string = ' '.join(user.name for user in all_users)

    if 'file' not in request.files:
        return 'No file part', 400
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400
    if file:
        filename = secure_filename(file.filename)
        if filename != 'backlog.txt':
            return 'Invalid file name', 400
        file_contents = file.read().decode('utf-8')  # Parse file to string

        Kanban.query.delete()

        # Process the string as needed in your application
        OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

        completion = client.chat.completions.create(model="gpt-3.5-turbo",
                                                    messages=[{"role": "user",
                                                               "content": "I have backlog in plain text format." +
                                                               " I need you to analyse it and create the output in" +
                                                               " json named tasks that is structured like:" +
                                                               " | Task | Description | Asignee | Estimated-time-consumption |." +
                                                               " In Task column paste the name of task given from backlog." +
                                                               " in Description column generate several steps description to the task given." +
                                                               " In assignee column please asign tasks evenly for each team-member:" +
                                                               f" {users_as_string}. In estimated-time-consumption column" +
                                                               " calculate the estimated time consumption for the task" +
                                                               " for chosen assignee regarding its experience." +
                                                               f" That's the backlog: {file_contents}" +
                                                               " Only respond with json code as plain text without" +
                                                               " code block syntax around it."}])

        print(completion)

        info = str(completion.choices[0].message.content)

        json_data = completion.choices[0].message.content
        data = json.loads(json_data)

        for task in data['tasks']:
            new_task = Kanban(
                user_id=task["Assignee"],
                task=task['Task'],
                description=task['Description'],
                time_consumption=task['Estimated-time-consumption'],
                status=0
            )
            db.session.add(new_task)

        db.session.commit()

    return redirect(url_for('views.home'))
       # return f'File successfully uploaded and parsed! : {info}', 200


@views.route('/update_task_status', methods=['POST'])
@login_required
def update_task_status():
    task_id = request.form.get('task_id')
    status = request.form.get('status')
    if task_id is not None and task_id.isdigit():
        task_id = int(task_id)

        task = Kanban.query.get(task_id)
        if task:
            task.status = int(status)
            db.session.commit()
            flash("Updated on the database", category="success")
            # Return a JSON response with the flash message
            return jsonify({'message': 'Updated on the database'}), 200
        else:
            flash("Something went wrong. Try again.", category="error")
            
    return jsonify({'message': 'Error updating task'}), 400


@views.route('/progress')
@login_required
def progress():
    total_tasks = Kanban.query.count()
    completed_tasks = Kanban.query.filter(Kanban.status == 1).count()
    
    if total_tasks > 0:
        percentage = (completed_tasks / total_tasks) * 100
        print(percentage)
    else:
        print("No tasks found.")
    
    def find_closest_percentage(value, percentages):
        return min(percentages, key=lambda x: abs(x - value))

    available_percentages = [5, 15, 35, 50, 65, 75, 85, 100]
    closest_percentage = find_closest_percentage(percentage, available_percentages)
    
        # Here, you can replace the print statements with logic to display the pizza slice image
    print(f"Closest Percentage: {closest_percentage}")
    print(f"Image URL: pics/{closest_percentage}.png")
    
    return render_template("progress.html", percentage=percentage, closest_percentage=str(closest_percentage), user=current_user)
