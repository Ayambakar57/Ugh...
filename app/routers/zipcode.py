from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.crud.location import crud_zipcode
from app.schemas.location import (
    MasterZipcodeCreate, MasterZipcodeUpdate, MasterZipcodeResponse
)

router = APIRouter()


@router.get("/", response_model=List[MasterZipcodeResponse])
def read_zipcodes(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    return crud_zipcode.get_multi(db, skip=skip, limit=limit)


@router.get("/{zipcode_id}", response_model=MasterZipcodeResponse)
def read_zipcode(
    zipcode_id: UUID,
    db: Session = Depends(get_db)
):
    zipcode = crud_zipcode.get(db, id=zipcode_id)
    if zipcode is None:
        raise HTTPException(status_code=404, detail="Zipcode not found")
    return zipcode


@router.post("/", response_model=MasterZipcodeResponse, status_code=201)
def create_zipcode(
    zipcode: MasterZipcodeCreate,
    db: Session = Depends(get_db)
):
    return crud_zipcode.create(db, obj_in=zipcode)


@router.put("/{zipcode_id}", response_model=MasterZipcodeResponse)
def update_zipcode(
    zipcode_id: UUID,
    zipcode: MasterZipcodeUpdate,
    db: Session = Depends(get_db)
):
    db_zipcode = crud_zipcode.get(db, id=zipcode_id)
    if db_zipcode is None:
        raise HTTPException(status_code=404, detail="Zipcode not found")
    return crud_zipcode.update(db, db_obj=db_zipcode, obj_in=zipcode)


@router.delete("/{zipcode_id}", response_model=MasterZipcodeResponse)
def delete_zipcode(
    zipcode_id: UUID,
    db: Session = Depends(get_db)
):
    zipcode = crud_zipcode.get(db, id=zipcode_id)
    if zipcode is None:
        raise HTTPException(status_code=404, detail="Zipcode not found")
    return crud_zipcode.delete(db, id=zipcode_id)
