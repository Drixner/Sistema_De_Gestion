"""
Este modulo sirve para definir los esquemas de los empleados"""

from pydantic import BaseModel
from typing import Optional


class EmployeeBase(BaseModel):
    """
    Esta clase sirve para definir los campos de un empleado"""

    name: str
    last_name: str


class EmployeeCreate(EmployeeBase):
    """
    Este clase sirve para crear un empleado"""


class Employee(EmployeeBase):
    """
    Esta clasr sirve para mostrar los datos de un empleado"""

    id: int

    class Config:
        """
        Esta clase sirve para configurar los esquemas"""

        orm_mode = True
