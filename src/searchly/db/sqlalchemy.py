from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from src.searchly import *


def _connect(user, password, database, host, port):
    """
    Connect to the database given its parameters.
    :param user: Database user.
    :param password: Database password.
    :param database: Database name.
    :param host: Database hostname.
    :param port: Database port.
    :return: Tuple of two objects composed by database engine and metadata.
    """
    url = f'postgresql://{user}:{password}@{host}:{port}/{database}'
    _engine = create_engine(url, client_encoding='utf8')
    _meta = MetaData(bind=_engine, reflect=True)
    return _engine, _meta


def commit_session():
    """
    Commit the current state of the transaction to the database.
    :return: Database committed.
    """
    db_session().commit()


def add_element(element):
    """
    Add an ORM element to the database.
    :param element: ORM object.
    :return: Element added to the database.
    """
    db_session().add(element)


# Connect to the database.
if DEVELOPMENT_MODE:
    engine, meta = _connect(DB_USER, DB_PASSWORD, DB_DB, DB_HOST_DEV, DB_PORT_DEV)
else:
    engine, meta = _connect(DB_USER, DB_PASSWORD, DB_DB, DB_HOST, DB_PORT)
db_session = scoped_session(sessionmaker(bind=engine))

# Declare base.
Base = declarative_base()
Base.query = db_session.query_property()
