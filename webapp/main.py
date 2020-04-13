from flask import Flask, Blueprint, request, Response, render_template, url_for, redirect, make_response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from flask_heroku import Heroku
import requests
import json
import os


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
heroku = Heroku(app)
db = SQLAlchemy(app)

port = int(os.environ.get("PORT", 5000))


class Survey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question1 = db.Column(db.Integer, unique=False, nullable=False)
    question2 = db.Column(db.Integer, unique=False, nullable=False)
    question3 = db.Column(db.Integer, unique=False, nullable=False)
    question4 = db.Column(db.Integer, unique=False, nullable=False)
    question5 = db.Column(db.Integer, unique=False, nullable=False)
    question6 = db.Column(db.Integer, unique=False, nullable=False)
    question7 = db.Column(db.Integer, unique=False, nullable=False)
    question8 = db.Column(db.Integer, unique=False, nullable=False)
    question9 = db.Column(db.Integer, unique=False, nullable=False)
    question10 = db.Column(db.Integer, unique=False, nullable=False)
    question11 = db.Column(db.Integer, unique=False, nullable=False)
    question12 = db.Column(db.Integer, unique=False, nullable=False)
    question13 = db.Column(db.Integer, unique=False, nullable=False)
    question14 = db.Column(db.Integer, unique=False, nullable=False)
    question15 = db.Column(db.Integer, unique=False, nullable=False)
    question16 = db.Column(db.Integer, unique=False, nullable=False)
    question17 = db.Column(db.Integer, unique=False, nullable=False)
    question18 = db.Column(db.Integer, unique=False, nullable=False)
    question19 = db.Column(db.Integer, unique=False, nullable=False)
    question20 = db.Column(db.Integer, unique=False, nullable=False)
    question21 = db.Column(db.Integer, unique=False, nullable=False)
    question22 = db.Column(db.Integer, unique=False, nullable=False)
    question23 = db.Column(db.Integer, unique=False, nullable=False)
    question24 = db.Column(db.Integer, unique=False, nullable=False)
    question25 = db.Column(db.Integer, unique=False, nullable=False)
    question26 = db.Column(db.Integer, unique=False, nullable=False)

    def __repr__(self):
        return '<Survey with id ' + self.id + '>'

    def __init__(self, *args):
        self.id = None
        self.question1 = int(args[0])
        self.question2 = int(args[1])
        self.question3 = int(args[2])
        self.question4 = int(args[3])
        self.question5 = int(args[4])
        self.question6 = int(args[5])
        self.question7 = int(args[6])
        self.question8 = int(args[7])
        self.question9 = int(args[8])
        self.question10 = int(args[9])
        self.question11 = int(args[10])
        self.question12 = int(args[11])
        self.question13 = int(args[12])
        self.question14 = int(args[13])
        self.question15 = int(args[14])
        self.question16 = int(args[15])
        self.question17 = int(args[16])
        self.question18 = int(args[17])
        self.question19 = int(args[18])
        self.question20 = int(args[19])
        self.question21 = int(args[20])
        self.question22 = int(args[21])
        self.question23 = int(args[22])
        self.question24 = int(args[23])
        self.question25 = int(args[24])
        self.question26 = int(args[25])


db.create_all()


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
    if correct:
        survey = Survey(request.form['question1'], request.form['question2'], request.form['question3'], request.form['question4'], request.form['question5'], request.form['question6'],
                        request.form['question7'], request.form['question8'], request.form['question9'], request.form[
                            'question10'], request.form['question11'], request.form['question12'],
                        request.form['question13'], request.form['question14'], request.form['question15'], request.form[
                            'question16'], request.form['question17'], request.form['question18'],
                        request.form['question19'], request.form['question20'], request.form['question21'], request.form[
                            'question22'], request.form['question23'], request.form['question24'],
                        request.form['question25'], request.form['question26'])
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
    app.run(host='0.0.0.0', port=port)
