"""add_performance_indexes

Revision ID: ad791d6cbf8a
Revises: e554c19dff79
Create Date: 2025-10-15 21:21:32.185457

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ad791d6cbf8a'
down_revision: Union[str, Sequence[str], None] = 'e554c19dff79'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # Companies
    op.create_index('idx_companies_category_id', 'companies', ['category_id'])
    op.create_index('idx_companies_province_id', 'companies', ['province_id'])
    op.create_index('idx_companies_district_id', 'companies', ['district_id'])
    op.create_index('idx_companies_subdistrict_id', 'companies', ['subdistrict_id'])
    op.create_index('idx_companies_ward_id', 'companies', ['ward_id'])
    op.create_index('idx_companies_zipcode_id', 'companies', ['zipcode_id'])
    op.create_index('idx_companies_deleted_at', 'companies', ['deleted_at'])
    
    # Branches
    op.create_index('idx_branches_company_id', 'branches', ['company_id'])
    op.create_index('idx_branches_province_id', 'branches', ['province_id'])
    op.create_index('idx_branches_district_id', 'branches', ['district_id'])
    op.create_index('idx_branches_subdistrict_id', 'branches', ['subdistrict_id'])
    op.create_index('idx_branches_ward_id', 'branches', ['ward_id'])
    op.create_index('idx_branches_deleted_at', 'branches', ['deleted_at'])
    
    # Warehouses
    op.create_index('idx_warehouses_branch_id', 'warehouses', ['branch_id'])
    op.create_index('idx_warehouses_province_id', 'warehouses', ['province_id'])
    op.create_index('idx_warehouses_district_id', 'warehouses', ['district_id'])
    op.create_index('idx_warehouses_subdistrict_id', 'warehouses', ['subdistrict_id'])
    op.create_index('idx_warehouses_ward_id', 'warehouses', ['ward_id'])
    op.create_index('idx_warehouses_deleted_at', 'warehouses', ['deleted_at'])
    
    # Partners
    op.create_index('idx_partners_category_id', 'partners', ['category_id'])
    op.create_index('idx_partners_branch_id', 'partners', ['branch_id'])
    op.create_index('idx_partners_warehouse_id', 'partners', ['warehouse_id'])
    op.create_index('idx_partners_province_id', 'partners', ['province_id'])
    op.create_index('idx_partners_district_id', 'partners', ['district_id'])
    op.create_index('idx_partners_subdistrict_id', 'partners', ['subdistrict_id'])
    op.create_index('idx_partners_ward_id', 'partners', ['ward_id'])
    op.create_index('idx_partners_deleted_at', 'partners', ['deleted_at'])
    
    # Products
    op.create_index('idx_products_category_id', 'products', ['category_id'])
    op.create_index('idx_products_branch_id', 'products', ['branch_id'])
    op.create_index('idx_products_warehouse_id', 'products', ['warehouse_id'])
    op.create_index('idx_products_deleted_at', 'products', ['deleted_at'])
    
    # Locations
    op.create_index('idx_master_districts_province_id', 'master_districts', ['province_id'])
    op.create_index('idx_master_subdistricts_district_id', 'master_subdistricts', ['district_id'])
    op.create_index('idx_master_wards_subdistrict_id', 'master_wards', ['subdistrict_id'])
    op.create_index('idx_master_zipcodes_ward_id', 'master_zipcodes', ['ward_id'])
    op.create_index('idx_master_zipcodes_code', 'master_zipcodes', ['code'])
    
    # Categories
    op.create_index('idx_company_categories_deleted_at', 'company_categories', ['deleted_at'])
    op.create_index('idx_partner_categories_deleted_at', 'partner_categories', ['deleted_at'])
    op.create_index('idx_product_categories_deleted_at', 'product_categories', ['deleted_at'])


def downgrade() -> None:
    """Downgrade schema."""
    # Drop all indexes in reverse order
    op.drop_index('idx_product_categories_deleted_at')
    op.drop_index('idx_partner_categories_deleted_at')
    op.drop_index('idx_company_categories_deleted_at')
    op.drop_index('idx_master_zipcodes_code')
    op.drop_index('idx_master_zipcodes_ward_id')
    op.drop_index('idx_master_wards_subdistrict_id')
    op.drop_index('idx_master_subdistricts_district_id')
    op.drop_index('idx_master_districts_province_id')
    op.drop_index('idx_products_deleted_at')
    op.drop_index('idx_products_warehouse_id')
    op.drop_index('idx_products_branch_id')
    op.drop_index('idx_products_category_id')
    op.drop_index('idx_partners_deleted_at')
    op.drop_index('idx_partners_ward_id')
    op.drop_index('idx_partners_subdistrict_id')
    op.drop_index('idx_partners_district_id')
    op.drop_index('idx_partners_province_id')
    op.drop_index('idx_partners_warehouse_id')
    op.drop_index('idx_partners_branch_id')
    op.drop_index('idx_partners_category_id')
    op.drop_index('idx_warehouses_deleted_at')
    op.drop_index('idx_warehouses_ward_id')
    op.drop_index('idx_warehouses_subdistrict_id')
    op.drop_index('idx_warehouses_district_id')
    op.drop_index('idx_warehouses_province_id')
    op.drop_index('idx_warehouses_branch_id')
    op.drop_index('idx_branches_deleted_at')
    op.drop_index('idx_branches_ward_id')
    op.drop_index('idx_branches_subdistrict_id')
    op.drop_index('idx_branches_district_id')
    op.drop_index('idx_branches_province_id')
    op.drop_index('idx_branches_company_id')
    op.drop_index('idx_companies_deleted_at')
    op.drop_index('idx_companies_zipcode_id')
    op.drop_index('idx_companies_ward_id')
    op.drop_index('idx_companies_subdistrict_id')
    op.drop_index('idx_companies_district_id')
    op.drop_index('idx_companies_province_id')
    op.drop_index('idx_companies_category_id')
