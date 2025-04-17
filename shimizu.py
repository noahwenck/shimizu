from flask import Flask, jsonify, Response
import netflix_scraper

# NOTE: THIS WILL BE REDONE AT SOME POINT

app = Flask(__name__)

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


if __name__ == '__main__':
    app.run()