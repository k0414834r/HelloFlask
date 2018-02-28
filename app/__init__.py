from flask import Flask
from config import Config

app2 = Flask(__name__)
app2.config.from_object(Config)

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy(app2)
migrate = Migrate(app2, db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Post(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   title = db.Column(db.String(20))
   subtitle = db.Column(db.String(40))
   body = db.Column(db.String(280))
   user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

   def __repr__(self):
       return '<Post {}>'.format(self.body)

from app import routes