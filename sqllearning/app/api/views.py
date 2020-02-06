from flask import jsonify, wrappers, current_app, request
from ..api import api
from . import database, models

@api.route("/")
def default_route() -> wrappers.Response:
    return jsonify("pong!")

@api.route("/post")
def test_post() -> wrappers.Response:
    session = database.create_session('sqlite://')
    customer = models.Customers("john", "1234 Street", "john@doe.com")
    session.add(customer)
    session.commit()    
    return "Posted!"