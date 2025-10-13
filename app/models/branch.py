from sqlalchemy import Column, String, Text, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid

from app.database import Base


class Branch(Base):
    __tablename__ = "branches"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    code_id = Column(String, nullable=False)
    company_id = Column(UUID(as_uuid=True), ForeignKey("companies.id"), nullable=False)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    province_id = Column(UUID(as_uuid=True), ForeignKey("master_provinces.id"), nullable=True)
    district_id = Column(UUID(as_uuid=True), ForeignKey("master_districts.id"), nullable=True)
    subdistrict_id = Column(UUID(as_uuid=True), ForeignKey("master_subdistricts.id"), nullable=True)
    ward_id = Column(UUID(as_uuid=True), ForeignKey("master_wards.id"), nullable=True)
    address = Column(Text, nullable=True)
    pic_name = Column(String, nullable=True)
    pic_contact = Column(String, nullable=True)
    note = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), nullable=True, server_default=func.now())
    updated_at = Column(DateTime(timezone=True), nullable=True, server_default=func.now(), onupdate=func.now())
    
    # Relationships
    company = relationship("Company", back_populates="branches")
    province = relationship("MasterProvince", foreign_keys=[province_id])
    district = relationship("MasterDistrict", foreign_keys=[district_id])
    subdistrict = relationship("MasterSubdistrict", foreign_keys=[subdistrict_id])
    ward = relationship("MasterWard", foreign_keys=[ward_id])
    warehouses = relationship("Warehouse", back_populates="branch")
    products = relationship("Product", back_populates="branch")
    partners = relationship("Partner", back_populates="branch")
