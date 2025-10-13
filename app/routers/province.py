from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.crud.location import crud_province
from app.schemas.location import (
    MasterProvinceCreate, MasterProvinceUpdate, MasterProvinceResponse
)

router = APIRouter()


@router.get("/", response_model=List[MasterProvinceResponse])
def read_provinces(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    return crud_province.get_multi(db, skip=skip, limit=limit)


@router.get("/{province_id}", response_model=MasterProvinceResponse)
def read_province(
    province_id: UUID,
    db: Session = Depends(get_db)
):
    province = crud_province.get(db, id=province_id)
    if province is None:
        raise HTTPException(status_code=404, detail="Province not found")
    return province


@router.post("/", response_model=MasterProvinceResponse, status_code=201)
def create_province(
    province: MasterProvinceCreate,
    db: Session = Depends(get_db)
):
    return crud_province.create(db, obj_in=province)


@router.put("/{province_id}", response_model=MasterProvinceResponse)
def update_province(
    province_id: UUID,
    province: MasterProvinceUpdate,
    db: Session = Depends(get_db)
):
    db_province = crud_province.get(db, id=province_id)
    if db_province is None:
        raise HTTPException(status_code=404, detail="Province not found")
    return crud_province.update(db, db_obj=db_province, obj_in=province)


@router.delete("/{province_id}", response_model=MasterProvinceResponse)
def delete_province(
    province_id: UUID,
    db: Session = Depends(get_db)
):
    province = crud_province.get(db, id=province_id)
    if province is None:
        raise HTTPException(status_code=404, detail="Province not found")
    return crud_province.delete(db, id=province_id)
