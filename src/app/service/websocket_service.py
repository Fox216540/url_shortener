from uuid import UUID
from fastapi import WebSocket
from src.infra.websocket.connection_manager import ConnectionManager
from src.infra.websocket.exceptions.conn_manager_exception import ConnManagerException
from src.app.exceptions.websocket_exceptions import (
	InvalidConnect, InvalidDisconnect, InvalidBroadcast
)


class WebsocketService:
	def __init__(self, connect: ConnectionManager):
		self._connect = connect

	async def connect(self, websocket: WebSocket, room_id: UUID):
		try:
			await self._connect.connect(websocket=websocket, room_id=room_id)
		except ConnManagerException as e:
			raise e
		except Exception as e:
			raise InvalidConnect() from e

	async def disconnect(self, websocket: WebSocket, room_id: UUID):
		try:
			await self._connect.disconnect(websocket=websocket, room_id=room_id)
		except ConnManagerException as e:
			raise e
		except Exception as e:
			raise InvalidDisconnect() from e

	async def broadcast(self, data: dict, room_id: UUID):
		try:
			await self._connect.broadcast(data=data, room_id=room_id)
		except ConnManagerException as e:
			raise e
		except Exception as e:
			raise InvalidBroadcast() from e
