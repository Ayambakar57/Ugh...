"""
Script to verify if database indexes exist
"""
import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()

# Get database URL from environment
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    print("❌ ERROR: DATABASE_URL not found in .env file")
    exit(1)

print(f"Connecting to database...")
print(f"Database: {DATABASE_URL.split('@')[1] if '@' in DATABASE_URL else 'hidden'}")

engine = create_engine(DATABASE_URL)

query = """
SELECT 
    tablename,
    indexname,
    indexdef
FROM pg_indexes
WHERE schemaname = 'public' 
  AND indexname LIKE 'idx_%'
ORDER BY tablename, indexname;
"""

print("\n" + "="*80)
print("CHECKING DATABASE INDEXES")
print("="*80)

try:
    with engine.connect() as conn:
        result = conn.execute(text(query))
        rows = result.fetchall()
        
        if not rows:
            print("\n❌ NO CUSTOM INDEXES FOUND!")
            print("The migration did NOT create any indexes.")
            print("\nThis is why your queries are slow!")
        else:
            print(f"\n✅ Found {len(rows)} custom indexes:\n")
            
            current_table = None
            for row in rows:
                table, index, definition = row
                if table != current_table:
                    print(f"\n📋 Table: {table}")
                    current_table = table
                print(f"  ✓ {index}")
            
            print("\n" + "="*80)
            print(f"✅ TOTAL: {len(rows)} indexes found")
            
except Exception as e:
    print(f"\n❌ ERROR: {e}")
    print("\nMake sure your DATABASE_URL is correct in .env")

print("="*80)
