"""
Este modulo sirve para definir los esquemas de los clientes"""
from pydantic import BaseModel
from typing import Optional


class CustomerBase(BaseModel):
    """
    Esta clase sirve para definir los campos de un cliente"""

    name: str
    last_name: str
    dni: Optional[str] = None


class CustomerCreate(CustomerBase):
    """
    Esta clase sirve para crear un cliente"""


class Customer(CustomerBase):
    """
    Esta clase sirve para mostrar los datos de un cliente"""

    id: int

    class Config:
        """
        Esta clase sirve para configurar los esquemas"""

        orm_mode = True
