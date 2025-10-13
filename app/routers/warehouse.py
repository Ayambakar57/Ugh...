from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.crud.warehouse import crud_warehouse
from app.schemas.warehouse import WarehouseCreate, WarehouseUpdate, WarehouseResponse

router = APIRouter()


@router.get("/", response_model=List[WarehouseResponse])
def read_warehouses(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    warehouses = crud_warehouse.get_multi(db, skip=skip, limit=limit)
    return warehouses


@router.get("/{warehouse_id}", response_model=WarehouseResponse)
def read_warehouse(
    warehouse_id: UUID,
    db: Session = Depends(get_db)
):
    warehouse = crud_warehouse.get(db, id=warehouse_id)
    if warehouse is None:
        raise HTTPException(status_code=404, detail="Warehouse not found")
    return warehouse


@router.post("/", response_model=WarehouseResponse, status_code=201)
def create_warehouse(
    warehouse: WarehouseCreate,
    db: Session = Depends(get_db)
):
    return crud_warehouse.create(db, obj_in=warehouse)


@router.put("/{warehouse_id}", response_model=WarehouseResponse)
def update_warehouse(
    warehouse_id: UUID,
    warehouse: WarehouseUpdate,
    db: Session = Depends(get_db)
):
    db_warehouse = crud_warehouse.get(db, id=warehouse_id)
    if db_warehouse is None:
        raise HTTPException(status_code=404, detail="Warehouse not found")
    return crud_warehouse.update(db, db_obj=db_warehouse, obj_in=warehouse)


@router.delete("/{warehouse_id}", response_model=WarehouseResponse)
def delete_warehouse(
    warehouse_id: UUID,
    db: Session = Depends(get_db)
):
    warehouse = crud_warehouse.get(db, id=warehouse_id)
    if warehouse is None:
        raise HTTPException(status_code=404, detail="Warehouse not found")
    return crud_warehouse.delete(db, id=warehouse_id)
