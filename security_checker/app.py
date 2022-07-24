import os
from flask import Flask
#from extensions import database, commands
# blueprint import
from .blueprints.webhook.views import webhook
def create_app():
    app = Flask(__name__)
    # setup with the configuration provided by the user / environment
    app.config.from_object(os.environ['APP_SETTINGS'])
    
    # setup all our dependencies
    #database.init_app(app)
    #commands.init_app(app)
    
    # register blueprint
    app.register_blueprint(webhook, url_prefix='/webhook')
    
    return app
if __name__ == "__main__":
    create_app().run()