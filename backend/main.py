"""
Este modulo sirve para definir las rutas de los productos"""

from fastapi import FastAPI
from app.routers import products

app = FastAPI()

app.include_router(products.router)
