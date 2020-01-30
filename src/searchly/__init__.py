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

# Cache settings
CACHE_MAX_LENGTH = 256
CACHE_MAX_AGE = 5 * 60  # 5 minutes
CACHE_DICT_FORMAT = '{}:{}'
