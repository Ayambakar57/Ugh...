import urllib.request
from sqlalchemy.sql import text
from app.database import SessionLocal
from app.models.location import (
    MasterProvince,
    MasterDistrict,
    MasterSubdistrict,
    MasterWard,
    MasterZipcode
)
from seed_dummy_data import run_dummy_data_seed

def download_master_location_data():
    print("Downloading master location data... (this may take a while)")
    with urllib.request.urlopen("https://archive.itsnep.my.id/umazink/master_location_data.sql") as response:
        data = response.read()
        return data.decode('utf-8')

def check_master_location_exists(db):
    return (
        db.query(MasterProvince).first() is not None and
        db.query(MasterDistrict).first() is not None and
        db.query(MasterSubdistrict).first() is not None and
        db.query(MasterWard).first() is not None and
        db.query(MasterZipcode).first() is not None
    )

def run_master_location_seed(db):
    if check_master_location_exists(db):
        print("Skipping master location seed as a master location data already exists.")
        return
    
    # Download and execute the SQL script to sqlalchemy
    sql_data = download_master_location_data()
    print("Uploading master location data...")
    try:
        db.execute(text(sql_data))
        db.commit()
        print("Master location data uploaded successfully.")
    except Exception as e:
        db.rollback()
        raise e

if __name__ == "__main__":
    print("\n" + "="*60)
    print("DATABASE SEEDING - Master Data & Dummy Data")
    print("="*60 + "\n")
    
    db = SessionLocal()
    
    try:
        # Seed master location data
        print("1. MASTER LOCATION DATA")
        print("-" * 60)
        run_master_location_seed(db)
        
        # Seed dummy company and product data
        print("\n2. DUMMY COMPANIES & PRODUCTS DATA")
        print("-" * 60)
        run_dummy_data_seed(db)
        
        print("\n" + "="*60)
        print("✓ ALL SEEDING COMPLETED SUCCESSFULLY!")
        print("="*60 + "\n")
        
    except Exception as e:
        print(f"\n✗ Seeding failed: {str(e)}")
        raise
    finally:
        db.close()