from contextlib import contextmanager
from settings import config as cg
import atexit

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#DATABASE_URL = f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['dbname']}"
#DATABASE_URL = f"postgresql://user:password@localhost:5432/books"

DATABASE_URL = (
    f"postgresql+psycopg2://{cg.DB_CONFIG['user']}:{cg.DB_CONFIG['password']}"
    f"@{cg.DB_CONFIG['host']}:{cg.DB_CONFIG['port']}/{cg.DB_CONFIG['dbname']}"
)

engine = create_engine(DATABASE_URL, pool_size=cg.POOL_SIZE, max_overflow=cg.POOL_MAX_SIZE)
Session = sessionmaker(
    bind=engine,
    expire_on_commit=False
)

@contextmanager
def get_session():
    session = Session()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()


def close_session_pool():
    if engine:
        engine.dispose()


def on_exit():
    print("Closing session pool")
    close_session_pool()


atexit.register(on_exit)