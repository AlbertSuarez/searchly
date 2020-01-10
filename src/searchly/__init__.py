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


__all__ = [
    'DEVELOPMENT_MODE',
    'DB_USER',
    'DB_PASSWORD',
    'DB_DB',
    'DB_HOST',
    'DB_HOST_DEV',
    'DB_PORT',
    'DB_PORT_DEV',
    'API_SONG_SEARCH_LIMIT'
]
