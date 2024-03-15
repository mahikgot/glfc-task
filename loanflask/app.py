from flask import Flask
import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from loanflask.config import config


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    from loanflask.models import db
    db.init_app(app)
    with app.app_context():
        db.create_all()
    from loanflask.routes import loan_bp
    app.register_blueprint(loan_bp)

    return app
