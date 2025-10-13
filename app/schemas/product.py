from pydantic import BaseModel, ConfigDict
from uuid import UUID
from datetime import datetime
from typing import Optional


# ProductCategory Schemas
class ProductCategoryBase(BaseModel):
    code_id: str
    name: str
    note: str


class ProductCategoryCreate(ProductCategoryBase):
    pass


class ProductCategoryUpdate(BaseModel):
    code_id: Optional[str] = None
    name: Optional[str] = None
    note: Optional[str] = None


class ProductCategoryResponse(ProductCategoryBase):
    id: UUID
    created_at: datetime
    updated_at: datetime
    
    model_config = ConfigDict(from_attributes=True)


# Product Schemas
class ProductBase(BaseModel):
    code_id: str
    warehouse_id: UUID
    branch_id: UUID
    name: str
    category_id: UUID
    description: str
    note: Optional[str] = None


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    code_id: Optional[str] = None
    warehouse_id: Optional[UUID] = None
    branch_id: Optional[UUID] = None
    name: Optional[str] = None
    category_id: Optional[UUID] = None
    description: Optional[str] = None
    note: Optional[str] = None


class ProductResponse(ProductBase):
    id: UUID
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    
    model_config = ConfigDict(from_attributes=True)
