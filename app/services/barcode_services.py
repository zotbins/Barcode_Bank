"""Barcode services to query the database"""
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


def is_barcode_unique(db: Session, barcode_item: barcode_model.Barcode):
    """Checks if barcode unique

    Args:
        db (Session): Database session
        barcode_item (barcode_model.Barcode): Barcode item

    Returns:
        Bool: Returns true if barcode is unique
    """
    return db.query(barcode_model.BarcodeDB).get(barcode_item.barcode) is None
