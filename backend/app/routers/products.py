"""
Este modulo sirve para definir las rutas de los productos"""
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..schemas.product import Product, ProductCreate
from ..schemas.family import Family, FamilyCreate
from ..schemas.section import Section, SectionCreate

from ..db.database import SessionLocal
from ..db.models import (
    Product as DBProduct,
    Family as DBFamily,
    Section as DBSection,
)


router = APIRouter()


def get_db():
    """
    Función que retorna la base de datos"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=Product)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    """
    Ruta que crea un producto"""

    db_product = DBProduct(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


@router.get("/", response_model=List[Product])
def read_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Ruta que retorna todos los productos"""
    products = db.query(DBProduct).offset(skip).limit(limit).all()
    return products


@router.get("/{product_id}", response_model=Product)
def read_product(product_id: int, db: Session = Depends(get_db)):
    """
    Ruta que retorna un producto
    """
    product = db.query(DBProduct).filter(DBProduct.id == product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.put("/{product_id}", response_model=Product)
def update_product(
    product_id: int, product: ProductCreate, db: Session = Depends(get_db)
):
    """
    Ruta que actualiza un producto"""
    db_product = db.query(DBProduct).filter(DBProduct.id == product_id).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    for key, value in product.dict().items():
        setattr(db_product, key, value)
    db.commit()
    db.refresh(db_product)
    return db_product


@router.delete("/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    """
    Ruta que elimina un producto"""
    db_product = db.query(DBProduct).filter(DBProduct.id == product_id).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(db_product)
    db.commit()
    return {"detail": "Product deleted"}


# Rutas para familias:
# Compare this snippet from backend/app/routers/products.py:


@router.post("/families/", response_model=Family)
def create_family(family: FamilyCreate, db: Session = Depends(get_db)):
    """
    Ruta que crea una familia"""
    db_family = DBFamily(**family.dict())
    db.add(db_family)
    db.commit()
    db.refresh(db_family)
    return db_family


@router.get("/families/{family_id}", response_model=Family)
def read_family(family_id: int, db: Session = Depends(get_db)):
    """
    Ruta que retorna una familia"""
    db_family = db.query(DBFamily).filter(DBFamily.id == family_id).first()
    if db_family is None:
        raise HTTPException(status_code=404, detail="Family not found")
    return db_family


@router.put("/families/{family_id}", response_model=Family)
def update_family(family_id: int, family: FamilyCreate, db: Session = Depends(get_db)):
    """
    Ruta que actualiza una familia"""
    db_family = db.query(DBFamily).filter(DBFamily.id == family_id).first()
    if db_family is None:
        raise HTTPException(status_code=404, detail="Family not found")
    for key, value in family.dict().items():
        setattr(db_family, key, value)
    db.commit()
    db.refresh(db_family)
    return db_family


@router.delete("/families/{family_id}")
def delete_family(family_id: int, db: Session = Depends(get_db)):
    """
    Ruta que elimina una familia"""
    db_family = db.query(DBFamily).filter(DBFamily.id == family_id).first()
    if db_family is None:
        raise HTTPException(status_code=404, detail="Family not found")
    db.delete(db_family)
    db.commit()
    return {"detail": "Family deleted"}


# Rutas para secciones:
# Compare this snippet from backend/app/routers/products.py:


@router.post("/sections/", response_model=Section)
def create_section(section: SectionCreate, db: Session = Depends(get_db)):
    """
    Ruta que crea una sección"""
    db_section = DBSection(**section.dict())
    db.add(db_section)
    db.commit()
    db.refresh(db_section)
    return db_section


@router.get("/sections/{section_id}", response_model=Section)
def read_section(section_id: int, db: Session = Depends(get_db)):
    """
    Ruta que retorna una sección"""
    db_section = db.query(DBSection).filter(DBSection.id == section_id).first()
    if db_section is None:
        raise HTTPException(status_code=404, detail="Section not found")
    return db_section


@router.put("/sections/{section_id}", response_model=Section)
def update_section(
    section_id: int, section: SectionCreate, db: Session = Depends(get_db)
):
    """
    Ruta que actualiza una sección"""
    db_section = db.query(DBSection).filter(DBSection.id == section_id).first()
    if db_section is None:
        raise HTTPException(status_code=404, detail="Section not found")
    for key, value in section.dict().items():
        setattr(db_section, key, value)
    db.commit()
    db.refresh(db_section)
    return db_section


@router.delete("/sections/{section_id}")
def delete_section(section_id: int, db: Session = Depends(get_db)):
    """
    Ruta que elimina una sección"""
    db_section = db.query(DBSection).filter(DBSection.id == section_id).first()
    if db_section is None:
        raise HTTPException(status_code=404, detail="Section not found")
    db.delete(db_section)
    db.commit()
    return {"detail": "Section deleted"}
