from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    names = ["Alice", "Bob", "Charlie"]
    return render_template("index.html", names=names)


@app.route("/extended")
def extended():
    names2 = ["Stefan", "Jacek", "Charlie"]
    names = ["Alice", "Bob", "Charlie"]
    return render_template("index2.html", names=names, names2=names2)
