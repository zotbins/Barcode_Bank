"""Barcode router """
from fastapi import APIRouter, Depends, Security
from pydantic import constr
from sqlalchemy.orm import Session

from services import database, security
from models import barcode_model
from controllers import barcode_controller

router = APIRouter()


@router.post(
    "/barcode",
    status_code=201,
    responses={
        201: {
            "description": "Barcode has been successfully added to the database",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Barcode has been successfully added to the database"
                    }
                }
            },
        },
        400: {
            "description": "Barcode already exists in database",
            "content": {
                "application/json": {
                    "example": {"detail": "Barcode already exists in database"}
                }
            },
        },
    },
    dependencies=[Security(security.get_write_api_key)],
)
def post_barcode(
    barcode_item: barcode_model.Barcode, db: Session = Depends(database.get_db)
):
    return barcode_controller.add_barcode(barcode_item=barcode_item, db=db)


@router.get(
    "/barcode/{barcode_id}",
    response_model=barcode_model.Barcode,
    responses={
        200: {"description": "Returned barcode entry"},
        400: {
            "description": "Barcode not found",
            "content": {
                "application/json": {"example": {"detail": "Barcode not found"}}
            },
        },
    },
    dependencies=[Security(security.get_read_api_key)],
)
def get_barcode(
    barcode_id: constr(max_length=13), db: Session = Depends(database.get_db)
):
    return barcode_controller.get_barcode(barcode_id=barcode_id, db=db)
