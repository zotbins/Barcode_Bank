""" This module setups the environmental variables """

from starlette.config import Config

config = Config(".env")

PROJECT_NAME = "ZotBins Barcode Bank"
VERSION = "1.0.1"

SECRET_KEY = config("SECRET_KEY", cast=str, default="CHANGEME")

POSTGRES_USER = config("POSTGRES_USER", cast=str)
POSTGRES_PASSWORD = config("POSTGRES_PASSWORD", cast=str)
POSTGRES_SERVER = config("POSTGRES_SERVER", cast=str, default="db")
POSTGRES_PORT = config("POSTGRES_PORT", cast=str, default="5432")
POSTGRES_DB = config("POSTGRES_DB", cast=str)

READ_API_KEY = config("READ_API_KEY", cast=str)
WRITE_API_KEY = config("WRITE_API_KEY", cast=str)
API_KEY_NAME = config("API_KEY_NAME", str)

DATABASE_URL = config(
    "DATABASE_URL",
    cast=str,
    default="postgresql://{}:{}@{}:{}/{}".format(
        POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_SERVER, POSTGRES_PORT, POSTGRES_DB
    ),
)
