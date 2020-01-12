from src.searchly import *
from src.searchly.helper import log, word2vec
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
