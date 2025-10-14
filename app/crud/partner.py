from typing import List, Optional
from uuid import UUID
from datetime import datetime

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.partner import Partner, PartnerCategory
from app.schemas.partner import (
    PartnerCreate, PartnerUpdate,
    PartnerCategoryCreate, PartnerCategoryUpdate
)


class CRUDPartner(CRUDBase[Partner, PartnerCreate, PartnerUpdate]):
    def get(self, db: Session, id: UUID) -> Optional[Partner]:
        return db.query(self.model).filter(
            self.model.id == id,
            self.model.deleted_at == None
        ).first()
    
    def get_multi(
        self, db: Session, *, skip: int = 0, limit: int = 100
    ) -> List[Partner]:
        return db.query(self.model).filter(
            self.model.deleted_at == None
        ).offset(skip).limit(limit).all()
    
    def delete(self, db: Session, *, id: UUID) -> Partner:
        obj = db.query(self.model).get(id)
        obj.deleted_at = datetime.now()
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj


class CRUDPartnerCategory(CRUDBase[PartnerCategory, PartnerCategoryCreate, PartnerCategoryUpdate]):
    def get(self, db: Session, id: UUID) -> Optional[PartnerCategory]:
        return db.query(self.model).filter(
            self.model.id == id,
            self.model.deleted_at == None
        ).first()
    
    def get_multi(
        self, db: Session, *, skip: int = 0, limit: int = 100
    ) -> List[PartnerCategory]:
        return db.query(self.model).filter(
            self.model.deleted_at == None
        ).offset(skip).limit(limit).all()
    
    def delete(self, db: Session, *, id: UUID) -> PartnerCategory:
        obj = db.query(self.model).get(id)
        obj.deleted_at = datetime.now()
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj


crud_partner = CRUDPartner(Partner)
crud_partner_category = CRUDPartnerCategory(PartnerCategory)
