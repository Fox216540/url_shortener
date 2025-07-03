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

URL = os.getenv("WEB_DOMAIN")

ACCESS_SECRET = os.getenv("ACCESS_SECRET", "supersecretkey")

REDIS_CONFIG = {
	"host": os.getenv("REDIS_HOST"),
	"port": os.getenv("REDIS_PORT"),
	"db": os.getenv("REDIS_DB"),
	"password": os.getenv("REDIS_PASSWORD"),
	"max_connections": os.getenv("REDIS_MAX_CONN")
}

ACCESS_TOKEN_TIME = int(os.getenv("ACCESS_TOKEN_TIME"))
REFRESH_TOKEN_TIME = int(os.getenv("REFRESH_TOKEN_TIME"))

BUFFER_SECONDS = int(os.getenv("BUFFER_SECONDS"))



class Config:
	def __init__(self):
		self.BUFFER_SECONDS = BUFFER_SECONDS
		self.REFRESH_TOKEN_TIME = REFRESH_TOKEN_TIME
		self.ACCESS_TOKEN_TIME = ACCESS_TOKEN_TIME
		self.REDIS_CONFIG = REDIS_CONFIG
		self.ACCESS_SECRET = ACCESS_SECRET
		self.URL = URL
		self.POOL_MAX_SIZE = POOL_MAX_SIZE
		self.POOL_SIZE = POOL_SIZE
		self.DB_CONFIG = DB_CONFIG

config = Config()
