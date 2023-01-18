from flask import Blueprint, request, jsonify
from flask.views import MethodView

from app import db
from app.models import Simple


bp = Blueprint("simple", __name__)


@bp.route("/helloworld", methods=["GET"])
def hello_world():
    return "hello world!"


class SimpleAPI(MethodView):
    def __init__(self, model):
        self.model = model 

    def post(self):
        db.session.add(self.model(**request.json))
        db.session.commit()
        return request.json

    def get(self):
        return [item.to_json() for item in self.model.query.all()]


simple = SimpleAPI.as_view("simple", Simple)
bp.add_url_rule("/simple/", view_func=simple)
