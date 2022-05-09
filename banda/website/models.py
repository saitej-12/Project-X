from sqlalchemy.orm import backref
from . import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(150), unique=True, nullable=False)
	password = db.Column(db.String(150), nullable=False)
	first_name = db.Column(db.String(150), nullable=False)
	user_type = db.Column(db.String(1), nullable=False)
	mobile = db.Column(db.Integer, nullable=False)
	profile_pic = db.Column(db.String(150), nullable=False, default="default.jpg")
	dob = db.Column(db.DateTime(timezone=True), nullable=False)
	gender = db.Column(db.String(1), nullable=False)


class Company(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	company = db.Column(db.String(150), unique=True, nullable=False)
	offers = db.relationship('Offers')
	user = db.relationship('User')


class Offers(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	company_id = db.Column(db.Integer, db.ForeignKey('company.id'))
	package = db.Column(db.Integer, nullable=False)

