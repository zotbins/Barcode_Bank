"""Barcode services to query the database"""
from fastapi import HTTPException
from sqlalchemy.orm import Session
from models import barcode_model


def get_barcode(db: Session, barcode_id: str):
    """[summary]

    Args:
        db (Session): Database session
        barcode_id (str): Barcode query

    Returns:
        [type]: [description]
    """
    return (
        db.query(barcode_model.BarcodeDB)
        .filter(barcode_model.BarcodeDB.barcode == barcode_id)
        .first()
    )


def post_barcode(db: Session, barcode_item: barcode_model.Barcode):
    """Adds barcode to the database

    Args:
        db (Session): Database session
        barcode_item (barcode_model.Barcode): Barcode item to be added

    Returns:
        None
    """
    db_item = barcode_model.BarcodeDB(**barcode_item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)


def post_barcodes(db: Session, barcodes: barcode_model.Barcodes):
    """Adds barcodes to the database

    Args:
        db (Session): Database session
        barcodes (barcode_model.Barcodes): Barcodes to be added

    Returns:
        None
    """
    db_items = [barcode_model.BarcodeDB(
        **barcode.dict()) for barcode in barcodes.barcodes]
    db.add_all(db_items)
    db.commit()


def is_barcode_unique(db: Session, barcode_item: barcode_model.Barcode):
    """Checks if barcode unique

    Args:
        db (Session): Database session
        barcode_item (barcode_model.Barcode): Barcode item

    Returns:
        Bool: Returns true if barcode is unique
    """
    return db.query(barcode_model.BarcodeDB).get(barcode_item.barcode) is None


def are_all_barcodes_unique(db: Session, barcodes: barcode_model.Barcodes):
    """Checks if barcode all unique

    Args:
        db (Session): Database session
        barcode_item (barcode_model.Barcodes): Barcodes

    Returns:
        Bool: Returns true if all barcodes are unique
    """

    # Check if input barcodes have duplicates
    barcode_list = [barcode_item.barcode for barcode_item in barcodes.barcodes]

    if len(set(barcode_list)) != len(barcode_list):
        raise HTTPException(
            status_code=400, detail={
                "message": "Duplicate barcodes in input",
                "duplicates": list(set([
                    barcode for barcode in barcode_list if barcode_list.count(barcode) > 1
                ]))
            },
        )

    # Check if input barcodes have duplicates in database
    duplicate_barcodes = []

    for barcode in barcodes.barcodes:
        if db.query(barcode_model.BarcodeDB).get(barcode.barcode) is not None:
            duplicate_barcodes.append(barcode.barcode)

    if duplicate_barcodes:
        raise HTTPException(
            status_code=400, detail={"message": "Barcodes already exists in database", "duplicates": duplicate_barcodes},
        )

    # If all of the barcodes are unique, return True
    return True
