from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

 
db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    todos = db.relationship('Todo', backref='user', lazy=True)

    def __repr__(self):
        return f'<User {self.username}>'


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(256), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'text': self.text,
        }