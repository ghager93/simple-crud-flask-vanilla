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
    """
    View object for methods that work on the base /simple/ route.
    I.e. POST and GET (all)
    """

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


class SimpleIdAPI(MethodView):
    """
    View object for methods that work on the individual /simple/<id> route.
    I.e. GET, PATCH, DELETE"""

    init_every_request = False

    def __init__(self, model):
        self.model = model

    def get(self, id):
        item = self.model.query.get_or_404(id)
        return item.to_json()

    def delete(self, id):
        entry = self.model.query.get_or_404(id)
        try:
            db.session.delete(entry)
            db.session.commit()
            return entry.to_json()
        except:
            return "Error deleting from database", 500

    def patch(self, id):
        entry = self.model.query.get_or_404(id)
        try:
            [setattr(entry, attr, val) for attr, val in request.get_json().items()]
            db.session.commit()
            return entry.to_json()
        except:
            return "Error saving to database", 500


simple = SimpleAPI.as_view("simple", Simple)
simple_id = SimpleIdAPI.as_view("simpleid", Simple)

bp.add_url_rule("/simple/", view_func=simple)
bp.add_url_rule("/simple/<int:id>", view_func=simple_id)
