from flask import Flask, render_template
from flask_cors import CORS

from src.searchly.api.v1.controllers import similarity
from src.searchly.db import sqlalchemy
from src.searchly.helper import log


flask_app = Flask(__name__, template_folder='./templates/')
flask_app.config['JSON_AS_ASCII'] = False
CORS(flask_app)


@flask_app.route('/')
def index():
    return render_template('index.html')


@flask_app.route('/api/v1')
def index_v1():
    return 'Welcome to SearchLy API /v1!', 200


@flask_app.route('/api/v1/similarity_by_song', methods=['GET'])
def similarity_by_song_get():
    return similarity.by_song()


@flask_app.teardown_appcontext
def shutdown_session(exception=None):
    log.debug(f'[DB] Session removed: {exception}')
    sqlalchemy.db_session.remove()
