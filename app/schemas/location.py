from pydantic import BaseModel, ConfigDict
from uuid import UUID
from typing import Optional, List


# MasterProvince Schemas
class MasterProvinceBase(BaseModel):
    name: str


class MasterProvinceCreate(MasterProvinceBase):
    pass


class MasterProvinceUpdate(BaseModel):
    name: Optional[str] = None


class MasterProvinceResponse(MasterProvinceBase):
    id: UUID
    
    model_config = ConfigDict(from_attributes=True)


# MasterDistrict Schemas
class MasterDistrictBase(BaseModel):
    name: str
    province_id: UUID


class MasterDistrictCreate(MasterDistrictBase):
    pass


class MasterDistrictUpdate(BaseModel):
    name: Optional[str] = None
    province_id: Optional[UUID] = None


class MasterDistrictResponse(MasterDistrictBase):
    id: UUID
    
    model_config = ConfigDict(from_attributes=True)


# MasterSubdistrict Schemas
class MasterSubdistrictBase(BaseModel):
    name: str
    district_id: UUID


class MasterSubdistrictCreate(MasterSubdistrictBase):
    pass


class MasterSubdistrictUpdate(BaseModel):
    name: Optional[str] = None
    district_id: Optional[UUID] = None


class MasterSubdistrictResponse(MasterSubdistrictBase):
    id: UUID
    
    model_config = ConfigDict(from_attributes=True)


# MasterWard Schemas
class MasterWardBase(BaseModel):
    name: str
    subdistrict_id: UUID


class MasterWardCreate(MasterWardBase):
    pass


class MasterWardUpdate(BaseModel):
    name: Optional[str] = None
    subdistrict_id: Optional[UUID] = None


class MasterWardResponse(MasterWardBase):
    id: UUID
    
    model_config = ConfigDict(from_attributes=True)


# MasterZipcode Schemas
class MasterZipcodeBase(BaseModel):
    code: int
    ward_id: UUID


class MasterZipcodeCreate(MasterZipcodeBase):
    pass


class MasterZipcodeUpdate(BaseModel):
    code: Optional[int] = None
    ward_id: Optional[UUID] = None


class MasterZipcodeResponse(MasterZipcodeBase):
    id: UUID
    
    model_config = ConfigDict(from_attributes=True)


# Nested Location Response Schemas (for simplified responses)
class LocationNameId(BaseModel):
    id: UUID
    name: str
    
    model_config = ConfigDict(from_attributes=True)


class ZipcodeLocationResponse(BaseModel):
    zipcode: int
    ward: LocationNameId
    subdistrict: LocationNameId
    district: LocationNameId
    province: LocationNameId
    
    model_config = ConfigDict(from_attributes=True)


class WardLocationDetail(BaseModel):
    """Ward with its full location hierarchy"""
    ward: LocationNameId
    subdistrict: LocationNameId
    district: LocationNameId
    province: LocationNameId
    
    model_config = ConfigDict(from_attributes=True)


class ZipcodeWithWardsResponse(BaseModel):
    """Response for zipcode lookup that returns all wards sharing the same zipcode"""
    zipcode: int
    wards: List[WardLocationDetail]
    
    model_config = ConfigDict(from_attributes=True)
