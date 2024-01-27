"""
Este esquema sirve para definir los esquemas de las familias
"""
from typing import Optional
from pydantic import BaseModel


class FamilyBase(BaseModel):
    name: str


class FamilyCreate(FamilyBase):
    pass


class Family(FamilyBase):
    id: int

    class Config:
        orm_mode = True
