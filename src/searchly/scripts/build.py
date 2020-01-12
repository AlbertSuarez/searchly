from tqdm import tqdm

from src.searchly import *
from src.searchly.helper import log, word2vec
from src.searchly.helper.nmslib import Nmslib
from src.searchly.service import song as song_service


def _get_all_lyrics():
    log.info('Getting all songs...')
    song_list = song_service.get_all_songs()
    lyrics_list = [song.lyrics for song in song_list]
    log.info(f'Lyrics: [{len(lyrics_list)}]')
    return lyrics_list


def _normalize_lyrics(lyrics_list, w2v_instance):
    lyrics_list_normalized = []
    log.info('Normalizing all lyrics...')
    index_id = 0
    for idx, lyrics in tqdm(enumerate(lyrics_list), total=len(lyrics_list)):
        lyrics_normalized = word2vec.normalize(lyrics, w2v_instance)
        if lyrics_normalized is not None:
            lyrics_list_normalized.append(lyrics_normalized)
            song_service.set_index_id(idx + 1, index_id)
            index_id += 1
    log.info(f'Lyrics normalized: [{len(lyrics_list_normalized)}]')
    return lyrics_list_normalized


def _shape(lyrics_list):
    log.info('Shaping lyrics list...')
    lyrics_list = word2vec.shape(lyrics_list)
    log.info(f'Shaping done. Shape: [{lyrics_list.shape}]')
    return lyrics_list


def _build(lyrics_list):
    log.info('Building index...')
    index_instance = Nmslib()
    index_instance.fit(lyrics_list)
    index_instance.save(FILE_NAME_INDEX)
    log.info('Index built!')


def build():
    lyrics_list = _get_all_lyrics()
    w2v_instance = word2vec.load_w2v_instance(FILE_NAME_W2V)
    lyrics_list = _normalize_lyrics(lyrics_list, w2v_instance)
    lyrics_list = _shape(lyrics_list)
    _build(lyrics_list)


if __name__ == '__main__':
    build()
