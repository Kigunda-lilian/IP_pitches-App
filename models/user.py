import email
# from enum import unique
from app import db
from flask_login import UserMixin

class User(UserMixin,db.Model):
    __tablename__= "users"
    id = db.column(db.Integer,primary_key=True,autoincrement=True)
    first_name = db.column(db.string(),nullable=False)
    last_name = db.column(db.string(),nullable=False)
    user_name = db.column(db.string(),nullable=False,unique=True)
    email = db.column(db.string(),nullable=False)
    password = db.column(db.string(),nullable=False)