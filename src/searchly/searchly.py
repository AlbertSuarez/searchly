from flask import Flask, render_template, request, Response
from flask_cors import CORS

from src.searchly.api.v1.controllers import similarity, song, error
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


@flask_app.route('/api/v1/similarity/by_song', methods=['GET'])
def similarity_by_song_get():
    return similarity.by_song()


@flask_app.route('/api/v1/similarity/by_content', methods=['POST'])
def similarity_by_content_post():
    return similarity.by_content()


@flask_app.route('/api/v1/song/search', methods=['GET'])
def song_search_get():
    return song.search()


@flask_app.teardown_appcontext
def shutdown_session(exception=None):
    log.debug(f'[DB] Session removed: {exception}')
    sqlalchemy.db_session.remove()


@flask_app.errorhandler(404)
def endpoint_not_found(e):
    if request.path != '/favicon.ico':  # Avoid handing error for favicon 404 errors.
        return error.not_found(e)
    else:
        return Response.force_type(e, request.environ)


@flask_app.errorhandler(405)
def endpoint_not_found(e):
    return error.method_not_allowed(e)
