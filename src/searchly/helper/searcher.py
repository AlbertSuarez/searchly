from src.searchly import *
from src.searchly.helper import log, word2vec
from src.searchly.helper.nmslib import Nmslib
from src.searchly.service import song as song_service


def extract_features(song_id):
    song = song_service.get_song(song_id)
    if song:
        lyrics = song.lyrics
        lyrics = word2vec.clean_lyrics(lyrics)
        lyrics = ' '.join(lyrics)
        w2v_instance = word2vec.load_w2v_instance(FILE_NAME_W2V)
        lyrics = word2vec.normalize(lyrics, w2v_instance)
        if lyrics is not None:
            lyrics = lyrics.reshape((1, NUM_FEATURES))
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
    nmslib_index = Nmslib()
    nmslib_index.load(FILE_NAME_INDEX)
    query_results = nmslib_index.batch_query(features, NEIGHBOURHOOD_AMOUNT)
    closest, distances = query_results[0]
    for i, dist in zip(closest, distances):
        i = int(i)
        if i != index_id:
            song = song_service.get_song_by_index_id(i)
            if song:
                result = song.serialize()
                result['percentage'] = float(dist)
                results.append(result)
    results = results[:amount_results]
    return results


def get_maximum_distance(features, nmslib_index, neighbourhood_amount):
    query_results = nmslib_index.batch_query(features, neighbourhood_amount)
    closest, distances = query_results[0]
    maximum_distance = distances[-1]
    maximum_distance = float(maximum_distance)
    return maximum_distance
