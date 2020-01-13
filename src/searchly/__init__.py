DEVELOPMENT_MODE = False

# Database connection
DB_USER = 'searchly'
DB_PASSWORD = 'searchly1234'
DB_DB = 'searchly'
DB_HOST = 'searchly_db'
DB_HOST_DEV = 'localhost'
DB_PORT = 5432
DB_PORT_DEV = 8089

# API settings
API_SONG_SEARCH_LIMIT = 100
API_SONG_SIMILARITY_LIMIT = 10

# Scripts settings
SCRIPT_ROW = ['ARTIST_NAME', 'ARTIST_URL', 'SONG_NAME', 'SONG_URL', 'LYRICS']
SCRIPT_PARALLEL = False
SCRIPT_PROCESS_AMOUNT = 8
SCRIPT_CHUNK_SIZE = 16

# String cleaning
STR_CLEAN_TIMES = 3
STR_CLEAN_DICT = {
    '\n\n': '\n',
    '\n\r\n': '\n',
    '\r': '',
    '\n': ', ',
    '  ': ' ',
    ' ,': ',',
    ' .': '.',
    ' :': ':',
    ' !': '!',
    ' ?': '?',
    ',,': ',',
    '..': '.',
    '::': ':',
    '!!': '!',
    '??': '?',
    '.,': '.',
    '.:': '.',
    ',.': ',',
    ',:': ',',
    ':,': ':',
    ':.': ':'
}

# AI settings
DATA_FOLDER = 'data'
FILE_NAME_W2V = f'{DATA_FOLDER}/w2v_trained.w2v'
FILE_NAME_INDEX = f'{DATA_FOLDER}/index.nmslib'
FILE_NAME_MAXIMUM_DISTANCE = f'{DATA_FOLDER}/maximum_distance.txt'
NUM_FEATURES = 50
MIN_WORD_COUNT = 1
CONTEXT_SIZE = 7
DOWN_SAMPLING = 1e-1
NEIGHBOURHOOD_AMOUNT = API_SONG_SIMILARITY_LIMIT * 10


__all__ = [
    'DEVELOPMENT_MODE',
    'DB_USER',
    'DB_PASSWORD',
    'DB_DB',
    'DB_HOST',
    'DB_HOST_DEV',
    'DB_PORT',
    'DB_PORT_DEV',
    'API_SONG_SEARCH_LIMIT',
    'API_SONG_SIMILARITY_LIMIT',
    'SCRIPT_ROW',
    'SCRIPT_PARALLEL',
    'SCRIPT_PROCESS_AMOUNT',
    'SCRIPT_CHUNK_SIZE',
    'STR_CLEAN_TIMES',
    'STR_CLEAN_DICT',
    'DATA_FOLDER',
    'FILE_NAME_W2V',
    'FILE_NAME_INDEX',
    'FILE_NAME_MAXIMUM_DISTANCE',
    'NUM_FEATURES',
    'MIN_WORD_COUNT',
    'CONTEXT_SIZE',
    'DOWN_SAMPLING',
    'NEIGHBOURHOOD_AMOUNT'
]
