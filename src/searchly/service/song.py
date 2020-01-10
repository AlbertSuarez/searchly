from src.searchly import *
from src.searchly.db.sqlalchemy import db_session, add_element, commit_session
from src.searchly.helper import log
from src.searchly.model.v1.song import Song


def get_song(song_id):
    return db_session().query(Song).filter_by(id=song_id).first()


def get_song_by_name_and_artist(song_name, artist_name):
    return db_session().query(Song).filter_by(song_name=song_name, artist_name=artist_name).first()


def add_song(artist_name, song_name, lyrics, artist_url=None, song_url=None):
    try:
        song = Song(
            artist_name=artist_name,
            song_name=song_name,
            lyrics=lyrics,
            artist_url=artist_url,
            song_url=song_url
        )
        add_element(song)
        commit_session()
        return song.id
    except Exception as e:
        log.error(f'Error adding a song: [{e}]')
        log.exception(e)
        return None


def search_song(query):
    return db_session().query(Song).filter(Song.song_name.ilike(query + '%')).limit(API_SONG_SEARCH_LIMIT).all()
