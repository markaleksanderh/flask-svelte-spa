from flask import (
    Flask,
    jsonify,
    send_from_directory,
)

from random import randint
import os


def create_app():
    app = Flask(__name__)
    app.secret_key = os.environ['SECRET_KEY']

    @app.route('/')
    def index():
        return send_from_directory('client/public', 'index.html')
    
    @app.route("/<path:path>")
    def home(path):
        return send_from_directory('client/public', path)

    # Returns random integer between 0 and 100
    @app.route('/randint')
    def random_integer():
        n = randint(0, 100)
        return jsonify({"integer": n})
    
    return app