import argparse
import csv
import glob
import zipfile

from tqdm import tqdm

from src.searchly.helper import log
from src.searchly.service import song as song_service


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_file', type=str, default='data/azlyrics-scraper.zip')
    parser.add_argument('--unzipping_output_folder', type=str, default='data/azlyrics-scraper')
    return parser.parse_args()


def _unzip():
    assert args.input_file.endswith('.zip')
    log.info('Opening input file...')
    with zipfile.ZipFile(args.input_file, 'r') as zip_file:
        log.info(f'Extracting all file from [{args.input_file}] into [{args.unzipping_output_folder}]...')
        zip_file.extractall(args.unzipping_output_folder)
    log.info('Unzipping done!')
    return args.unzipping_output_folder


def _get_csv_file_list(unzipping_output_folder):
    csv_file_list = [i for i in glob.glob(f'{unzipping_output_folder}/**/*.csv')]
    log.info(f'{len(csv_file_list)} CSV files extracted.')
    return csv_file_list


def _fill(csv_file_list):
    song_added = 0
    for csv_file_name in tqdm(csv_file_list, total=len(csv_file_list)):
        with open(csv_file_name, 'r') as csv_file:
            rows = [row for row in csv.reader(csv_file) if row][1:]
            for row in rows:
                try:
                    song_name = row[2]
                    artist_name = row[0]
                    if not song_service.get_song_by_name_and_artist(song_name, artist_name):
                        lyrics = row[4]
                        song_id = song_service.add_song(artist_name, song_name, lyrics)
                        song_added += int(bool(song_id))
                except Exception as e:
                    log.warn(f'Skipping row due to [{e}]')
                    log.warn(f'Row: {row}')
    log.info(f'Songs added: [{song_added}]')


def fill_database():
    unzipping_output_folder = _unzip()
    csv_file_list = _get_csv_file_list(unzipping_output_folder)
    _fill(csv_file_list)


if __name__ == '__main__':
    args = parse_args()
    fill_database()
