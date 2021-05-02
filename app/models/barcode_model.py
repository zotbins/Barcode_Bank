from pydantic import BaseModel, constr
from enum import Enum


class Bin(str, Enum):
    landfill = "Landfill"
    recycle = "Recycle"
    compost = "Compost"


class Barcode(BaseModel):
    barcode: constr(max_length=13)
    item: str
    bin: Bin

    class Config:
        schema_extra = {
            "example": {
                "barcode": "12000009105",
                "item": "10200774 - MUG ROOT BEER",
                "bin": "Recycle",
            }
        }
