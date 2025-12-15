import logging
import sys
from logging import Formatter
from logging.handlers import RotatingFileHandler
from pathlib import Path

LOG_FORMAT_APP = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_DIR = Path("./logs")


class Configs:
    @staticmethod
    def _create_logger(name: str, file_name: str, level: int):
        LOG_DIR.mkdir(parents=True, exist_ok=True)
        log = logging.getLogger(name)
        log.setLevel(logging.DEBUG)

        if not log.handlers:  # Проверка на существующие хендлеры
            log_file = LOG_DIR / file_name
            handler = RotatingFileHandler(
                filename=log_file,
                maxBytes=2 ** 20,  # 1 MB
                backupCount=1,
                encoding="utf-8"
            )
            handler.setFormatter(Formatter(LOG_FORMAT_APP))
            handler.setLevel(level)
            log.addHandler(handler)

        return log

    @staticmethod
    def config_status_logger(name: str = "app"):
        log = Configs._create_logger(f"{name}_status", f"{name}.log", logging.INFO)
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(Formatter(LOG_FORMAT_APP))
        console_handler.setLevel(logging.INFO)  # Можно поменять на DEBUG для вывода всего
        log.addHandler(console_handler)
        return log

    @staticmethod
    def config_error_logger(name: str = 'app'):
        log = Configs._create_logger(f"{name}_error", f"errors_{name}.log", logging.ERROR)
        return log


status_logger = Configs.config_status_logger()
error_logger = Configs.config_error_logger()
