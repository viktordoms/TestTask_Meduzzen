from datetime import datetime

from app import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(500), nullable=False)
    register_date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return 'User %r>' % self.username

    def __init__(self, id, username, email, password, register_date):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.register_date = register_date
