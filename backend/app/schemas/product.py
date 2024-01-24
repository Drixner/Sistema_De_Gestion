"""
Este modulo sirve para definir los esquemas de los productos"""
from typing import Optional
from pydantic import BaseModel


class ProductBase(BaseModel):
    """
    Esta clase sirve para definir los campos de un producto"""

    description: str
    stock: int
    purchase_price: float
    sale_price: float
    margin: float
    ean_code: Optional[str] = None


class ProductCreate(ProductBase):
    """
    Esta clase sirve para crear un producto"""


class Product(ProductBase):
    """
    Esta clase sirve para mostrar los datos de un producto"""

    id: int
    family_id: int

    class Config:
        """
        Esta clase sirve para configurar los esquemas
        """

        orm_mode = True
