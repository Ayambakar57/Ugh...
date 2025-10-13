from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.crud.product import crud_product, crud_product_category
from app.schemas.product import (
    ProductCreate, ProductUpdate, ProductResponse,
    ProductCategoryCreate, ProductCategoryUpdate, ProductCategoryResponse
)

router = APIRouter()


# Product Category Endpoints
@router.get("/categories/", response_model=List[ProductCategoryResponse])
def read_product_categories(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    categories = crud_product_category.get_multi(db, skip=skip, limit=limit)
    return categories


@router.get("/categories/{category_id}", response_model=ProductCategoryResponse)
def read_product_category(
    category_id: UUID,
    db: Session = Depends(get_db)
):
    category = crud_product_category.get(db, id=category_id)
    if category is None:
        raise HTTPException(status_code=404, detail="Product category not found")
    return category


@router.post("/categories/", response_model=ProductCategoryResponse, status_code=201)
def create_product_category(
    category: ProductCategoryCreate,
    db: Session = Depends(get_db)
):
    return crud_product_category.create(db, obj_in=category)


@router.put("/categories/{category_id}", response_model=ProductCategoryResponse)
def update_product_category(
    category_id: UUID,
    category: ProductCategoryUpdate,
    db: Session = Depends(get_db)
):
    db_category = crud_product_category.get(db, id=category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Product category not found")
    return crud_product_category.update(db, db_obj=db_category, obj_in=category)


@router.delete("/categories/{category_id}", response_model=ProductCategoryResponse)
def delete_product_category(
    category_id: UUID,
    db: Session = Depends(get_db)
):
    category = crud_product_category.get(db, id=category_id)
    if category is None:
        raise HTTPException(status_code=404, detail="Product category not found")
    return crud_product_category.delete(db, id=category_id)


# Product Endpoints
@router.get("/", response_model=List[ProductResponse])
def read_products(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    products = crud_product.get_multi(db, skip=skip, limit=limit)
    return products


@router.get("/{product_id}", response_model=ProductResponse)
def read_product(
    product_id: UUID,
    db: Session = Depends(get_db)
):
    product = crud_product.get(db, id=product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.post("/", response_model=ProductResponse, status_code=201)
def create_product(
    product: ProductCreate,
    db: Session = Depends(get_db)
):
    return crud_product.create(db, obj_in=product)


@router.put("/{product_id}", response_model=ProductResponse)
def update_product(
    product_id: UUID,
    product: ProductUpdate,
    db: Session = Depends(get_db)
):
    db_product = crud_product.get(db, id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return crud_product.update(db, db_obj=db_product, obj_in=product)


@router.delete("/{product_id}", response_model=ProductResponse)
def delete_product(
    product_id: UUID,
    db: Session = Depends(get_db)
):
    product = crud_product.get(db, id=product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return crud_product.delete(db, id=product_id)
