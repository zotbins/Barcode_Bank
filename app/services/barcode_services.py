from sqlalchemy.orm import Session
from models import barcode_model


def get_barcode(db: Session, barcode_id: str):
    return (
        db.query(barcode_model.BarcodeDB)
        .filter(barcode_model.BarcodeDB.barcode == barcode_id)
        .first()
    )


def post_barcode(db: Session, barcode_item: barcode_model.Barcode):
    db_item = barcode_model.BarcodeDB(**barcode_item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def is_barcode_unique(db: Session, barcode_item: barcode_model.Barcode):
    return db.query(barcode_model.BarcodeDB).get(barcode_item.barcode) is None
