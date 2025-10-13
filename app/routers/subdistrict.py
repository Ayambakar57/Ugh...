from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.crud.location import crud_subdistrict
from app.schemas.location import (
    MasterSubdistrictCreate, MasterSubdistrictUpdate, MasterSubdistrictResponse
)

router = APIRouter()


@router.get("/", response_model=List[MasterSubdistrictResponse])
def read_subdistricts(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    return crud_subdistrict.get_multi(db, skip=skip, limit=limit)


@router.get("/{subdistrict_id}", response_model=MasterSubdistrictResponse)
def read_subdistrict(
    subdistrict_id: UUID,
    db: Session = Depends(get_db)
):
    subdistrict = crud_subdistrict.get(db, id=subdistrict_id)
    if subdistrict is None:
        raise HTTPException(status_code=404, detail="Subdistrict not found")
    return subdistrict


@router.post("/", response_model=MasterSubdistrictResponse, status_code=201)
def create_subdistrict(
    subdistrict: MasterSubdistrictCreate,
    db: Session = Depends(get_db)
):
    return crud_subdistrict.create(db, obj_in=subdistrict)


@router.put("/{subdistrict_id}", response_model=MasterSubdistrictResponse)
def update_subdistrict(
    subdistrict_id: UUID,
    subdistrict: MasterSubdistrictUpdate,
    db: Session = Depends(get_db)
):
    db_subdistrict = crud_subdistrict.get(db, id=subdistrict_id)
    if db_subdistrict is None:
        raise HTTPException(status_code=404, detail="Subdistrict not found")
    return crud_subdistrict.update(db, db_obj=db_subdistrict, obj_in=subdistrict)


@router.delete("/{subdistrict_id}", response_model=MasterSubdistrictResponse)
def delete_subdistrict(
    subdistrict_id: UUID,
    db: Session = Depends(get_db)
):
    subdistrict = crud_subdistrict.get(db, id=subdistrict_id)
    if subdistrict is None:
        raise HTTPException(status_code=404, detail="Subdistrict not found")
    return crud_subdistrict.delete(db, id=subdistrict_id)
