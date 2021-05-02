from pydantic import BaseModel, constr
from enum import Enum
from sqlalchemy import Column, VARCHAR, String

from services.database import Base


class Bin(str, Enum):
    landfill = "Landfill"
    recycle = "Recycle"
    compost = "Compost"


class Barcode(BaseModel):
    barcode: constr(max_length=13)
    item: str
    bin: Bin

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "barcode": "12000009105",
                "item": "10200774 - MUG ROOT BEER",
                "bin": "Recycle",
            }
        }


class BarcodeResponse(BaseModel):
    message: str
    data: Barcode


class BarcodeDB(Base):
    __tablename__ = "barcodes"

    barcode = Column(VARCHAR(13), primary_key=True)
    item = Column(String)
    bin = Column(VARCHAR(8), nullable=False)
