import argparse

from tqdm import tqdm

from src.searchly import *
from src.searchly.helper import log, word2vec
from src.searchly.service import song as song_service


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output_file', type=str, default=FILE_NAME_W2V)
    return parser.parse_args()


def _get_all_lyrics():
    log.info('Getting all songs...')
    song_list = song_service.get_all_songs()
    lyrics_list = [song.lyrics for song in song_list]
    log.info(f'Lyrics: [{len(lyrics_list)}]')
    return lyrics_list


def _clean_lyrics(lyrics_list):
    lyrics_list_cleaned = []
    log.info('Cleaning all lyrics...')
    for lyrics in tqdm(lyrics_list, total=len(lyrics_list)):
        lyrics_list_cleaned.append(word2vec.clean_lyrics(lyrics))
    log.info(f'Lyrics cleaned: [{len(lyrics_list_cleaned)}]')
    return lyrics_list_cleaned


def train():
    lyrics_list = _get_all_lyrics()
    lyrics_list = _clean_lyrics(lyrics_list)


if __name__ == '__main__':
    args = parse_args()
    train()
