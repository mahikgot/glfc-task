from flask import Flask
import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

def create_app():
    app = Flask(__name__)
    #app.config.from_object(config_object)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DB_URI")

    from loanflask.models import *
    db.init_app(app)
    with app.app_context():
        db.create_all()

    return app
