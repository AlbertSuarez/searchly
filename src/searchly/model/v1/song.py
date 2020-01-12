import sqlalchemy as db

from src.searchly.db.sqlalchemy import Base


class Song(Base):
    __tablename__ = 'searchly_song'

    id = db.Column(db.Integer, primary_key=True)
    artist_name = db.Column(db.String(256), nullable=False)
    song_name = db.Column(db.String(256), nullable=False)
    lyrics = db.Column(db.String(131072), nullable=False)
    artist_url = db.Column(db.String(256), nullable=True)
    song_url = db.Column(db.String(256), nullable=True)
    index_id = db.Column(db.Integer, nullable=True)

    def serialize(self):
        return dict(
            id=self.id,
            artist_name=self.artist_name,
            song_name=self.song_name,
            lyrics=self.lyrics,
            artist_url=self.artist_url,
            song_url=self.song_url,
            index_id=self.index_id
        )
