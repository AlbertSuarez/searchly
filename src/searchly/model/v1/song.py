import sqlalchemy as db

from src.searchly.db.sqlalchemy import Base


class Song(Base):
    __tablename__ = 'searchly_song'

    id = db.Column(db.Integer, primary_key=True)
    artist_name = db.Column(db.String(256), nullable=False)
    song_name = db.Column(db.String(256), nullable=False)
    lyrics = db.Column(db.String(4096), nullable=False)

    def serialize(self):
        return dict(
            id=self.id,
            artist_name=self.artist_name,
            song_name=self.song_name,
            lyrics=self.lyrics
        )
