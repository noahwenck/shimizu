from flask import Flask, jsonify, Response, redirect
from shimizu import netflix_scraper

app = Flask(__name__)
# todo: Add logging + log file

@app.route('/')
def index():
    return redirect('/ping')

@app.route('/ping')
def hello_world():
    return Response("pong!", status=200, mimetype='text/plain')

@app.route('/netflix')
def netflix():
    """
    Endpoint to get the films expiring from Netflix.
    """
    expiring_films = netflix_scraper.extract_expiring_netflix()
    return jsonify([film.to_dict() for film in expiring_films])