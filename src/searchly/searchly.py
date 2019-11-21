import connexion

from flask_cors import CORS


connexion_app = connexion.FlaskApp(__name__, specification_dir='./openapi/')
flask_app = connexion_app.app
flask_app.config['JSON_AS_ASCII'] = False
connexion_app.add_api('openapi_v1.yaml', arguments={'title': 'SearchLy API v1'})
CORS(flask_app)


@flask_app.route('/api/v1')
def alive_check():
    return 'Welcome to SearchLy API!', 200
