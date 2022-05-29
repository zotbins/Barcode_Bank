""" Barcode controller takes the request data from the
Barcode Router and passes it to the Barcode Services"""

from fastapi import HTTPException
from fastapi.responses import JSONResponse
from pydantic import constr
from sqlalchemy.orm import Session

from services import barcode_services
from models import barcode_model


def add_barcode(barcode_item: barcode_model.Barcode, db: Session):
    """Adds unique barcode to database. Returns error if not unique

    Args:
        barcode_item (barcode_model.Barcode): New barcode item to be added
        db (Session): Database session

    Raises:
        HTTPException: 400 Exception if barcode is not unique

    Returns:
        JSONResponse: Returns success response if successfully added
    """
    if barcode_services.is_barcode_unique(db=db, barcode_item=barcode_item):
        barcode_services.post_barcode(db=db, barcode_item=barcode_item)
        return JSONResponse(
            status_code=201,
            content={
                "detail": "Barcode has been successfully added to the database"},
        )


def add_barcodes(barcodes: barcode_model.Barcodes, db: Session):
    """Adds unique barcodes to database. Only inserts if all of the barcodes are unique.

    Args:
        barcodes (barcode_model.Barcodes): List of barcodes to be added
        db (Session): Database session

    Raises:
        HTTPException: 400 Exception if barcode is not unique

    Returns:
        JSONResponse: Returns success response if successfully added
    """
    if barcode_services.are_all_barcodes_unique(db=db, barcodes=barcodes):
        barcode_services.post_barcodes(db=db, barcodes=barcodes)
        return JSONResponse(
            status_code=201,
            content={
                "detail": "All barcodes have been successfully added to the database"}
        )


def get_barcode(barcode_id: constr(max_length=13), db: Session):
    """Queries the database for the requested barcode

    Args:
        db (Session): Database session
        barcode_id (constr, optional): Barcode to search for in the database

    Raises:
        HTTPException: 404 Exception if barcode is not found

    Returns:
        barcode_model.Barcode: Barcode requested from database
    """
    barcode_item = barcode_services.get_barcode(barcode_id=barcode_id, db=db)
    if barcode_item is None:
        raise HTTPException(status_code=404, detail="Barcode not found")

    return barcode_item
