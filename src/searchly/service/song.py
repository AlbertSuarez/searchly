from sqlalchemy import or_

from src.searchly import *
from src.searchly.db.sqlalchemy import db_session, add_element, commit_session
from src.searchly.helper import log
from src.searchly.model.v1.song import Song


def get_all_songs():
    """
    Retrieve all the songs from the database.
    :return: List of ORM objects representing all the song database.
    """
    return db_session().query(Song).order_by(Song.id).all()


def get_song(song_id):
    """
    Get a certain song given its identifier.
    :param song_id: Song identifier.
    :return: Song ORM representation.
    """
    return db_session().query(Song).filter_by(id=song_id).first()


def get_song_by_index_id(index_id):
    """
    Get a certain song given its NMSLIB index identifier.
    :param index_id: NMSLIB index identifier.
    :return: Song ORM representation.
    """
    return db_session().query(Song).filter_by(index_id=index_id).first()


def get_song_by_name_and_artist(song_name, artist_name):
    """
    Get a certain song given its name and artist name.
    :param song_name: Song name.
    :param artist_name: Artist name.
    :return: Song ORM representation.
    """
    return db_session().query(Song).filter_by(song_name=song_name, artist_name=artist_name).first()


def get_song_by_query(query):
    """
    Retrieve a list of songs that applies the given query.
    :param query: Query to use.
    :return: List of ORM objects.
    """
    return db_session()\
        .query(Song)\
        .filter(or_(
            Song.song_name.ilike('%' + query + '%'),
            Song.artist_name.ilike('%' + query + '%')
        ))\
        .limit(API_SONG_SEARCH_LIMIT)\
        .all()


def add_song(artist_name, song_name, lyrics, artist_url=None, song_url=None, index_id=None):
    """
    Add a song row to the database given all the information.
    :param artist_name: Artist name.
    :param song_name: Song name.
    :param lyrics: Song lyrics.
    :param artist_url: Artist URL.
    :param song_url: Song URL.
    :param index_id: NMSLIB index identifier.
    :return: Song identifier if it was added as expected, None otherwise.
    """
    try:
        song = Song(
            artist_name=artist_name,
            song_name=song_name,
            lyrics=lyrics,
            artist_url=artist_url,
            song_url=song_url,
            index_id=index_id
        )
        add_element(song)
        commit_session()
        return song.id
    except Exception as e:
        log.error(f'Error adding a song: [{e}]')
        log.exception(e)
        return None


def set_index_id(song_id, index_id):
    """
    Update the song instance given its identifier setting a new NMSLIB index identifier.
    :param song_id: Song identifier.
    :param index_id: NMSLIB index identifier.
    :return: True if the update was successful, False otherwise.
    """
    song = db_session().query(Song).filter_by(id=song_id).first()
    if song:
        song.index_id = index_id
        commit_session()
        return True
    else:
        log.warn(f'Not song found with id [{song_id}]')
        return False
