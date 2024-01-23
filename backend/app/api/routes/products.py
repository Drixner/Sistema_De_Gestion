"""
Define las rutas de la API para los productos, incluyendo la creación y lectura de productos.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import models, schemas, database

router = APIRouter()


@router.post("/{category}/")
def create_product(
    category: str,
    product: schemas.ProductCreate,
    db: Session = Depends(database.get_db),
):
    """
    Crea un nuevo producto en la base de datos."""
    db_product = models.Product(**product.dict(), category=category)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


@router.get("/{category}/")
def read_products(category: str, db: Session = Depends(database.get_db)):
    """
    Obtiene todos los productos de la base de datos."""
    products = (
        db.query(models.Product).filter(models.Product.category == category).all()
    )
    return products
