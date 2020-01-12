import argparse

from tqdm import tqdm

from src.searchly import *
from src.searchly.helper import log, word2vec
from src.searchly.helper.nmslib import Nmslib
from src.searchly.service import song as song_service


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_file', type=str, default=FILE_NAME_W2V)
    parser.add_argument('--output_file', type=str, default=FILE_NAME_INDEX)
    return parser.parse_args()


def _get_all_lyrics():
    log.info('Getting all songs...')
    song_list = song_service.get_all_songs()
    lyrics_list = [song.lyrics for song in song_list]
    log.info(f'Lyrics: [{len(lyrics_list)}]')
    return lyrics_list


def _normalize_lyrics(lyrics_list, w2v_instance):
    lyrics_list_normalized = []
    log.info('Normalizing all lyrics...')
    for lyrics in tqdm(lyrics_list, total=len(lyrics_list)):
        lyrics_normalized = word2vec.normalize(lyrics, w2v_instance)
        if lyrics_normalized is not None:
            lyrics_list_normalized.append(lyrics_normalized)
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
    index_instance.save(args.output_file)
    log.info('Index built!')


def build():
    lyrics_list = _get_all_lyrics()
    w2v_instance = word2vec.load_w2v_instance(args.input_file)
    lyrics_list = _normalize_lyrics(lyrics_list, w2v_instance)
    lyrics_list = _shape(lyrics_list)
    _build(lyrics_list)


if __name__ == '__main__':
    args = parse_args()
    build()
