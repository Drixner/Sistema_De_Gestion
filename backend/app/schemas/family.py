"""
Este esquema sirve para definir los esquemas de las familias
"""
from pydantic import BaseModel
from typing import List, Optional


class FamilyBase(BaseModel):
    name: str


class FamilyCreate(FamilyBase):
    pass


class Family(FamilyBase):
    id: int

    class Config:
        orm_mode = True
