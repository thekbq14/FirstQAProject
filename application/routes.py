from . import app, db
from .models import Users, AthleticEvent

from flask import redirect, url_for

@app.route("/")
def home():
    user = Users.query.all()
    athletic = AthleticEvent.query.all()

    result = "<h1>My QA Project - Athletes Scoreboard</h1><br>"
    for users in user:
        result += f"{users.id:0>3} | {users.first_name} | {users.last_name} <br>"
    for athleticevent in athletic:
        result += f"{athleticevent.id} | {athleticevent.distance} | {athleticevent.track_name} | {athleticevent.event} | {athleticevent.track_type} | {athleticevent.time} <br>"
    
    return result

@app.route("/createdistance/<distance>")
def createdistance(distance):
    new_distance = AthleticEvent(distance=distance)
    db.session.add(new_distance)
    db.session.commit()

    return redirect(url_for("home"))

@app.route("/createtrackname/<track_name>")
def createtrackname(track_name):
    new_trackname = AthleticEvent(track_name=track_name)
    db.session.add(new_trackname)
    db.session.commit()

    return redirect(url_for("home"))

@app.route("/createevent/<event>")
def createevent(event):
    new_event = AthleticEvent(event=event)
    db.session.add(new_event)
    db.session.commit()

    return redirect(url_for("home"))

@app.route("/createtracktype/<track_type>")
def createtracktype(track_type):
    new_tracktype = AthleticEvent(track_type=track_type)
    db.session.add(new_tracktype)
    db.session.commit()

    return redirect(url_for("home"))

@app.route("/createtime/<time>")
def createtime(time):
    new_time = AthleticEvent(time=time)
    db.session.add(new_time)
    db.session.commit()

    return redirect(url_for("home"))

@app.route("/createfirstname/<first_name>")
def createfirstname(first_name):
    new_firstname = Users(first_name=first_name)
    db.session.add(new_firstname)
    db.session.commit()

    return redirect(url_for("home"))

@app.route("/createlastname/<last_name>")
def createlastname(last_name):
    new_lastname = Users(last_name=last_name)
    db.session.add(new_lastname)
    db.session.commit()

    return redirect(url_for("home"))

@app.route("/updatedistance/<int:id>/<distance>")
def updatedistance(id, distance):
    athleticevent = AthleticEvent.query.get(id)
    athleticevent.distance = distance
    db.session.add(athleticevent)
    db.session.commit()

    return redirect(url_for("home"))

@app.route("/updatetrackname/<int:id>/<track_name>")
def updatetrackname(id, track_name):
    athleticevent = AthleticEvent.query.get(id)
    athleticevent.track_name = track_name
    db.session.add(athleticevent)
    db.session.commit()

    return redirect(url_for("home"))

@app.route("/updateevent/<int:id>/<event>")
def updateevent(id, event):
    athleticevent = AthleticEvent.query.get(id)
    athleticevent.event = event
    db.session.add(athleticevent)
    db.session.commit()

    return redirect(url_for("home"))

@app.route("/updatetracktype/<int:id>/<track_type>")
def updatetracktype(id, track_type):
    athleticevent = AthleticEvent.query.get(id)
    athleticevent.track_type = track_type
    db.session.add(athleticevent)
    db.session.commit()

    return redirect(url_for("home"))

@app.route("/update/<int:id>/<time>")
def updatetime(id, time):
    athleticevent = AthleticEvent.query.get(id)
    athleticevent.time = time
    db.session.add(athleticevent)
    db.session.commit()

    return redirect(url_for("home"))

@app.route("/update/<int:id>/<first_name>")
def updatefirstname(id, first_name):
    users = Users.query.get(id)
    users.first_name = first_name
    db.session.add(users)
    db.session.commit()

    return redirect(url_for("home"))

@app.route("/update/<int:id>/<last_name>")
def updatelastname(id, last_name):
    users = Users.query.get(id)
    users.last_name = last_name
    db.session.add(users)
    db.session.commit()

    return redirect(url_for("home"))

@app.route("/delete/<int:id>")
def delete(id):
    athleticevent = AthleticEvent.query.get(id)
    db.session.delete(athleticevent)
    db.session.commit()

    return redirect(url_for("home"))

@app.route("/deleteusers/<int:id>")
def deleteuser(id):
    users = Users.query.get(id)
    db.session.delete(users)
    db.session.commit()

    return redirect(url_for("home"))