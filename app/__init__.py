import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()


def create_app():
    # initialize flask application
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_pyfile('config.py', silent=True)

    app.config.from_mapping(DATABASE=os.path.join(app.instance_path, 'app.db'))

    # Ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from app import api

    # register all blueprints
    app.register_blueprint(api.simple_bp, url_prefix="/")

    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        db.create_all()

    # register before request middleware
    # before_request_middleware(app=app)

    # # register after request middleware
    # after_request_middleware(app=app)

    # # register after app context teardown middleware
    # teardown_appcontext_middleware(app=app)

    # # register custom error handler
    # response.json_error_handler(app=app)

    # initialize the database
    # init_db()

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port="5000")