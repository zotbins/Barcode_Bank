from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import barcode_router
from services import database
import config


def get_application():
    app = FastAPI(title=config.PROJECT_NAME, version=config.VERSION)

    app.include_router(barcode_router.router, prefix="/barcode", tags=["Barcode"])

    return app


app = get_application()


@app.get("/")
def read_root():
    return {"Hello": "Nice"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
