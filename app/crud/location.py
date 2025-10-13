from typing import List, Optional
from uuid import UUID
from sqlalchemy.orm import Session, joinedload

from app.crud.base import CRUDBase
from app.models.location import (
    MasterProvince, MasterDistrict, MasterSubdistrict,
    MasterWard, MasterZipcode
)
from app.schemas.location import (
    MasterProvinceCreate, MasterProvinceUpdate,
    MasterDistrictCreate, MasterDistrictUpdate,
    MasterSubdistrictCreate, MasterSubdistrictUpdate,
    MasterWardCreate, MasterWardUpdate,
    MasterZipcodeCreate, MasterZipcodeUpdate
)


class CRUDProvince(CRUDBase[MasterProvince, MasterProvinceCreate, MasterProvinceUpdate]):
    pass


class CRUDDistrict(CRUDBase[MasterDistrict, MasterDistrictCreate, MasterDistrictUpdate]):
    def get_by_province(self, db: Session, province_id: UUID) -> List[MasterDistrict]:
        """Get all districts in a province"""
        return db.query(self.model).filter(self.model.province_id == province_id).all()


class CRUDSubdistrict(CRUDBase[MasterSubdistrict, MasterSubdistrictCreate, MasterSubdistrictUpdate]):
    def get_by_district(self, db: Session, district_id: UUID) -> List[MasterSubdistrict]:
        """Get all subdistricts in a district"""
        return db.query(self.model).filter(self.model.district_id == district_id).all()


class CRUDWard(CRUDBase[MasterWard, MasterWardCreate, MasterWardUpdate]):
    def get_by_subdistrict(self, db: Session, subdistrict_id: UUID) -> List[MasterWard]:
        """Get all wards in a subdistrict"""
        return db.query(self.model).filter(self.model.subdistrict_id == subdistrict_id).all()


class CRUDZipcode(CRUDBase[MasterZipcode, MasterZipcodeCreate, MasterZipcodeUpdate]):
    def get_by_ward(self, db: Session, ward_id: UUID) -> List[MasterZipcode]:
        """Get all zipcodes in a ward"""
        return db.query(self.model).filter(self.model.ward_id == ward_id).all()
    
    def get_by_code(self, db: Session, code: int) -> Optional[MasterZipcode]:
        """Get zipcode by code with all related location data"""
        return db.query(self.model).options(
            joinedload(self.model.ward).joinedload(MasterWard.subdistrict).joinedload(MasterSubdistrict.district).joinedload(MasterDistrict.province)
        ).filter(self.model.code == code).first()
    
    def get_all_by_code(self, db: Session, code: int) -> List[MasterZipcode]:
        """Get all zipcodes with the same code (multiple wards can share the same zipcode)"""
        return db.query(self.model).options(
            joinedload(self.model.ward).joinedload(MasterWard.subdistrict).joinedload(MasterSubdistrict.district).joinedload(MasterDistrict.province)
        ).filter(self.model.code == code).all()


crud_province = CRUDProvince(MasterProvince)
crud_district = CRUDDistrict(MasterDistrict)
crud_subdistrict = CRUDSubdistrict(MasterSubdistrict)
crud_ward = CRUDWard(MasterWard)
crud_zipcode = CRUDZipcode(MasterZipcode)
