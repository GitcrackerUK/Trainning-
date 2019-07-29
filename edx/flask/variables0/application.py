from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    headline = "Introduction to flask!"
    paragraph ="The flask script is nice to start a local development server"
    article_title="Flask server"
    article="If you run the server you will notice that the server is only accessible from your own computer"
    return render_template("index.html", headline=headline, paragraph=paragraph, article_title=article_title, article=article)

@app.route("/more")
def more():
    headline = "Here is more about flask routing!"
    paragraph = "Welcome to Flask’s documentation. Get started with Installation and then get an overview with the Quickstart. "
    article_title = "User's Guide"
    article = "This part of the documentation, which is mostly prose, begins with some background information about Flask, then focuses on step-by-step instructions for web development with Flask."
    return render_template("index.html", headline=headline, paragraph=paragraph, article_title=article_title, article=article)
