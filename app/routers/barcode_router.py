from fastapi import APIRouter, Depends, HTTPException
from typing import List
from models import barcode_model
from pydantic import constr

from sqlalchemy.orm import Session
from services import database, barcode_services

router = APIRouter()


@router.get("/")
def get_all_barcodes() -> List[dict]:
    barcodes = {
        "barcode": "12000009105",
        "item": "10200774 - MUG ROOT BEER",
        "bin": "Recycle",
    }

    return barcodes


@router.post("/", response_model=barcode_model.BarcodeResponse)
def post_barcode(
    barcode_item: barcode_model.Barcode, db: Session = Depends(database.get_db)
):
    barcode_services.post_barcode(db=db, barcode_item=barcode_item)


@router.get("/{barcode_id}", response_model=barcode_model.Barcode)
def get_barcode(
    barcode_id: constr(max_length=13), db: Session = Depends(database.get_db)
):
    barcode_item = barcode_services.get_barcode(barcode_id=barcode_id, db=db)
    if barcode_item is None:
        raise HTTPException(status_code=404, detail="Barcode not found")

    return barcode_item
