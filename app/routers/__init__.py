from fastapi import APIRouter

from routers.v0 import barcode_router

router = APIRouter()

router.include_router(barcode_router.router, prefix="/v0", tags=["v0"])
