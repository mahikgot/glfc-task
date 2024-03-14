import os
from dotenv import load_dotenv

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship

from typing import List


class Base(DeclarativeBase):
    pass
db = SQLAlchemy(model_class=Base)

class User(db.Model):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    loans: Mapped[List["Loan"]] = relationship(cascade="all, delete")

class Loan(db.Model):
    __tablename__ = "loans"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

