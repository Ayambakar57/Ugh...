from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.crud.location import crud_district
from app.schemas.location import (
    MasterDistrictCreate, MasterDistrictUpdate, MasterDistrictResponse
)

router = APIRouter()





@router.get("/{district_id}", response_model=MasterDistrictResponse)
def read_district(
    district_id: UUID,
    db: Session = Depends(get_db)
):
    district = crud_district.get(db, id=district_id)
    if district is None:
        raise HTTPException(status_code=404, detail="District not found")
    return district

@router.get("/", response_model=List[MasterDistrictResponse])
def read_districts(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    return crud_district.get_multi(db, skip=skip, limit=limit)
    
@router.post("/", response_model=MasterDistrictResponse, status_code=201)
def create_district(
    district: MasterDistrictCreate,
    db: Session = Depends(get_db)
):
    return crud_district.create(db, obj_in=district)


@router.put("/{district_id}", response_model=MasterDistrictResponse)
def update_district(
    district_id: UUID,
    district: MasterDistrictUpdate,
    db: Session = Depends(get_db)
):
    db_district = crud_district.get(db, id=district_id)
    if db_district is None:
        raise HTTPException(status_code=404, detail="District not found")
    return crud_district.update(db, db_obj=db_district, obj_in=district)


@router.delete("/{district_id}", response_model=MasterDistrictResponse)
def delete_district(
    district_id: UUID,
    db: Session = Depends(get_db)
):
    district = crud_district.get(db, id=district_id)
    if district is None:
        raise HTTPException(status_code=404, detail="District not found")
    return crud_district.delete(db, id=district_id)
