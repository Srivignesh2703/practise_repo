from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "sample code for github"


@app.route('/design')
def design():
    return "some design"
