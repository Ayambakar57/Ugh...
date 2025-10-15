from pydantic import BaseModel, ConfigDict
from uuid import UUID
from datetime import datetime
from typing import Optional
from app.schemas.location import MasterProvinceResponse, MasterDistrictResponse, MasterSubdistrictResponse, MasterWardResponse


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
    province: Optional[MasterProvinceResponse] = None
    district: Optional[MasterDistrictResponse] = None
    subdistrict: Optional[MasterSubdistrictResponse] = None
    ward: Optional[MasterWardResponse] = None


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
