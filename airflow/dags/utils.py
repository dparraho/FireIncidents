import os
from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


@contextmanager
def get_session():
    user = os.environ["POSTGRES_USER"]
    password = os.environ["POSTGRES_PASS"]
    db = os.environ["POSTGRES_DB"]
    host = os.environ["PG_HOST"]
    port = os.environ["PG_PORT"]

    print(f"postgresql://{user}:{password}@{host}:{port}/{db}")

    engine = create_engine(
        f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}")

    session = scoped_session(
        sessionmaker(
            bind=engine,
            autocommit=False,
            autoflush=False
        )
    )
    yield session, engine

    session.close()