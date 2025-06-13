from src.infra.websocket.connection_manager import ConnectionManager
from uuid import UUID
from fastapi import WebSocket
from src.logger import status_logger


class WebsocketService:
	def __init__(self, connect: ConnectionManager):
		self._connect = connect

	async def connect(self, websocket: WebSocket, room_id: UUID):
		status_logger.info('Переходим в service')
		await self._connect.connect(websocket=websocket, room_id=room_id)
		status_logger.info('Закончили в service')

	async def disconnect(self, websocket: WebSocket, room_id: UUID):
		await self._connect.disconnect(websocket=websocket, room_id=room_id)

	async def broadcast(self, data: dict, room_id: UUID):
		await self._connect.broadcast(data=data, room_id=room_id)
