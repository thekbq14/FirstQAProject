from flask_testing import TestCase

from application import app, db
from application.models import Users, AthleticEvent

from flask import redirect, url_for

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"
        )

        return app
    
    def setUp(self):
        db.create_all()

        db.session.add(Users(first_name="Run some unit tests"))
        db.session.add(Users(first_name="Bob"))

        db.session.commit()
    
    def tearDown(self):
        db.drop_all()

class TestRead(TestBase):
    def test_home(self):
        response = self.client.get(url_for("home"))

        assert "Run some unit tests" in response.data.decode()
        assert "Bob" in response.data.decode()


class TestCreate(TestBase):
    def test_create(self):
        response = self.client.post(url_for("createfirstname", first_name = "Check create is working"),
            data = {"first_name": "Check create is working"},
            follow_redirects=True
        )

        assert "Check create is working" in response.data.decode()

class TestCreateLastName(TestBase):
    def test_createlastname(self):
        response = self.client.post(url_for("createlastname", last_name = "Check create is working"),
            data = {"last_name": "Check create is working"},
            follow_redirects=True
        )

        assert "Check create is working" in response.data.decode()

class TestCreateDistance(TestBase):
    def test_createdistance(self):
        response = self.client.post(url_for("createdistance", distance = "Check create is working"),
            data = {"distance": "Check create is working"},
            follow_redirects=True
        )

        assert "Check create is working" in response.data.decode()

class TestCreateTrackName(TestBase):
    def test_createdistance(self):
        response = self.client.post(url_for("createtrackname", track_name = "Check create is working"),
            data = {"trackname": "Check create is working"},
            follow_redirects=True
        )

        assert "Check create is working" in response.data.decode()

class TestCreateTrackType(TestBase):
    def test_createdistance(self):
        response = self.client.post(url_for("createtracktype", track_type = "Check create is working"),
            data = {"tracktype": "Check create is working"},
            follow_redirects=True
        )

        assert "Check create is working" in response.data.decode()

class TestCreateEvent(TestBase):
    def test_createdistance(self):
        response = self.client.post(url_for("createevent", event = "Check create is working"),
            data = {"event": "Check create is working"},
            follow_redirects=True
        )

        assert "Check create is working" in response.data.decode()

class TestTime(TestBase):
    def test_createdistance(self):
        response = self.client.post(url_for("createtime", time = "Check create is working"),
            data = {"time": "Check create is working"},
            follow_redirects=True
        )

        assert "Check create is working" in response.data.decode()

class TestUpdate(TestBase):
    def test_update(self):
        response = self.client.post(
            url_for("updatefirstname", first_name = "Check update is working", id = "1"),
            data = {"first_name": "Check update is working", "id": "1"},
            follow_redirects=True
        )

        assert "Check update is working" in response.data.decode()
        assert "Bob" in response.data.decode()

        assert "Run unit tests" not in response.data.decode()

class TestUpdateLastName(TestBase):
    def test_updatelastname(self):
        response = self.client.post(
            url_for("updatelastname", last_name = "Check update is working", id = "1"),
            data = {"last_name": "Check update is working", "id": "1"},
            follow_redirects=True
        )

        assert "Check update is working" in response.data.decode()
        assert "Bob" in response.data.decode()

        assert "Run unit tests" not in response.data.decode()


class TestDelete(TestBase):
    def test_delete(self):
        response = self.client.get(
            url_for("deleteuser", id=1),
            follow_redirects=True
            )
        
        assert "Run unit tests" not in response.data.decode()


class TestDeleteAthletes(TestBase):
    def test_deleteathletes(self):
        response = self.client.get(
            url_for("delete", id=1),
            follow_redirects=True
            )
        
        assert "Run unit tests" not in response.data.decode()

