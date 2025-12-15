# redis_context.py
import redis
import os
from contextlib import contextmanager
import atexit

from redis import ConnectionPool

from settings import config as cg

_pool: ConnectionPool | None = None
_client = None


def get_redis_pool():
	global _pool
	if _pool is None:
		_pool = redis.ConnectionPool(
			host=cg.REDIS_CONFIG["host"],
			port=int(cg.REDIS_CONFIG["port"]),
			db=int(cg.REDIS_CONFIG["db"]),
			password=cg.REDIS_CONFIG["password"] or None,
			max_connections=int(cg.REDIS_CONFIG["max_connections"]),
			decode_responses=True,
		)
	return _pool


def get_redis_client():
	global _client
	if _client is None:
		_client = redis.Redis(connection_pool=get_redis_pool())
	return _client


@contextmanager
def get_redis():
	client = get_redis_client()
	try:
		yield client
	finally:
		# Redis клиент не требует закрытия соединения в обычном смысле,
		# но можно добавить логику, если используешь транзакции, пайпы и т.п.
		pass


def close_redis_pool():
	global _pool
	if _pool:
		_pool.disconnect()
		_pool = None


def on_exit():
	print("Closing Redis connection pool")
	close_redis_pool()


atexit.register(on_exit)
