from application import db
from application.models import Users, AthleticEvent

db.drop_all()
db.create_all()

name = Users(first_name="Kwame", last_name="Bamfo")
db.session.add(name)
db.session.commit()

one = AthleticEvent(distance = "100", track_name = "Croydon Arena", event = "Championships", track_type = "Track", time = "0:11",  users=name) 
two = AthleticEvent(distance = "200", track_name = "Hull Arena", event = "Training", track_type = "Track", time = "0:22",  users=name) 
three = AthleticEvent(distance = "400", track_name = "London Stadium", event = "Championships", track_type = "Track", time = "0:50",  users=name) 
four = AthleticEvent(distance = "800", track_name = "Manchester Arena", event = "Heats", track_type = "Field", time = "1:50",  users=name) 
five = AthleticEvent(distance = "1500", track_name = "Birmingham Park", event = "Championships", track_type = "Field", time = "4:10",  users=name) 
db.session.add(one)
db.session.add(two)
db.session.add(three)
db.session.add(four)
db.session.add(five)
db.session.commit()
