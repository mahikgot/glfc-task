from flask import Flask
import os
from dotenv import load_dotenv
from sqlalchemy.orm import DeclarativeBase

app = Flask(__name__)

class Base(DeclarativeBase):
    pass
#db = SQLAlchemy(model_class=Base)
#app.config["SQLALCHEMY_DATABASE_URL"] = os.getenv("DB_URI")
#db.init_app(app)


from loanflask import routes

