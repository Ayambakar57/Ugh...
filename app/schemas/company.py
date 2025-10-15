from pydantic import BaseModel, ConfigDict
from uuid import UUID
from datetime import datetime
from typing import Optional
from app.schemas.location import MasterProvinceResponse, MasterDistrictResponse, MasterSubdistrictResponse, MasterWardResponse, MasterZipcodeResponse


# CompanyCategory Schemas
class CompanyCategoryBase(BaseModel):
    code_id: str
    name: str
    note: str


class CompanyCategoryCreate(CompanyCategoryBase):
    pass


class CompanyCategoryUpdate(BaseModel):
    code_id: Optional[str] = None
    name: Optional[str] = None
    note: Optional[str] = None


class CompanyCategoryResponse(CompanyCategoryBase):
    id: UUID
    created_at: datetime
    updated_at: datetime
    
    model_config = ConfigDict(from_attributes=True)


# Company Schemas
class CompanyBase(BaseModel):
    code_id: str
    name: str
    category_id: UUID
    description: Optional[str] = None
    province_id: Optional[UUID] = None
    district_id: Optional[UUID] = None
    subdistrict_id: Optional[UUID] = None
    ward_id: Optional[UUID] = None
    zipcode_id: Optional[UUID] = None
    address: Optional[str] = None
    pic_name: Optional[str] = None
    pic_contact: Optional[str] = None
    note: Optional[str] = None
    province: Optional[MasterProvinceResponse] = None
    district: Optional[MasterDistrictResponse] = None
    subdistrict: Optional[MasterSubdistrictResponse] = None
    ward: Optional[MasterWardResponse] = None
    zipcode: Optional[MasterZipcodeResponse] = None


class CompanyCreate(CompanyBase):
    pass


class CompanyUpdate(BaseModel):
    code_id: Optional[str] = None
    name: Optional[str] = None
    category_id: Optional[UUID] = None
    description: Optional[str] = None
    province_id: Optional[UUID] = None
    district_id: Optional[UUID] = None
    subdistrict_id: Optional[UUID] = None
    ward_id: Optional[UUID] = None
    zipcode_id: Optional[UUID] = None
    address: Optional[str] = None
    pic_name: Optional[str] = None
    pic_contact: Optional[str] = None
    note: Optional[str] = None


class CompanyResponse(CompanyBase):
    id: UUID
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    
    model_config = ConfigDict(from_attributes=True)
