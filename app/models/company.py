from sqlalchemy import Column, String, Text, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid

from app.database import Base


class CompanyCategory(Base):
    __tablename__ = "company_categories"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    code_id = Column(String, nullable=False)
    name = Column(String, nullable=False)
    note = Column(Text, nullable=False)
    deleted_at = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now())
    
    # Relationships
    companies = relationship("Company", back_populates="category")


class Company(Base):
    __tablename__ = "companies"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    code_id = Column(String, nullable=False)
    name = Column(String, nullable=False)
    category_id = Column(UUID(as_uuid=True), ForeignKey("company_categories.id"), nullable=False)
    description = Column(Text, nullable=True)
    province_id = Column(UUID(as_uuid=True), ForeignKey("master_provinces.id"), nullable=True)
    district_id = Column(UUID(as_uuid=True), ForeignKey("master_districts.id"), nullable=True)
    subdistrict_id = Column(UUID(as_uuid=True), ForeignKey("master_subdistricts.id"), nullable=True)
    ward_id = Column(UUID(as_uuid=True), ForeignKey("master_wards.id"), nullable=True)
    zipcode_id = Column(UUID(as_uuid=True), ForeignKey("master_zipcodes.id"), nullable=True)
    address = Column(Text, nullable=True)
    pic_name = Column(String, nullable=True)
    pic_contact = Column(String, nullable=True)
    note = Column(Text, nullable=True)
    deleted_at = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), nullable=True, server_default=func.now())
    updated_at = Column(DateTime(timezone=True), nullable=True, server_default=func.now(), onupdate=func.now())
    
    # Relationships
    category = relationship("CompanyCategory", back_populates="companies")
    province = relationship("MasterProvince", foreign_keys=[province_id])
    district = relationship("MasterDistrict", foreign_keys=[district_id])
    subdistrict = relationship("MasterSubdistrict", foreign_keys=[subdistrict_id])
    ward = relationship("MasterWard", foreign_keys=[ward_id])
    zipcode = relationship("MasterZipcode", foreign_keys=[zipcode_id])
    branches = relationship("Branch", back_populates="company")
