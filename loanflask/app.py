from flask import Flask
import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


def create_app():
    load_dotenv()
    app = Flask(__name__)
    #app.config.from_object(config_object)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DB_URI")
    app.config["SQLALCHEMY_ECHO"] = True

    from loanflask.models import db
    db.init_app(app)
    with app.app_context():
        db.create_all()
    from loanflask.routes import loan_bp
    app.register_blueprint(loan_bp)

    return app
