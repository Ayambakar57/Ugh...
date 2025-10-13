from pydantic import BaseModel, ConfigDict
from uuid import UUID
from datetime import datetime
from typing import Optional


class WarehouseBase(BaseModel):
    code_id: str
    branch_id: UUID
    name: str
    description: str
    province_id: Optional[UUID] = None
    district_id: Optional[UUID] = None
    subdistrict_id: Optional[UUID] = None
    ward_id: Optional[UUID] = None
    address: Optional[str] = None
    pic_name: Optional[str] = None
    pic_contact: Optional[str] = None
    note: Optional[str] = None


class WarehouseCreate(WarehouseBase):
    pass


class WarehouseUpdate(BaseModel):
    code_id: Optional[str] = None
    branch_id: Optional[UUID] = None
    name: Optional[str] = None
    description: Optional[str] = None
    province_id: Optional[UUID] = None
    district_id: Optional[UUID] = None
    subdistrict_id: Optional[UUID] = None
    ward_id: Optional[UUID] = None
    address: Optional[str] = None
    pic_name: Optional[str] = None
    pic_contact: Optional[str] = None
    note: Optional[str] = None


class WarehouseResponse(WarehouseBase):
    id: UUID
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    
    model_config = ConfigDict(from_attributes=True)
