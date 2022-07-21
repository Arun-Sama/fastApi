from pydantic import BaseModel
from typing import Optional


class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None

    class Config:
        orm_mode = True


class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    brand: Optional[str] = None

    class Config:
        orm_mode = True


inventory = {}
