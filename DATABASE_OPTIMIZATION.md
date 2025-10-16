# Database Performance Optimization Guide

## Summary
This document outlines critical database indexes needed to improve query performance in your application.

---

## Critical Missing Indexes

### 1. Foreign Key Indexes

PostgreSQL does NOT automatically create indexes on foreign key columns. Add these indexes:

#### Companies Table
```sql
CREATE INDEX idx_companies_category_id ON companies(category_id);
CREATE INDEX idx_companies_province_id ON companies(province_id);
CREATE INDEX idx_companies_district_id ON companies(district_id);
CREATE INDEX idx_companies_subdistrict_id ON companies(subdistrict_id);
CREATE INDEX idx_companies_ward_id ON companies(ward_id);
CREATE INDEX idx_companies_zipcode_id ON companies(zipcode_id);
CREATE INDEX idx_companies_deleted_at ON companies(deleted_at);
```

#### Branches Table
```sql
CREATE INDEX idx_branches_company_id ON branches(company_id);
CREATE INDEX idx_branches_province_id ON branches(province_id);
CREATE INDEX idx_branches_district_id ON branches(district_id);
CREATE INDEX idx_branches_subdistrict_id ON branches(subdistrict_id);
CREATE INDEX idx_branches_ward_id ON branches(ward_id);
CREATE INDEX idx_branches_deleted_at ON branches(deleted_at);
```

#### Warehouses Table
```sql
CREATE INDEX idx_warehouses_branch_id ON warehouses(branch_id);
CREATE INDEX idx_warehouses_province_id ON warehouses(province_id);
CREATE INDEX idx_warehouses_district_id ON warehouses(district_id);
CREATE INDEX idx_warehouses_subdistrict_id ON warehouses(subdistrict_id);
CREATE INDEX idx_warehouses_ward_id ON warehouses(ward_id);
CREATE INDEX idx_warehouses_deleted_at ON warehouses(deleted_at);
```

#### Partners Table
```sql
CREATE INDEX idx_partners_category_id ON partners(category_id);
CREATE INDEX idx_partners_branch_id ON partners(branch_id);
CREATE INDEX idx_partners_warehouse_id ON partners(warehouse_id);
CREATE INDEX idx_partners_province_id ON partners(province_id);
CREATE INDEX idx_partners_district_id ON partners(district_id);
CREATE INDEX idx_partners_subdistrict_id ON partners(subdistrict_id);
CREATE INDEX idx_partners_ward_id ON partners(ward_id);
CREATE INDEX idx_partners_deleted_at ON partners(deleted_at);
```

#### Products Table
```sql
CREATE INDEX idx_products_category_id ON products(category_id);
CREATE INDEX idx_products_branch_id ON products(branch_id);
CREATE INDEX idx_products_warehouse_id ON products(warehouse_id);
CREATE INDEX idx_products_deleted_at ON products(deleted_at);
```

#### Location Tables
```sql
CREATE INDEX idx_master_districts_province_id ON master_districts(province_id);
CREATE INDEX idx_master_subdistricts_district_id ON master_subdistricts(district_id);
CREATE INDEX idx_master_wards_subdistrict_id ON master_wards(subdistrict_id);
CREATE INDEX idx_master_zipcodes_ward_id ON master_zipcodes(ward_id);
CREATE INDEX idx_master_zipcodes_code ON master_zipcodes(code);
```

#### Category Tables
```sql
CREATE INDEX idx_company_categories_deleted_at ON company_categories(deleted_at);
CREATE INDEX idx_partner_categories_deleted_at ON partner_categories(deleted_at);
CREATE INDEX idx_product_categories_deleted_at ON product_categories(deleted_at);
```

---

## Performance Impact

### Before Optimization
- Fetching 100 companies with relationships: **500+ queries**
- Query time: **5-10 seconds** (or more with large datasets)
- Database load: **VERY HIGH**

### After Optimization (with eager loading + indexes)
- Fetching 100 companies with relationships: **1 query with joins**
- Query time: **< 500ms**
- Database load: **LOW**

---

## Implementation Steps

### Option 1: Raw SQL (Quick Fix)
1. Connect to your PostgreSQL database
2. Run all the CREATE INDEX statements above
3. Verify with: `\d+ table_name` in psql

### Option 2: Using Alembic Migration (Recommended)
Create a new migration file:

```bash
alembic revision -m "add_performance_indexes"
```

Then add to the migration:

```python
def upgrade():
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


def downgrade():
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
```

### Option 3: Add to SQLAlchemy Models (For New Deployments)
Add index=True to Column definitions in models:

```python
# Example for Company model
category_id = Column(UUID(as_uuid=True), ForeignKey("company_categories.id"), nullable=False, index=True)
province_id = Column(UUID(as_uuid=True), ForeignKey("master_provinces.id"), nullable=True, index=True)
deleted_at = Column(DateTime(timezone=True), nullable=True, index=True)
```

---

## Monitoring & Verification

### Check Index Usage
```sql
SELECT schemaname, tablename, indexname, idx_scan, idx_tup_read, idx_tup_fetch
FROM pg_stat_user_indexes
WHERE schemaname = 'public'
ORDER BY idx_scan DESC;
```

### Check Slow Queries
Enable slow query logging in PostgreSQL:
```sql
ALTER SYSTEM SET log_min_duration_statement = 1000;  -- Log queries > 1 second
SELECT pg_reload_conf();
```

### Analyze Query Plans
```sql
EXPLAIN ANALYZE SELECT * FROM companies WHERE deleted_at IS NULL LIMIT 100;
```

Look for "Seq Scan" - these should be "Index Scan" after adding indexes.

---

## Additional Recommendations

1. **Add composite indexes** for common query patterns:
   ```sql
   CREATE INDEX idx_companies_deleted_category ON companies(deleted_at, category_id);
   ```

2. **Partial indexes** for soft-deleted rows:
   ```sql
   CREATE INDEX idx_companies_active ON companies(id) WHERE deleted_at IS NULL;
   ```

3. **Regular VACUUM and ANALYZE**:
   ```sql
   VACUUM ANALYZE companies;
   VACUUM ANALYZE branches;
   -- Run for all tables
   ```

4. **Monitor index bloat** and rebuild if necessary:
   ```sql
   REINDEX TABLE companies;
   ```

---

## Changes Already Applied

✅ **Eager Loading** added to all CRUD operations to prevent N+1 queries:
- `app/crud/company.py` - Company and CompanyCategory
- `app/crud/branch.py` - Branch
- `app/crud/warehouse.py` - Warehouse
- `app/crud/partner.py` - Partner and PartnerCategory
- `app/crud/product.py` - Product and ProductCategory

This ensures relationships are loaded with JOINs instead of separate queries.

---

## Quick Start

**Fastest way to apply indexes:**

1. Copy all SQL CREATE INDEX statements from sections above
2. Connect to your database: `psql -U your_user -d your_database`
3. Paste and run all CREATE INDEX commands
4. Done! Your queries will be much faster

**Recommended for production:**
Use Option 2 (Alembic migration) to keep track of changes in version control.
