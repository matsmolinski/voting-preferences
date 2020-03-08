from flask import Flask, Blueprint, request, Response, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
import requests
import json


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://admin:admin@postgres:5432/default_db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def __init__(self, username, email, id=None):
        self.id = id
        self.username = username
        self.email = email

    def get_all(self):
        data = {
            "id": self.id,
            "username": self.username,
            "email": self.email
        }
        return data

db.create_all()

try:
    user = User(username="admin", email="a@dmi.n")
    db.session.add(user)
    db.session.commit()
except IntegrityError:
    db.session.rollback()


@app.route('/', methods=['GET'])
def app_default():
    user_db = User.query.filter_by(user=user).first()
    print(user_db, flush=True)
    return render_template("loginForm.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
