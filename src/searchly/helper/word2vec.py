import multiprocessing
import re
import numpy as np
import string
import gensim.models.word2vec as w2v
import unidecode

from nltk.corpus import stopwords

from src.searchly import *
from src.searchly.helper import log


def clean_lyrics(lyrics):
    stop_words = set(stopwords.words('english'))
    translator = str.maketrans('', '', string.punctuation)
    lyrics = lyrics.translate(translator)
    words = [p for p in lyrics.lower().split() if p.isalpha()]
    return [w for w in words if w not in stop_words]


def clean_content(content):
    content = content.lower()
    content = content.strip()
    content = unidecode.unidecode(content)
    content = re.sub('[(\[].*?[)\]]', '', content)
    for _ in range(0, STR_CLEAN_TIMES):
        for to_be_replaced, to_replace in STR_CLEAN_DICT.items():
            content = content.replace(to_be_replaced, to_replace)
    content = content.strip()
    return content


def normalize(lyrics, w2v_instance):
    vector_sum = n_words = 0
    lyrics = clean_lyrics(lyrics)
    for word in lyrics:
        if word in w2v_instance:
            vector_sum += w2v_instance[word]
            n_words += 1
    if n_words:
        return vector_sum / n_words
    else:
        return None


def shape(lyrics_list):
    return np.array(lyrics_list)


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


def load_w2v_instance(file_path):
    return w2v.Word2Vec.load(file_path)
