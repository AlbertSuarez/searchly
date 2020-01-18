from flask import request

from src.searchly.api.v1.services import response
from src.searchly.helper import log
from src.searchly.service import song as song_service


def search():
    """
    Controller for searching songs from the database.
    :return: JSON response.
    """
    try:
        query = request.args.get('query')
        if not query:
            return response.make(error=True, message='`query` missed as a query parameter.')
        query = query.strip()
        if len(query) <= 2:
            log.warn(f'Query is too short: [{query}]')
            return response.make(error=False, response=dict(results=[]))
        results = song_service.get_song_by_query(query)
        results = [{'id': q.id, 'name': f'{q.artist_name} - {q.song_name}'} for q in results]
        results = sorted(results, key=lambda q: q['name'])
        return response.make(error=False, response=dict(results=results))
    except Exception as e:
        log.error(f'Unexpected error: [{e}]')
        log.exception(e)
        return response.make(error=True, message='Unexpected error.')
