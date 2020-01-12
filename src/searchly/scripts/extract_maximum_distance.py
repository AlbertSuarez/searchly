from tqdm import tqdm

from src.searchly import *
from src.searchly.helper import log, searcher
from src.searchly.helper.nmslib import Nmslib
from src.searchly.service import song as song_service


def _get_all_lyrics():
    log.info('Getting all songs...')
    song_list = song_service.get_all_songs()
    id_list = [song.id for song in song_list]
    log.info(f'Lyrics: [{len(id_list)}]')
    return id_list


def _extract(id_list):
    log.info('Extracting maximum distance...')
    nmslib_index = Nmslib()
    nmslib_index.load(FILE_NAME_INDEX)
    maximum_distance = 0.0
    for song_id in tqdm(id_list, total=len(id_list)):
        features = searcher.extract_features(song_id)
        if features is not None:
            song_maximum_distance = searcher.get_maximum_distance(features, nmslib_index, len(id_list))
            if song_maximum_distance > maximum_distance:
                maximum_distance = song_maximum_distance
    log.info('Extracted!')
    return maximum_distance


def _save(maximum_distance):
    log.info(f'Saving maximum distance: [{maximum_distance}]')
    with open(FILE_NAME_MAXIMUM_DISTANCE, 'w') as file:
        file.write(str(maximum_distance))
    log.info('Done!')


def extract():
    id_list = _get_all_lyrics()
    maximum_distance = _extract(id_list)
    _save(maximum_distance)


if __name__ == '__main__':
    extract()
