from contextlib import contextmanager
from typing import Iterator

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

from config import DATABASE_PATH

engine = create_engine(f"sqlite:///{DATABASE_PATH}")
Base = declarative_base()
db_session = sessionmaker(bind=engine)


def _get_db_connection() -> Iterator[Session]:
    conn = db_session()
    try:
        yield conn
    finally:
        conn.close()


managed_db_connection = contextmanager(_get_db_connection)
