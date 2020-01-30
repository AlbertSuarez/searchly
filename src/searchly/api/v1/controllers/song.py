from flask import request

from src.searchly.api.v1.services import response
from src.searchly.helper import log, cache
from src.searchly.service import song as song_service


def search():
    """
    Controller for searching songs from the database.
    :return: JSON response.
    """
    try:
        # Parameters retrieving
        query = request.args.get('query')
        if not query:
            return response.make(error=True, message='`query` missed as a query parameter.')
        query = query.strip()
        if len(query) <= 2:
            log.warn(f'Query is too short: [{query}]')
            return response.make(error=False, response=dict(results=[]))
        # Cache processing
        method = search.__name__
        key = '{}'.format(query)
        results_cached = cache.get(method, key)
        if results_cached is not None:
            return response.make(response=results_cached, cached=True)
        # Searching
        results = song_service.get_song_by_query(query)
        results = [{'id': q.id, 'name': f'{q.artist_name} - {q.song_name}'} for q in results]
        results = sorted(results, key=lambda q: q['name'])
        # Return results and refresh cache
        return response.make(error=False, response=dict(results=results), method=method, key=key)
    except Exception as e:
        log.error(f'Unexpected error: [{e}]')
        log.exception(e)
        return response.make(error=True, message='Unexpected error.')
