from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from typing import Dict, List

router = APIRouter(tags=["websocket"])


class ConnectionManager:
	def __init__(self):
		self.active_connections: Dict[str, List[WebSocket]] = {}

	async def connect(self, websocket: WebSocket, short_code: str):
		await websocket.accept()
		if short_code not in self.active_connections:
			self.active_connections[short_code] = []
		self.active_connections[short_code].append(websocket)

	def disconnect(self, websocket: WebSocket, short_code: str):
		if short_code in self.active_connections:
			self.active_connections[short_code].remove(websocket)
			if not self.active_connections[short_code]:
				del self.active_connections[short_code]

	async def broadcast(self, message: str, short_code: str):
		if short_code in self.active_connections:
			for connection in self.active_connections[short_code]:
				await connection.send_text(message)


manager = ConnectionManager()


@router.websocket("/ws/{short_code}")
async def websocket_endpoint(websocket: WebSocket, short_code: str):
	await manager.connect(websocket, short_code)
	try:
		while True:
			data = await websocket.receive_text()
			await manager.broadcast(f"Сообщение: {data}", short_code)
	except WebSocketDisconnect:
		manager.disconnect(websocket, short_code)
