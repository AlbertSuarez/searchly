from tqdm import tqdm

from src.searchly import *
from src.searchly.helper import log, word2vec
from src.searchly.service import song as song_service


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


def _train(w2c_instance, lyrics_list):
    log.info('Introducing the vocabulary...')
    w2c_instance.build_vocab(lyrics_list)
    log.info('Vocabulary introduced.')
    lyrics_count = w2c_instance.corpus_count
    epochs_count = w2c_instance.epochs
    log.info(f'Lyrics count: [{lyrics_count}]')
    log.info(f'Epochs count: [{epochs_count}]')
    log.info('Start training...')
    w2c_instance.train(lyrics_list, total_examples=lyrics_count, epochs=epochs_count)
    log.info('Trained!')
    log.info('Saving instance...')
    word2vec.save_w2v_instance(FILE_NAME_W2V, w2c_instance)
    log.info(f'Saved in [{FILE_NAME_W2V}]')


def train():
    lyrics_list = _get_all_lyrics()
    lyrics_list = _clean_lyrics(lyrics_list)
    w2c_instance = word2vec.get_w2v_instance()
    _train(w2c_instance, lyrics_list)


if __name__ == '__main__':
    train()
