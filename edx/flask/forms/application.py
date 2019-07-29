from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello", methods=["POST"])
def hello():
    name = request.form.get("name")
    return render_template("hello.html", name=name)


@app.route("/auto", methods=["GET","POST"])
def auto():
    if request.method == "GET":
        return render_template("warning.html")
    else:
        name = request.form.get("name")
        return render_template("auto.html", name=name)

@app.route("/place", methods=["POST"])
def place():
    name=request.form.get("name")
    return render_template("place.html", name=name)

@app.route("/color", methods=["POST"])
def color():
    name=request.form.get("name")
    return render_template("color.html", name=name)