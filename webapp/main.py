from flask import Flask, Blueprint, request, Response, render_template, url_for, redirect, make_response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
import requests
import json


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://admin:admin@postgres:5432/default_db'
db = SQLAlchemy(app)


class Survey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    party = db.Column(db.String(10), unique=False, nullable=False)
    eyes = db.Column(db.String(20), unique=False, nullable=False)

    def __repr__(self):
        return '<Party ' + self.party + ' eyes ' + self.email + '>'

    def __init__(self, party, eyes, id=None):
        self.id = id
        self.party = party
        self.eyes = eyes

    def get_all(self):
        data = {
            "id": self.id,
            "party": self.party,
            "eyes": self.eyes
        }
        return data


db.create_all()

try:
    user = Survey(party="pis", eyes="blue")
    db.session.add(user)
    db.session.commit()
except IntegrityError:
    db.session.rollback()


@app.route('/', methods=['GET'])
def get_survey():
    lock = request.cookies.get('lock')
    if lock == '1':
        return redirect(url_for('get_thanks'))
    else:
        return render_template("survey.html")


@app.route('/', methods=['POST'])
def upload_survey():
    lock = request.cookies.get('lock')
    if lock == '1':
        return redirect(url_for('get_thanks'))
    correct = True
    party = request.form['party']
    eyes = request.form['eyes']
    if correct:
        survey = Survey(party=party, eyes=eyes)
        db.session.add(survey)
        db.session.commit()
        resp = make_response(redirect(url_for('get_thanks')))
        resp.set_cookie('lock', '1')
        return resp  # redirect(url_for('get_thanks'))
    else:
        return render_template("survey.html")


@app.route('/thanks', methods=['GET'])
def get_thanks():
    return render_template("thanks.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
