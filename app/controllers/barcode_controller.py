from fastapi import HTTPException
from fastapi.responses import JSONResponse
from typing import List
from pydantic import constr
from sqlalchemy.orm import Session

from services import database, barcode_services
from models import barcode_model


def add_barcode(barcode_item: barcode_model.Barcode, db: Session):
    if barcode_services.is_barcode_unique(db=db, barcode_item=barcode_item):
        barcode_services.post_barcode(db=db, barcode_item=barcode_item)
        return JSONResponse(
            status_code=201,
            content={"message": "Barcode has been successfully added to the database"},
        )
    else:
        raise HTTPException(
            status_code=400, detail="Barcode already exists in database"
        )


def get_barcode(barcode_id: constr(max_length=13), db: Session):
    barcode_item = barcode_services.get_barcode(barcode_id=barcode_id, db=db)
    if barcode_item is None:
        raise HTTPException(status_code=404, detail="Barcode not found")

    return barcode_item
