"""SQLAlchemy & Pydantic barcode models"""

from typing import List
from enum import Enum
from pydantic import BaseModel, constr
from sqlalchemy import Column, VARCHAR, String

from services.database import Base


class Bin(str, Enum):
    """Bin type enumeration"""

    landfill = "Landfill"
    recycle = "Recycle"
    compost = "Compost"


class Barcode(BaseModel):
    """Pydantic barcode model"""

    barcode: constr(max_length=13)
    item: str
    bin: Bin

    class Config:
        """Pydantic config class"""

        orm_mode = True
        schema_extra = {
            "example": {
                "barcode": "12000009105",
                "item": "10200774 - MUG ROOT BEER",
                "bin": "Recycle",
            }
        }

class Barcodes(BaseModel):
    """List of barcodes"""
    barcodes: List[Barcode]


class BarcodeDB(Base):
    """SQLAlchemy barcode model"""

    __tablename__ = "barcodes"

    barcode = Column(VARCHAR(13), primary_key=True)
    item = Column(String)
    bin = Column(VARCHAR(8), nullable=False)
