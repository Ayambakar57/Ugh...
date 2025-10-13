"""
Seeder for Dummy Data - Companies and Products
Loads printing and hardware business data from dummy_data.sql
"""
import os
from sqlalchemy.sql import text
from app.database import SessionLocal
from app.models.company import Company, CompanyCategory
from app.models.product import Product, ProductCategory
from app.models.branch import Branch
from app.models.warehouse import Warehouse


def check_dummy_data_exists(db):
    """Check if dummy data already exists"""
    return (
        db.query(CompanyCategory).filter(
            CompanyCategory.code_id.in_(['CC-PRINT', 'CC-HARDWARE'])
        ).first() is not None
    )


def run_dummy_data_seed(db):
    """Execute dummy data seeding"""
    if check_dummy_data_exists(db):
        print("✓ Dummy data already exists. Skipping seed.")
        return
    
    print("Loading dummy data from SQL file...")
    
    # Read SQL file
    sql_file_path = os.path.join(os.path.dirname(__file__), 'dummy_data.sql')
    
    if not os.path.exists(sql_file_path):
        print("✗ Error: dummy_data.sql file not found!")
        return
    
    with open(sql_file_path, 'r', encoding='utf-8') as f:
        sql_content = f.read()
    
    # Split by semicolon and filter out comments and empty statements
    statements = []
    for statement in sql_content.split(';'):
        # Remove comments and whitespace
        cleaned = '\n'.join(
            line for line in statement.split('\n') 
            if not line.strip().startswith('--') and line.strip()
        )
        if cleaned.strip():
            statements.append(cleaned.strip())
    
    print(f"Found {len(statements)} SQL statements to execute...")
    
    try:
        # Execute each statement
        for i, statement in enumerate(statements, 1):
            if statement.strip():
                print(f"  [{i}/{len(statements)}] Executing statement...")
                db.execute(text(statement))
        
        db.commit()
        print("✓ Dummy data seeded successfully!")
        
        # Print summary
        company_count = db.query(Company).count()
        branch_count = db.query(Branch).count()
        warehouse_count = db.query(Warehouse).count()
        product_count = db.query(Product).count()
        
        print("\n" + "="*50)
        print("SEED SUMMARY")
        print("="*50)
        print(f"  Companies:    {company_count}")
        print(f"  Branches:     {branch_count}")
        print(f"  Warehouses:   {warehouse_count}")
        print(f"  Products:     {product_count}")
        print("="*50)
        
    except Exception as e:
        db.rollback()
        print(f"✗ Error seeding dummy data: {str(e)}")
        raise


def main():
    """Main seeder function"""
    print("\n" + "="*50)
    print("DUMMY DATA SEEDER - Companies & Products")
    print("="*50 + "\n")
    
    db = SessionLocal()
    
    try:
        run_dummy_data_seed(db)
        
        print("\n✓ All done!")
        
    except Exception as e:
        print(f"\n✗ Seeding failed: {str(e)}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
