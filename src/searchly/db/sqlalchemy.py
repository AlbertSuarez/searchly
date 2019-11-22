from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from src.searchly import *


def connect(user, password, database, host, port):
    url = f'postgresql://{user}:{password}@{host}:{port}/{database}'
    _engine = create_engine(url, client_encoding='utf8')
    _meta = MetaData(bind=_engine, reflect=True)
    return _engine, _meta


# Connect to the database.
engine, meta = connect(DB_USER, DB_PASSWORD, DB_DB, DB_HOST, DB_PORT)
db_session = scoped_session(sessionmaker(bind=engine))

# Declare base.
Base = declarative_base()
Base.query = db_session.query_property()
