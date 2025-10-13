from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.crud.location import crud_ward
from app.schemas.location import (
    MasterWardCreate, MasterWardUpdate, MasterWardResponse
)

router = APIRouter()


@router.get("/", response_model=List[MasterWardResponse])
def read_wards(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    return crud_ward.get_multi(db, skip=skip, limit=limit)


@router.get("/{ward_id}", response_model=MasterWardResponse)
def read_ward(
    ward_id: UUID,
    db: Session = Depends(get_db)
):
    ward = crud_ward.get(db, id=ward_id)
    if ward is None:
        raise HTTPException(status_code=404, detail="Ward not found")
    return ward


@router.post("/", response_model=MasterWardResponse, status_code=201)
def create_ward(
    ward: MasterWardCreate,
    db: Session = Depends(get_db)
):
    return crud_ward.create(db, obj_in=ward)


@router.put("/{ward_id}", response_model=MasterWardResponse)
def update_ward(
    ward_id: UUID,
    ward: MasterWardUpdate,
    db: Session = Depends(get_db)
):
    db_ward = crud_ward.get(db, id=ward_id)
    if db_ward is None:
        raise HTTPException(status_code=404, detail="Ward not found")
    return crud_ward.update(db, db_obj=db_ward, obj_in=ward)


@router.delete("/{ward_id}", response_model=MasterWardResponse)
def delete_ward(
    ward_id: UUID,
    db: Session = Depends(get_db)
):
    ward = crud_ward.get(db, id=ward_id)
    if ward is None:
        raise HTTPException(status_code=404, detail="Ward not found")
    return crud_ward.delete(db, id=ward_id)
