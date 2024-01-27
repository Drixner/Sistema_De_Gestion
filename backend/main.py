"""
Este modulo sirve para definir las rutas de los productos"""

from fastapi import FastAPI
from app.routers import products
from app.db.database import Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(products.router)
