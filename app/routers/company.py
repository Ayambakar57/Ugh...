from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud.company import crud_company, crud_company_category
from app.schemas.company import (
    CompanyCreate, CompanyUpdate, CompanyResponse,
    CompanyCategoryCreate, CompanyCategoryUpdate, CompanyCategoryResponse
)

router = APIRouter()


@router.get("/", response_model=List[CompanyResponse])
def read_companies(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    companies = crud_company.get_multi(db, skip=skip, limit=limit)
    return companies

@router.get("/{company_id}", response_model=CompanyResponse)
def read_company(
    company_id: UUID,
    db: Session = Depends(get_db)
):
    company = crud_company.get(db, id=company_id)
    if company is None:
        raise HTTPException(status_code=404, detail="Company not found")
    return company

@router.post("/", response_model=CompanyResponse, status_code=201)
def create_company(
    company: CompanyCreate,
    db: Session = Depends(get_db)
):
    return crud_company.create(db, obj_in=company)

@router.put("/{company_id}", response_model=CompanyResponse)
def update_company(
    company_id: UUID,
    company: CompanyUpdate,
    db: Session = Depends(get_db)
):
    db_company = crud_company.get(db, id=company_id)
    if db_company is None:
        raise HTTPException(status_code=404, detail="Company not found")
    return crud_company.update(db, db_obj=db_company, obj_in=company)

@router.delete("/{company_id}", response_model=CompanyResponse)
def delete_company(
    company_id: UUID,
    db: Session = Depends(get_db)
):
    company = crud_company.get(db, id=company_id)
    if company is None:
        raise HTTPException(status_code=404, detail="Company not found")
    return crud_company.delete(db, id=company_id)


# Company Category Endpoints (Specific routes AFTER general routes)
@router.get("/categories/", response_model=List[CompanyCategoryResponse])
def read_company_categories(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    categories = crud_company_category.get_multi(db, skip=skip, limit=limit)
    return categories

@router.get("/categories/{category_id}", response_model=CompanyCategoryResponse)
def read_company_category(
    category_id: UUID,
    db: Session = Depends(get_db)
):
    category = crud_company_category.get(db, id=category_id)
    if category is None:
        raise HTTPException(status_code=404, detail="Company category not found")
    return category

@router.post("/categories/", response_model=CompanyCategoryResponse, status_code=201)
def create_company_category(
    category: CompanyCategoryCreate,
    db: Session = Depends(get_db)
):
    return crud_company_category.create(db, obj_in=category)

@router.put("/categories/{category_id}", response_model=CompanyCategoryResponse)
def update_company_category(
    category_id: UUID,
    category: CompanyCategoryUpdate,
    db: Session = Depends(get_db)
):
    db_category = crud_company_category.get(db, id=category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Company category not found")
    return crud_company_category.update(db, db_obj=db_category, obj_in=category)

@router.delete("/categories/{category_id}", response_model=CompanyCategoryResponse)
def delete_company_category(
    category_id: UUID,
    db: Session = Depends(get_db)
):
    category = crud_company_category.get(db, id=category_id)
    if category is None:
        raise HTTPException(status_code=404, detail="Company category not found")
    return crud_company_category.delete(db, id=category_id)