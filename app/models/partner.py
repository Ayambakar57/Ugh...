from sqlalchemy import Column, String, Text, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid

from app.database import Base


class PartnerCategory(Base):
    __tablename__ = "partner_categories"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    code_id = Column(String, nullable=False)
    name = Column(String, nullable=False)
    note = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now())
    
    # Relationships
    partners = relationship("Partner", back_populates="category")


class Partner(Base):
    __tablename__ = "partners"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    code_id = Column(String, nullable=False)
    branch_id = Column(UUID(as_uuid=True), ForeignKey("branches.id"), nullable=False)
    warehouse_id = Column(UUID(as_uuid=True), ForeignKey("warehouses.id"), nullable=False)
    name = Column(String, nullable=False)
    category_id = Column(UUID(as_uuid=True), ForeignKey("partner_categories.id"), nullable=False)
    description = Column(Text, nullable=False)
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
    branch = relationship("Branch", back_populates="partners")
    warehouse = relationship("Warehouse", back_populates="partners")
    category = relationship("PartnerCategory", back_populates="partners")
    province = relationship("MasterProvince", foreign_keys=[province_id])
    district = relationship("MasterDistrict", foreign_keys=[district_id])
    subdistrict = relationship("MasterSubdistrict", foreign_keys=[subdistrict_id])
    ward = relationship("MasterWard", foreign_keys=[ward_id])
