from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.crud.partner import crud_partner, crud_partner_category
from app.schemas.partner import (
    PartnerCreate, PartnerUpdate, PartnerResponse,
    PartnerCategoryCreate, PartnerCategoryUpdate, PartnerCategoryResponse
)

router = APIRouter()


# Partner Category Endpoints
@router.get("/categories/", response_model=List[PartnerCategoryResponse])
def read_partner_categories(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    categories = crud_partner_category.get_multi(db, skip=skip, limit=limit)
    return categories


@router.get("/categories/{category_id}", response_model=PartnerCategoryResponse)
def read_partner_category(
    category_id: UUID,
    db: Session = Depends(get_db)
):
    category = crud_partner_category.get(db, id=category_id)
    if category is None:
        raise HTTPException(status_code=404, detail="Partner category not found")
    return category


@router.post("/categories/", response_model=PartnerCategoryResponse, status_code=201)
def create_partner_category(
    category: PartnerCategoryCreate,
    db: Session = Depends(get_db)
):
    return crud_partner_category.create(db, obj_in=category)


@router.put("/categories/{category_id}", response_model=PartnerCategoryResponse)
def update_partner_category(
    category_id: UUID,
    category: PartnerCategoryUpdate,
    db: Session = Depends(get_db)
):
    db_category = crud_partner_category.get(db, id=category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Partner category not found")
    return crud_partner_category.update(db, db_obj=db_category, obj_in=category)


@router.delete("/categories/{category_id}", response_model=PartnerCategoryResponse)
def delete_partner_category(
    category_id: UUID,
    db: Session = Depends(get_db)
):
    category = crud_partner_category.get(db, id=category_id)
    if category is None:
        raise HTTPException(status_code=404, detail="Partner category not found")
    return crud_partner_category.delete(db, id=category_id)


# Partner Endpoints
@router.get("/", response_model=List[PartnerResponse])
def read_partners(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    partners = crud_partner.get_multi(db, skip=skip, limit=limit)
    return partners


@router.get("/{partner_id}", response_model=PartnerResponse)
def read_partner(
    partner_id: UUID,
    db: Session = Depends(get_db)
):
    partner = crud_partner.get(db, id=partner_id)
    if partner is None:
        raise HTTPException(status_code=404, detail="Partner not found")
    return partner


@router.post("/", response_model=PartnerResponse, status_code=201)
def create_partner(
    partner: PartnerCreate,
    db: Session = Depends(get_db)
):
    return crud_partner.create(db, obj_in=partner)


@router.put("/{partner_id}", response_model=PartnerResponse)
def update_partner(
    partner_id: UUID,
    partner: PartnerUpdate,
    db: Session = Depends(get_db)
):
    db_partner = crud_partner.get(db, id=partner_id)
    if db_partner is None:
        raise HTTPException(status_code=404, detail="Partner not found")
    return crud_partner.update(db, db_obj=db_partner, obj_in=partner)


@router.delete("/{partner_id}", response_model=PartnerResponse)
def delete_partner(
    partner_id: UUID,
    db: Session = Depends(get_db)
):
    partner = crud_partner.get(db, id=partner_id)
    if partner is None:
        raise HTTPException(status_code=404, detail="Partner not found")
    return crud_partner.delete(db, id=partner_id)
