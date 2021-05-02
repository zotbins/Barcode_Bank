from fastapi import APIRouter
from typing import List
from models import barcode_model

router = APIRouter()


@router.get("/", response_model=barcode_model.Barcode)
async def get_all_barcodes() -> List[dict]:
    barcodes = {
        "barcode": "12000009105",
        "item": "10200774 - MUG ROOT BEER",
        "bin": "Recycle",
    }

    return barcodes
