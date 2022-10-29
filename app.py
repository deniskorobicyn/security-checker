import os
from flask import Flask
from flask_alembic import Alembic
from flask_sqlalchemy import SQLAlchemy

# create the extension

#from extensions import database, commands
# blueprint import
from security_checker.blueprints.webhook.views import webhook
from security_checker.blueprints.api.v1 import api_v1

def create_app():
    app = Flask(__name__)
    # setup with the configuration provided by the user / environment
    app.config.from_object(os.environ['APP_SETTINGS'])
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ['DATABASE_URI']

    alembic = Alembic()
    alembic.init_app(app)

    db = SQLAlchemy()
    db.init_app(app)

    # register blueprint
    app.register_blueprint(webhook, url_prefix='/webhook')
    app.register_blueprint(api_v1, url_prefix='/api/v1')

    return app

if __name__ == "__main__":
    create_app().run()