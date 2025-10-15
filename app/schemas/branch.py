from pydantic import BaseModel, ConfigDict
from uuid import UUID
from datetime import datetime
from typing import Optional
from app.schemas.location import MasterProvinceResponse, MasterDistrictResponse, MasterSubdistrictResponse, MasterWardResponse, MasterZipcodeResponse


class BranchBase(BaseModel):
    code_id: str
    company_id: UUID
    name: str
    description: Optional[str] = None
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
    



class BranchCreate(BranchBase):
    pass


class BranchUpdate(BaseModel):
    code_id: Optional[str] = None
    company_id: Optional[UUID] = None
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


class BranchResponse(BranchBase):
    id: UUID
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    
    model_config = ConfigDict(from_attributes=True)
