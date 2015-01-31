from flask import Flask
from flask.ext.mongoengine import MongoEngine
from flask.ext.bcrypt import Bcrypt
from datetime import datetime
from flask import url_for



app = Flask(__name__)


app.config['MONGODB_DB'] = 'learnflow'
app.config['MONGODB_HOST'] = 'ds063869.mongolab.com'
app.config['MONGODB_PORT'] = 63869
app.config['MONGODB_USERNAME'] = 'hack'
app.config['MONGODB_PASSWORD'] = 'hackdat'
app.config["SECRET_KEY"] = "secretwords"

db = MongoEngine(app)
flask_bcrypt = Bcrypt(app)

def register_blueprints(app):
    # Prevents circular imports
    from learnflow.views import api
    app.register_blueprint(api)

register_blueprints(app)

if __name__ == '__main__':
    app.run()