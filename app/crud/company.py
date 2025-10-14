from typing import List, Optional
from uuid import UUID
from datetime import datetime

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.company import Company, CompanyCategory
from app.schemas.company import (
    CompanyCreate, CompanyUpdate,
    CompanyCategoryCreate, CompanyCategoryUpdate
)


class CRUDCompany(CRUDBase[Company, CompanyCreate, CompanyUpdate]):
    def get(self, db: Session, id: UUID) -> Optional[Company]:
        return db.query(self.model).filter(
            self.model.id == id,
            self.model.deleted_at == None
        ).first()
    
    def get_multi(
        self, db: Session, *, skip: int = 0, limit: int = 100
    ) -> List[Company]:
        return db.query(self.model).filter(
            self.model.deleted_at == None
        ).offset(skip).limit(limit).all()
    
    def delete(self, db: Session, *, id: UUID) -> Company:
        obj = db.query(self.model).get(id)
        obj.deleted_at = datetime.now()
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj


class CRUDCompanyCategory(CRUDBase[CompanyCategory, CompanyCategoryCreate, CompanyCategoryUpdate]):
    def get(self, db: Session, id: UUID) -> Optional[CompanyCategory]:
        return db.query(self.model).filter(
            self.model.id == id,
            self.model.deleted_at == None
        ).first()
    
    def get_multi(
        self, db: Session, *, skip: int = 0, limit: int = 100
    ) -> List[CompanyCategory]:
        return db.query(self.model).filter(
            self.model.deleted_at == None
        ).offset(skip).limit(limit).all()
    
    def delete(self, db: Session, *, id: UUID) -> CompanyCategory:
        obj = db.query(self.model).get(id)
        obj.deleted_at = datetime.now()
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj


crud_company = CRUDCompany(Company)
crud_company_category = CRUDCompanyCategory(CompanyCategory)
