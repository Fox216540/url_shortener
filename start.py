from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.api.link_handlers import router as link_router
from src.api.user_handlers import router as user_router
from src.api.message_websocket import router as websocket_router
from src.api.message_handler import router as message_router
from src.api.health_handler import router as health_router
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from src.logger import status_logger
from fastapi.middleware.gzip import GZipMiddleware
from src.core.Middleware.jwtmiddleware import JWTMiddleware



@asynccontextmanager
async def app_logger(application):
    status_logger.info("Starting my new application")
    # globals.smtp_pool = SMTPPool(
    #     host=os.getenv("SMTP_SERVER"),
    #     port=int(os.getenv("SMTP_PORT")),
    #     username=os.getenv("SMTP_USER"),
    #     password=os.getenv("SMTP_PASSWORD"),
    #     use_tls=True
    # )
    # status_logger.info("Пулл подключен")
    yield
    # if globals.smtp_pool is not None:
    #     await globals.smtp_pool.close()
    status_logger.info("Shutting down application")


app = FastAPI(lifespan=app_logger)#docs_url=None, redoc_url=None
app.add_middleware(
    CORSMiddleware,     # type: ignore
    allow_origins=["http://localhost:8000", "http://localhost:3000"],  # Разрешаем все домены, например, ["http://localhost:3000", "http://127.0.0.1:8000"]
    allow_credentials=True,
	allow_methods=["*"],  # включить OPTIONS, GET, POST, PUT, DELETE и т.д.
	allow_headers=["*"],  # Разрешаем все заголовки
)
app.add_middleware(GZipMiddleware, minimum_size=1000)   # type: ignore
app.add_middleware(JWTMiddleware)   # type: ignore
app.include_router(health_router)
app.include_router(websocket_router)

app.include_router(user_router)
app.include_router(message_router)
app.include_router(link_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
