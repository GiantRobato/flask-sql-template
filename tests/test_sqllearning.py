from flask import testing, wrappers
from sqllearning.app.api import database, models
import sqlite3

def test_create_app(test_client: testing.FlaskClient):
    """ Test app creation
    """
    out: wrappers.Response = test_client.get("/api/")
    assert out.data.decode("utf-8").replace('"',"") == "pong!\n"

def test_post(test_client: testing.FlaskClient, mocked_session):
    out: wrappers.Response = test_client.get("/api/post")

    result = mocked_session.query(models.Customers).all()
    res : models.Customers
    for res in result:
        print(res.name)
        print(res.address)
        print(res.email)


