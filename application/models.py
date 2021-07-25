from . import db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=True)
    last_name = db.Column(db.String(30), nullable=True)
    athletes = db.relationship('AthleticEvent', backref = "users")

class AthleticEvent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    distance = db.Column(db.String(30), nullable=True)
    track_name = db.Column(db.String(30), nullable=True)
    event = db.Column(db.String(30), nullable=True)
    track_type = db.Column(db.String(30), nullable=True)
    time = db.Column(db.Integer, nullable=True) 
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=True)