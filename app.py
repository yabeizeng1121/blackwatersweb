from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/project")
def project():
    return render_template("project.html")


@app.route("/analysis")
def analysis():
    return render_template("analysis.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
