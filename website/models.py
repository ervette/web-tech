from . import db
from flask_login import UserMixin

class Kanban(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    task = db.Column(db.String(500))
    description = db.Column(db.String(2000))
    time_consumption = db.Column(db.String(150))
    status = db.Column(db.Integer)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    name = db.Column(db.String(150))
    kanbans = db.relationship('Kanban')
    # team = db.Column(db.String(150))
    