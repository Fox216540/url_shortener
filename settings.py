from dotenv import load_dotenv
import os

load_dotenv()

DB_CONFIG = {
    "dbname": os.getenv("POSTGRES_DB"),
    "user": os.getenv("POSTGRES_USER"),
    "password": os.getenv("POSTGRES_PASSWORD"),
    "host": os.getenv("POSTGRES_HOST"),
    "port": os.getenv("POSTGRES_PORT"),
}

POOL_SIZE = int(os.getenv("POOL_SIZE", 10))
POOL_MAX_SIZE = int(os.getenv("POOL_MAX_SIZE", 20))

URL = 'http://127.0.0.1:8000/'
