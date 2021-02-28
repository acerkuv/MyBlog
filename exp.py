from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

exp = Flask(__name__)

@exp.route('/')
def index():
    render_template("good_moorning.html")


if __name__=='__main__':
    exp.run(debug=True)