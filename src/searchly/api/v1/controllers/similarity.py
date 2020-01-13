from flask import request

from src.searchly.api.v1.services import response
from src.searchly.helper import searcher, log


def by_song():
    try:
        song_id = request.args.get('song_id')
        if not song_id:
            return response.make(error=True, message='`song_id` missed as a query parameter.')
        features = searcher.extract_features(song_id)
        if features is None:
            return response.make(error=True, message='Song not found.')
        results = searcher.search(features, song_id=song_id)
        return response.make(error=False, response=dict(similarity_list=results))
    except Exception as e:
        log.error(f'Unexpected error: [{e}]')
        log.exception(e)
        return response.make(error=True, message='Unexpected error.')
