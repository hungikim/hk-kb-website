from flask import Flask, render_template, request, redirect, url_for
import sys
application = Flask(__name__)

@application.route("/")
def hello():
    return render_template("hello.html")

if __name__ == "__main__":
    application.run(host='0.0.0.0')