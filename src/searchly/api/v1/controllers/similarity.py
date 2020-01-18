from flask import request

from src.searchly.api.v1.services import response
from src.searchly.helper import searcher, log


def by_song():
    """
    Controller for searching similarity through song identifier.
    :return: JSON response.
    """
    try:
        song_id = request.args.get('song_id')
        if not song_id:
            return response.make(error=True, message='`song_id` missed as a query parameter.')
        features = searcher.extract_features_from_song(song_id)
        if features is None:
            return response.make(error=True, message='Song not found.')
        results = searcher.search(features, song_id=song_id)
        return response.make(error=False, response=dict(similarity_list=results))
    except Exception as e:
        log.error(f'Unexpected error: [{e}]')
        log.exception(e)
        return response.make(error=True, message='Unexpected error.')


def by_content():
    """
    Controller for searching similarity through song lyrics content.
    :return: JSON response.
    """
    try:
        request_json = request.json
        content = response.get('content', request_json)
        if not content:
            return response.make(error=True, message='`content` missed as a request json parameter.')
        features = searcher.extract_features_from_content(content)
        if features is None:
            return response.make(error=True, message='Could not be possible to extract features from it.')
        results = searcher.search(features)
        return response.make(error=False, response=dict(similarity_list=results))
    except Exception as e:
        log.error(f'Unexpected error: [{e}]')
        log.exception(e)
        return response.make(error=True, message='Unexpected error.')
