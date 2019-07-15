import datetime

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    now = datetime.datetime.now()
    new_year = now.month == 1 and now.day == 1
    return render_template("index.html", new_year=new_year)

@app.route("/today")
def today():
    now = datetime.datetime.now()
    today = now.month == now.month and now.day ==  now.day
    return render_template("today.html", today=today)

@app.route("/friday")
def friday():
    friday=datetime.datetime.today().weekday()== 4
    return render_template("friday.html", friday=friday)