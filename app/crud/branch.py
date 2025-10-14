from typing import List, Optional
from uuid import UUID
from datetime import datetime

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.branch import Branch
from app.schemas.branch import BranchCreate, BranchUpdate


class CRUDBranch(CRUDBase[Branch, BranchCreate, BranchUpdate]):
    def get(self, db: Session, id: UUID) -> Optional[Branch]:
        return db.query(self.model).filter(
            self.model.id == id,
            self.model.deleted_at == None
        ).first()
    
    def get_multi(
        self, db: Session, *, skip: int = 0, limit: int = 100
    ) -> List[Branch]:
        return db.query(self.model).filter(
            self.model.deleted_at == None
        ).offset(skip).limit(limit).all()
    
    def delete(self, db: Session, *, id: UUID) -> Branch:
        obj = db.query(self.model).get(id)
        obj.deleted_at = datetime.now()
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj


crud_branch = CRUDBranch(Branch)
