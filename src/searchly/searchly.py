from flask import Flask, render_template
from flask_cors import CORS

from src.searchly.api.v1 import song


flask_app = Flask(__name__, template_folder='./templates/')
flask_app.config['JSON_AS_ASCII'] = False
CORS(flask_app)


@flask_app.route('/')
def index():
    return render_template('index.html')


@flask_app.route('/api/v1')
def index_v1():
    return 'Welcome to SearchLy API /v1!', 200


@flask_app.route('/api/v1/song', methods=['GET'])
def song_get():
    return song.get()
