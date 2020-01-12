from src.searchly import *
from src.searchly.helper import log, word2vec
from src.searchly.searchly import nmslib_index
from src.searchly.service import song as song_service


def extract_features(song_id):
    song = song_service.get_song(song_id)
    if song:
        lyrics = song.lyrics
        lyrics = word2vec.clean_lyrics(lyrics)
        lyrics = ' '.join([item for sub_list in lyrics for item in sub_list])
        w2v_instance = word2vec.load_w2v_instance(FILE_NAME_W2V)
        lyrics = word2vec.normalize(lyrics, w2v_instance)
        if lyrics:
            return lyrics
        else:
            log.warn('Empty lyrics after normalizing it.')
            return None
    else:
        log.warn(f'Not song found with id: [{song_id}]')
        return None


def search(features, amount_results=API_SONG_SIMILARITY_LIMIT, song_id=None):
    results = []
    index_id = -1
    if song_id:
        song = song_service.get_song(song_id)
        if song:
            index_id = song.index_id
        else:
            log.warn(f'Not song found with id: [{song_id}]')
    query_results = nmslib_index.batch_query(features, NEIGHBOURHOOD_AMOUNT)
    closest, distances = query_results[0]
    for i, dist in zip(closest, distances):
        if i != index_id:
            song = song_service.get_song_by_index_id(i)
            if song:
                result = song.serialize()
                result['percentage'] = dist
                results.append(result)
    results = results[:amount_results]
    return results
