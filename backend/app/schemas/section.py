"""
Este modelo sirve para definir los esquemas de las secciones"""
from pydantic import BaseModel
from typing import List, Optional


class SectionBase(BaseModel):
    name: str


class SectionCreate(SectionBase):
    pass


class Section(SectionBase):
    id: int

    class Config:
        orm_mode = True
