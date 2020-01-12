from multiprocessing import Pool as ProcessPool
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


def __get_maximum_distance(args):
    song_id, neighbour_amount = args
    nmslib_index = Nmslib()
    nmslib_index.load(FILE_NAME_INDEX)
    features = searcher.extract_features(song_id)
    if features is not None:
        return searcher.get_maximum_distance(features, nmslib_index, neighbour_amount)
    else:
        return 0.0


def _extract(id_list):
    log.info('Extracting maximum distance...')
    with ProcessPool(SCRIPT_PROCESS_AMOUNT) as pool:
        args_list = [(song_id, len(id_list)) for song_id in id_list]
        r = list(tqdm(pool.imap(__get_maximum_distance, args_list, chunksize=SCRIPT_CHUNK_SIZE), total=len(args_list)))
        maximum_distance = max(r)
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
