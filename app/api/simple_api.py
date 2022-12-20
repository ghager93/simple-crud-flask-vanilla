from flask import Blueprint
from flask.views import MethodView


bp = Blueprint("simple", __name__)


@bp.route("/helloworld", methods=["GET"])
def hello_world():
    return "hello world!"


class SimpleAPI(MethodView):
    def post(self):
        return "post"


simple = SimpleAPI.as_view("simple")
