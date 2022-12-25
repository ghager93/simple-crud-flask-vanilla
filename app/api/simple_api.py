from flask import Blueprint
from flask.views import MethodView

from app.models import Simple


bp = Blueprint("simple", __name__)


@bp.route("/helloworld", methods=["GET"])
def hello_world():
    return "hello world!"


class SimpleAPI(MethodView):
    def __init__(self, model):
        self.model = model 

    def post(self):
        return "post"


simple = SimpleAPI.as_view("simple", Simple)
bp.add_url_rule("/simple/", view_func=simple)
