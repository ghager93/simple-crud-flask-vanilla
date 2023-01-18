from flask import Blueprint, request, jsonify
from flask.views import MethodView

from app import db
from app import exceptions
from app.models import Simple


bp = Blueprint("simple", __name__)


@bp.route("/helloworld", methods=["GET"])
def hello_world():
    return "hello world!"


class SimpleAPI(MethodView):
    init_every_request = False

    def __init__(self, model):
        self.model = model 

    def post(self):
        try:
            entry = self.model.from_json(request.json)
        except exceptions.ValidationError:
            return "Invalid payload", 400

        try:
            db.session.add(entry)
            db.session.commit()
            return request.json
        except:
            return "Error saving to database", 500

    def get(self):
        return [item.to_json() for item in self.model.query.all()]


simple = SimpleAPI.as_view("simple", Simple)
bp.add_url_rule("/simple/", view_func=simple)
