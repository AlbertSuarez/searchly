import multiprocessing
import re
import numpy as np
import string
import gensim.models.word2vec as w2v
import unidecode

from nltk.corpus import stopwords

from src.searchly import NUM_FEATURES, MIN_WORD_COUNT, CONTEXT_SIZE, DOWN_SAMPLING, STR_CLEAN_TIMES, STR_CLEAN_DICT
from src.searchly.helper import log


def clean_lyrics(lyrics):
    """
    Clean lyrics removing English stop words and punctuation characters.
    :param lyrics: Input content to clean.
    :return: Array of cleaned words from the given content.
    """
    stop_words = set(stopwords.words('english'))
    translator = str.maketrans('', '', string.punctuation)
    lyrics = lyrics.translate(translator)
    words = [p for p in lyrics.lower().split() if p.isalpha()]
    return [w for w in words if w not in stop_words]


def clean_content(content):
    """
    Clean input content from the API lowering case and removing non needed characters.
    :param content: Input content to clean.
    :return: String representation of the cleaned content.
    """
    content = content.lower()
    content = content.strip()
    content = unidecode.unidecode(content)
    content = re.sub(r'[(\[].*?[)\]]', '', content)
    for _ in range(0, STR_CLEAN_TIMES):
        for to_be_replaced, to_replace in STR_CLEAN_DICT.items():
            content = content.replace(to_be_replaced, to_replace)
    content = content.strip()
    return content


def normalize(lyrics, w2v_instance):
    """
    Normalize the lyrics of a song given the trained word2vec model.
    :param lyrics: String representation of the song lyrics.
    :param w2v_instance: Trained word2vec model.
    :return: Lyrics normalized.
    """
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
    """
    Shape a list of song lyrics to the required shape.
    :param lyrics_list: Lyrics list to shape.
    :return: Shaped list.
    """
    return np.array(lyrics_list)


def get_w2v_instance():
    """
    Get word2vec model instance.
    :return: Object representing the word2vec model.
    """
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
    """
    Save a word2vec instance to an output path.
    :param output_file: Output path where to save the instance.
    :param w2v_instance: Word2vec Instance to save.
    :return: Word2vec instance saved.
    """
    try:
        w2v_instance.save(output_file)
    except IOError as e:
        log.error(f'Error saving the word2vec instance: [{e}]')


def load_w2v_instance(file_path):
    """
    Load a word2vec instance given its file path.
    :param file_path: File path where the instance is located.
    :return: Word2vec instance.
    """
    return w2v.Word2Vec.load(file_path)
