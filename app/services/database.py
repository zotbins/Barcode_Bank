from fastapi import FastAPI
from typing import Callable

from databases import Database
from config import DATABASE_URL
import logging

logger = logging.getLogger(__name__)


def create_start_app_handler(app: FastAPI) -> Callable:
    async def start_app() -> None:
        await connect_to_db(app)

    return start_app


def create_stop_app_handler(app: FastAPI) -> Callable:
    async def stop_app() -> None:
        await close_db_connection(app)

    return stop_app


async def connect_to_db(app: FastAPI) -> None:
    database = Database(
        DATABASE_URL, min_size=2, max_size=10
    )  # these can be configured in config as well
    try:
        await database.connect()
        app.state._db = database
        logger.info("DATABASE CONNNECTED")
    except Exception as e:
        logger.warn("--- DB CONNECTION ERROR ---")
        logger.warn(e)
        logger.warn("--- DB CONNECTION ERROR ---")


async def close_db_connection(app: FastAPI) -> None:
    try:
        await app.state._db.disconnect()
    except Exception as e:
        logger.warn("--- DB DISCONNECT ERROR ---")
        logger.warn(e)
        logger.warn("--- DB DISCONNECT ERROR ---")
