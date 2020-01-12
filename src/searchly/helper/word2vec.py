import multiprocessing
import string
import gensim.models.word2vec as w2v

from nltk.corpus import stopwords

from src.searchly import *
from src.searchly.helper import log


def clean_lyrics(lyrics):
    stop_words = set(stopwords.words('english'))
    translator = str.maketrans('', '', string.punctuation)
    lyrics = lyrics.translate(translator)
    words = [p for p in lyrics.lower().split() if p.isalpha()]
    return [w for w in words if w not in stop_words]


def get_w2v_instance():
    return w2v.Word2Vec(
        sg=1,
        seed=2,
        workers=multiprocessing.cpu_count(),
        size=NUM_FEATURES,
        min_count=MIN_WORD_COUNT,
        window=CONTEXT_SIZE,
        sample=DOWN_SAMPLING
    )


def save_w2v_instance(output_file, w2v_instance):
    try:
        w2v_instance.save(output_file)
    except IOError as e:
        log.error(f'Error saving the word2vec instance: [{e}]')
