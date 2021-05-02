from fastapi import FastAPI
from starlette.responses import RedirectResponse

from routers import router
from services import database
import config


def get_application():
    app = FastAPI(
        title=config.PROJECT_NAME, version=config.VERSION, docs_url="/", redoc_url=None
    )

    app.include_router(router)

    return app


app = get_application()
