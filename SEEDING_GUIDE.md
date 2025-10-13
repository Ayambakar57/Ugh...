# Database Seeding Guide

This guide explains how to seed your database with master location data and dummy business data.

## Overview

The seeding system includes:
1. **Master Location Data** - Complete location hierarchy (provinces, districts, subdistricts, wards, zipcodes)
2. **Dummy Business Data** - Sample companies and products for testing

## What's Included in Dummy Data

### Companies (6 total)
**Printing & Publishing Companies:**
- **PrintMaster Solutions** - Commercial printing services (offset, digital, large format)
- **Creative Print Hub** - Custom packaging and branding materials
- **Digital Print Express** - 24/7 digital printing with same-day delivery

**Hardware & Tools Companies:**
- **Mega Hardware Supply** - Construction materials and home improvement
- **Pro Tools Indonesia** - Professional grade tools and equipment
- **BuildMart Hardware** - One-stop construction and building materials

### Branches
- 7 branches across different locations
- Each with complete address and contact information
- Linked to location data from `res.json`

### Warehouses
- 6 warehouses distributed across branches
- Climate-controlled and heavy-duty facilities
- Complete with managers and contact info

### Product Categories
**Printing Categories:**
- Printing Paper
- Ink & Toner
- Printing Machines
- Packaging Materials

**Hardware Categories:**
- Hand Tools
- Power Tools
- Fasteners
- Building Materials

### Products (22 total)
**Printing Products (9):**
- A4 Copy Paper, Art Paper, Cardstock
- Offset Ink Sets, Laser Toner
- Digital Printers, Offset Machines
- Corrugated Boxes, Paper Bags

**Hardware Products (13):**
- Hand tools (Hammers, Screwdrivers, Wrenches, Pliers)
- Power tools (Drills, Angle Grinders, Circular Saws)
- Fasteners (Screws, Bolts, Anchors)
- Building materials (Cement, PVC Pipes, Steel Rebar)

## Files

```
├── seed.py                  # Main seeder (runs all seeders)
├── seed_dummy_data.py       # Dummy data seeder
├── dummy_data.sql           # SQL file with dummy data
├── res.json                 # Location IDs for addresses
└── SEEDING_GUIDE.md        # This file
```

## Running the Seeder

### Option 1: Seed Everything (Recommended)

Run the main seeder to populate both master location and dummy data:

```bash
python seed.py
```

This will:
1. Download and seed master location data (if not exists)
2. Seed dummy companies and products (if not exists)
3. Show a summary of seeded data

### Option 2: Seed Only Dummy Data

If you already have location data and only want dummy data:

```bash
python seed_dummy_data.py
```

### Option 3: Manual SQL Execution

You can also manually execute the SQL file:

```bash
# Using psql
psql -U your_username -d your_database -f dummy_data.sql

# Or import via database client
```

## Sample Output

```
============================================================
DATABASE SEEDING - Master Data & Dummy Data
============================================================

1. MASTER LOCATION DATA
------------------------------------------------------------
Skipping master location seed as master location data already exists.

2. DUMMY COMPANIES & PRODUCTS DATA
------------------------------------------------------------
Loading dummy data from SQL file...
Found 72 SQL statements to execute...
  [1/72] Executing statement...
  [2/72] Executing statement...
  ...
✓ Dummy data seeded successfully!

==================================================
SEED SUMMARY
==================================================
  Companies:    6
  Branches:     7
  Warehouses:   6
  Products:     22
==================================================

============================================================
✓ ALL SEEDING COMPLETED SUCCESSFULLY!
============================================================
```

## Location Data Mapping

The dummy data uses real location IDs from `res.json`:

| Company | Province ID | District ID | Subdistrict ID | Ward ID | Zipcode |
|---------|------------|-------------|----------------|---------|---------|
| PrintMaster Solutions | 09d2c834... | fb6323dc... | 08c17844... | 75fca822... | 63372 |
| Creative Print Hub | e13c585e... | bb15ba9d... | 4b326dec... | 71526a3b... | 23768 |
| Digital Print Express | 715e36a7... | 99fdeaee... | fe480cd7... | 92209704... | 34787 |
| Mega Hardware Supply | b2f0075b... | de69d363... | a7ec6f87... | 44e0b8c9... | 93355 |
| Pro Tools Indonesia | d8e15fd4... | ebaf7360... | 57858397... | 072a6690... | 50663 |
| BuildMart Hardware | 224fabdb... | e8d1dd17... | 3d61964a... | ec304291... | 71554 |

## Verifying the Data

### Check via API

After seeding, verify the data through your API:

```bash
# Get all companies
curl http://localhost:8000/api/companies

# Get all products
curl http://localhost:8000/api/products

# Get company by ID
curl http://localhost:8000/api/companies/b1111111-1111-1111-1111-111111111111

# Get location by zipcode
curl http://localhost:8000/api/locations/zipcode/63372
```

### Check via Database

```sql
-- Count records
SELECT 'Companies' as table_name, COUNT(*) as count FROM companies
UNION ALL
SELECT 'Branches', COUNT(*) FROM branches
UNION ALL
SELECT 'Warehouses', COUNT(*) FROM warehouses
UNION ALL
SELECT 'Products', COUNT(*) FROM products;

-- View sample data
SELECT c.name as company, c.code_id, cc.name as category 
FROM companies c
JOIN company_categories cc ON c.category_id = cc.id;

-- View products with categories
SELECT p.name, p.code_id, pc.name as category
FROM products p
JOIN product_categories pc ON p.category_id = pc.id
ORDER BY pc.name, p.name;
```

## Resetting Data

To remove dummy data and re-seed:

```sql
-- Delete in correct order (respecting foreign keys)
DELETE FROM products;
DELETE FROM warehouses;
DELETE FROM branches;
DELETE FROM companies;
DELETE FROM company_categories;
DELETE FROM product_categories;
```

Then run the seeder again:
```bash
python seed.py
```

## Customization

### Adding More Data

Edit `dummy_data.sql` and add your own INSERT statements following the existing format.

### Modifying Existing Data

Update the values in `dummy_data.sql`:
- Change company names, descriptions, contacts
- Add more products or categories
- Update addresses using different IDs from `res.json`

### Using Different Locations

Pick different location IDs from `res.json` and update the INSERT statements:

```sql
-- Example: Use a different location
province_id = 'YOUR_PROVINCE_ID',
district_id = 'YOUR_DISTRICT_ID',
subdistrict_id = 'YOUR_SUBDISTRICT_ID',
ward_id = 'YOUR_WARD_ID',
zipcode_id = 'YOUR_ZIPCODE_ID'
```

## Troubleshooting

### Error: "dummy_data.sql file not found"
- Make sure `dummy_data.sql` is in the same directory as `seed_dummy_data.py`
- Check file path and permissions

### Error: "Foreign key constraint violation"
- Ensure master location data is seeded first
- Check that all referenced IDs exist in the database

### Error: "Duplicate key value"
- Dummy data already exists
- Either skip seeding or delete existing data first

### Data not appearing in API
- Check database connection in `.env`
- Verify tables are created (run migrations)
- Restart the FastAPI server

## Integration with Your App

After seeding, you can:
- Test your API endpoints with real-looking data
- Develop frontend with realistic data
- Demo your application to clients
- Perform load testing with sample records

## Notes

- All UUIDs are pre-generated for consistency
- Location IDs match actual data from your location master
- Product codes follow a logical naming convention
- All timestamps use `NOW()` for current date/time
- The seeder is idempotent (safe to run multiple times)

## Need More Data?

To generate additional dummy data:
1. Copy existing INSERT patterns in `dummy_data.sql`
2. Generate new UUIDs
3. Update code_id sequences
4. Choose different locations from `res.json`
5. Run the seeder again

Happy seeding! 🌱
