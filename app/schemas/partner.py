from pydantic import BaseModel, ConfigDict
from uuid import UUID
from datetime import datetime
from typing import Optional


# PartnerCategory Schemas
class PartnerCategoryBase(BaseModel):
    code_id: str
    name: str
    note: str


class PartnerCategoryCreate(PartnerCategoryBase):
    pass


class PartnerCategoryUpdate(BaseModel):
    code_id: Optional[str] = None
    name: Optional[str] = None
    note: Optional[str] = None


class PartnerCategoryResponse(PartnerCategoryBase):
    id: UUID
    created_at: datetime
    updated_at: datetime
    
    model_config = ConfigDict(from_attributes=True)


# Partner Schemas
class PartnerBase(BaseModel):
    code_id: str
    branch_id: UUID
    warehouse_id: UUID
    name: str
    category_id: UUID
    description: str
    province_id: Optional[UUID] = None
    district_id: Optional[UUID] = None
    subdistrict_id: Optional[UUID] = None
    ward_id: Optional[UUID] = None
    address: Optional[str] = None
    pic_name: Optional[str] = None
    pic_contact: Optional[str] = None
    note: Optional[str] = None


class PartnerCreate(PartnerBase):
    pass


class PartnerUpdate(BaseModel):
    code_id: Optional[str] = None
    branch_id: Optional[UUID] = None
    warehouse_id: Optional[UUID] = None
    name: Optional[str] = None
    category_id: Optional[UUID] = None
    description: Optional[str] = None
    province_id: Optional[UUID] = None
    district_id: Optional[UUID] = None
    subdistrict_id: Optional[UUID] = None
    ward_id: Optional[UUID] = None
    address: Optional[str] = None
    pic_name: Optional[str] = None
    pic_contact: Optional[str] = None
    note: Optional[str] = None


class PartnerResponse(PartnerBase):
    id: UUID
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    
    model_config = ConfigDict(from_attributes=True)
