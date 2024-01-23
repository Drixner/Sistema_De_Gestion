"""
Define los modelos de la base de datos."""

from sqlalchemy import Column, Integer, String, ForeignKey, Table, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Esta es la tabla de asociación para la relación muchos a muchos
product_provider_association = Table(
    "product_provider",
    Base.metadata,
    Column("product_id", Integer, ForeignKey("products.id")),
    Column("provider_id", Integer, ForeignKey("providers.id")),
)


class Section(Base):
    """
    Define la tabla de secciones."""

    __tablename__ = "sections"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    families = relationship("Family", back_populates="section")


class Family(Base):
    """
    Define la tabla de familias."""

    __tablename__ = "families"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    section_id = Column(Integer, ForeignKey("sections.id"))
    section = relationship("Section", back_populates="families")


class Provider(Base):
    """
    Define la tabla de proveedores."""

    __tablename__ = "providers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    products = relationship("Product", secondary=product_provider_association)


class Product(Base):
    """
    Define la tabla de productos."""

    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, index=True)
    stock = Column(Integer)
    purchase_price = Column(Float)
    sale_price = Column(Float)
    margin = Column(Float)
    ean_code = Column(String, index=True)
    family_id = Column(Integer, ForeignKey("families.id"))

    family = relationship("Family")
    providers = relationship("Provider", secondary=product_provider_association)
