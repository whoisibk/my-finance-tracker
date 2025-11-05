from extensions import db
from sqlalchemy import ForeignKey, select
from datetime import datetime
from sqlalchemy.orm import relationship


class User(db.Model):
    __tablename__ = 'user'

    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    job = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True) 
    password = db.Column(db.String(50), nullable=False)



    # def __repr__(self):
    #     return f'Your name is {self.name} and you are a {self.job}'


class Transaction(db.Model):
    __tablename__ =  'transaction'

    id = db.Column(db.Integer, primary_key=True)
    # currency = db.Column(db.String, nullable=False)
    type = db.Column(db.String(30), nullable=False) #income or expense
    description = db.Column(db.String[20], nullable=False)
    category = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, default=datetime.now, nullable=False)
    user_id = db.Column(db.Integer, ForeignKey('user.user_id'), nullable=False)

    transac = relationship('User', backref='user')

