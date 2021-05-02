from fastapi import Security, HTTPException
from fastapi.security.api_key import APIKeyHeader

from config import READ_API_KEY, WRITE_API_KEY, API_KEY_NAME

api_key_header_auth = APIKeyHeader(name=API_KEY_NAME, auto_error=True)


def get_read_api_key(api_key_header: str = Security(api_key_header_auth)):
    if api_key_header not in (READ_API_KEY, WRITE_API_KEY):
        raise HTTPException(status_code=401, detail="Invalid API Key")


def get_write_api_key(api_key_header: str = Security(api_key_header_auth)):
    if api_key_header != WRITE_API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")
