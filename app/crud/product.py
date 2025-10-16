from typing import List, Optional
from uuid import UUID
from datetime import datetime

from sqlalchemy.orm import Session, joinedload

from app.crud.base import CRUDBase
from app.models.product import Product, ProductCategory
from app.schemas.product import (
    ProductCreate, ProductUpdate,
    ProductCategoryCreate, ProductCategoryUpdate
)


class CRUDProduct(CRUDBase[Product, ProductCreate, ProductUpdate]):
    def get(self, db: Session, id: UUID) -> Optional[Product]:
        return db.query(self.model).options(
            joinedload(self.model.category),
            joinedload(self.model.branch),
            joinedload(self.model.warehouse)
        ).filter(
            self.model.id == id,
            self.model.deleted_at == None
        ).first()
    
    def get_multi(
        self, db: Session, *, skip: int = 0, limit: int = 100
    ) -> List[Product]:
        return db.query(self.model).options(
            joinedload(self.model.category),
            joinedload(self.model.branch),
            joinedload(self.model.warehouse)
        ).filter(
            self.model.deleted_at == None
        ).offset(skip).limit(limit).all()
    
    def delete(self, db: Session, *, id: UUID) -> Product:
        obj = db.query(self.model).get(id)
        obj.deleted_at = datetime.now()
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj


class CRUDProductCategory(CRUDBase[ProductCategory, ProductCategoryCreate, ProductCategoryUpdate]):
    def get(self, db: Session, id: UUID) -> Optional[ProductCategory]:
        return db.query(self.model).filter(
            self.model.id == id,
            self.model.deleted_at == None
        ).first()
    
    def get_multi(
        self, db: Session, *, skip: int = 0, limit: int = 100
    ) -> List[ProductCategory]:
        return db.query(self.model).filter(
            self.model.deleted_at == None
        ).offset(skip).limit(limit).all()
    
    def delete(self, db: Session, *, id: UUID) -> ProductCategory:
        obj = db.query(self.model).get(id)
        obj.deleted_at = datetime.now()
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj


crud_product = CRUDProduct(Product)
crud_product_category = CRUDProductCategory(ProductCategory)
