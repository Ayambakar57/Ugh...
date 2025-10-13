from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid

from app.database import Base


class MasterProvince(Base):
    __tablename__ = "master_provinces"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    
    # Relationships
    districts = relationship("MasterDistrict", back_populates="province")


class MasterDistrict(Base):
    __tablename__ = "master_districts"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    province_id = Column(UUID(as_uuid=True), ForeignKey("master_provinces.id"), nullable=False)
    
    # Relationships
    province = relationship("MasterProvince", back_populates="districts")
    subdistricts = relationship("MasterSubdistrict", back_populates="district")


class MasterSubdistrict(Base):
    __tablename__ = "master_subdistricts"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    district_id = Column(UUID(as_uuid=True), ForeignKey("master_districts.id"), nullable=False)
    
    # Relationships
    district = relationship("MasterDistrict", back_populates="subdistricts")
    wards = relationship("MasterWard", back_populates="subdistrict")


class MasterWard(Base):
    __tablename__ = "master_wards"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    subdistrict_id = Column(UUID(as_uuid=True), ForeignKey("master_subdistricts.id"), nullable=False)
    
    # Relationships
    subdistrict = relationship("MasterSubdistrict", back_populates="wards")
    zipcodes = relationship("MasterZipcode", back_populates="ward")


class MasterZipcode(Base):
    __tablename__ = "master_zipcodes"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    code = Column(Integer, nullable=False)
    ward_id = Column(UUID(as_uuid=True), ForeignKey("master_wards.id"), nullable=False)
    
    # Relationships
    ward = relationship("MasterWard", back_populates="zipcodes")
