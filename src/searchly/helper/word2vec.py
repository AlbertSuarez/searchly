import string

from nltk.corpus import stopwords


def clean_lyrics(lyrics):
    stop_words = set(stopwords.words('english'))
    translator = str.maketrans('', '', string.punctuation)
    lyrics = lyrics.translate(translator)
    words = [p for p in lyrics.lower().split() if p.isalpha()]
    return [w for w in words if w not in stop_words]
