from uuid import UUID
from fastapi import WebSocket
from src.infra.websocket.connection_manager import ConnectionManager
from src.infra.websocket.exceptions.conn_error_list import ERRORS_CONN_MANAGER

class WebsocketService:
	def __init__(self, connect: ConnectionManager):
		self._connect = connect

	async def connect(self, websocket: WebSocket, room_id: UUID):
		try:
			await self._connect.connect(websocket=websocket, room_id=room_id)
		except ERRORS_CONN_MANAGER as e:
			raise e
		except Exception as e:  #TODO: ошибка сервиса
			raise e

	async def disconnect(self, websocket: WebSocket, room_id: UUID):
		try:
			await self._connect.disconnect(websocket=websocket, room_id=room_id)
		except ERRORS_CONN_MANAGER as e:
			raise e
		except Exception as e:  #TODO: ошибка сервиса
			raise e

	async def broadcast(self, data: dict, room_id: UUID):
		try:
			await self._connect.broadcast(data=data, room_id=room_id)
		except ERRORS_CONN_MANAGER as e:
			raise e
		except Exception as e:  #TODO: ошибка сервиса
			raise e
