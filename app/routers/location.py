from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.crud.location import (
    crud_province, crud_district, crud_subdistrict, crud_ward, crud_zipcode
)
from app.schemas.location import (
    MasterProvinceResponse, MasterDistrictResponse, MasterSubdistrictResponse,
    MasterWardResponse, MasterZipcodeResponse, ZipcodeLocationResponse, LocationNameId,
    ZipcodeWithWardsResponse
)

router = APIRouter()





@router.get("/provinces", response_model=List[MasterProvinceResponse])
def get_provinces(
    skip: int = 0,
    limit: int = 1000,
    db: Session = Depends(get_db)
):
    """
    Get list of all provinces.
    Used for populating province dropdown.
    """
    return crud_province.get_multi(db, skip=skip, limit=limit)


@router.get("/provinces/{province_id}/districts", response_model=List[MasterDistrictResponse])
def get_districts_by_province(
    province_id: UUID,
    db: Session = Depends(get_db)
):
    """
    Get all districts/regencies in a specific province.
    Used for cascading dropdown when province is selected.
    """
    # Verify province exists
    province = crud_province.get(db, id=province_id)
    if province is None:
        raise HTTPException(status_code=404, detail="Province not found")
    
    districts = crud_district.get_by_province(db, province_id=province_id)
    return districts


@router.get("/districts/{district_id}/subdistricts", response_model=List[MasterSubdistrictResponse])
def get_subdistricts_by_district(
    district_id: UUID,
    db: Session = Depends(get_db)
):
    """
    Get all subdistricts in a specific district.
    Used for cascading dropdown when district is selected.
    """
    # Verify district exists
    district = crud_district.get(db, id=district_id)
    if district is None:
        raise HTTPException(status_code=404, detail="District not found")
    
    subdistricts = crud_subdistrict.get_by_district(db, district_id=district_id)
    return subdistricts


@router.get("/subdistricts/{subdistrict_id}/wards", response_model=List[MasterWardResponse])
def get_wards_by_subdistrict(
    subdistrict_id: UUID,
    db: Session = Depends(get_db)
):
    """
    Get all wards in a specific subdistrict.
    Used for cascading dropdown when subdistrict is selected.
    """
    # Verify subdistrict exists
    subdistrict = crud_subdistrict.get(db, id=subdistrict_id)
    if subdistrict is None:
        raise HTTPException(status_code=404, detail="Subdistrict not found")
    
    wards = crud_ward.get_by_subdistrict(db, subdistrict_id=subdistrict_id)
    return wards


@router.get("/wards/{ward_id}/zipcodes", response_model=List[MasterZipcodeResponse])
def get_zipcodes_by_ward(
    ward_id: UUID,
    db: Session = Depends(get_db)
):
    """
    Get all zipcodes in a specific ward.
    Used for cascading dropdown when ward is selected.
    """
    # Verify ward exists
    ward = crud_ward.get(db, id=ward_id)
    if ward is None:
        raise HTTPException(status_code=404, detail="Ward not found")
    
    zipcodes = crud_zipcode.get_by_ward(db, ward_id=ward_id)
    return zipcodes

@router.get("/zipcode/{code}", response_model=ZipcodeWithWardsResponse)
def get_location_by_zipcode(
    code: int,
    db: Session = Depends(get_db)
):
    """
    Get full location data by zipcode.
    Returns zipcode with list of all wards that share this zipcode.
    Multiple wards can have the same zipcode.
    """
    zipcode_list = crud_zipcode.get_all_by_code(db, code=code)
    if not zipcode_list:
        raise HTTPException(
            status_code=404, 
            detail=f"Zipcode {code} not found. Please check the zipcode and try again."
        )
    
    # Build the response with all wards that share this zipcode
    wards = []
    for zipcode_data in zipcode_list:
        wards.append({
            "ward": {
                "id": zipcode_data.ward.id,
                "name": zipcode_data.ward.name
            },
            "subdistrict": {
                "id": zipcode_data.ward.subdistrict.id,
                "name": zipcode_data.ward.subdistrict.name
            },
            "district": {
                "id": zipcode_data.ward.subdistrict.district.id,
                "name": zipcode_data.ward.subdistrict.district.name
            },
            "province": {
                "id": zipcode_data.ward.subdistrict.district.province.id,
                "name": zipcode_data.ward.subdistrict.district.province.name
            }
        })
    
    return {
        "zipcode": code,
        "wards": wards
    }