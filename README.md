# FastAPI Backend Application

A complete FastAPI backend application with SQLAlchemy ORM, Alembic migrations, and full CRUD operations for all database entities.

## Project Structure

```
TEST_BE/
├── alembic/                    # Alembic migration files
│   ├── versions/              # Migration versions
│   └── env.py                 # Alembic environment configuration
├── app/
│   ├── crud/                  # CRUD operations
│   │   ├── base.py           # Base CRUD class
│   │   ├── company.py        # Company CRUD
│   │   ├── branch.py         # Branch CRUD
│   │   ├── warehouse.py      # Warehouse CRUD
│   │   ├── product.py        # Product CRUD
│   │   ├── partner.py        # Partner CRUD
│   │   ├── location.py       # Location CRUD (provinces, districts, etc.)
│   │   └── user.py           # User CRUD
│   ├── models/               # SQLAlchemy models
│   │   ├── company.py        # Company & CompanyCategory models
│   │   ├── branch.py         # Branch model
│   │   ├── warehouse.py      # Warehouse model
│   │   ├── product.py        # Product & ProductCategory models
│   │   ├── partner.py        # Partner & PartnerCategory models
│   │   ├── location.py       # Location models (provinces, districts, etc.)
│   │   └── user.py           # User model
│   ├── routers/              # API endpoints
│   │   ├── company.py        # Company endpoints
│   │   ├── branch.py         # Branch endpoints
│   │   ├── warehouse.py      # Warehouse endpoints
│   │   ├── product.py        # Product endpoints
│   │   ├── partner.py        # Partner endpoints
│   │   ├── province.py       # Province endpoints
│   │   ├── district.py       # District endpoints
│   │   ├── subdistrict.py    # Subdistrict endpoints
│   │   ├── ward.py           # Ward endpoints
│   │   ├── zipcode.py        # Zipcode endpoints
│   │   └── user.py           # User endpoints
│   ├── schemas/              # Pydantic schemas
│   │   ├── company.py
│   │   ├── branch.py
│   │   ├── warehouse.py
│   │   ├── product.py
│   │   ├── partner.py
│   │   ├── location.py
│   │   └── user.py
│   ├── config.py             # Application configuration
│   └── database.py           # Database connection setup
├── main.py                   # FastAPI application entry point
├── alembic.ini              # Alembic configuration
├── requirements.txt         # Python dependencies
└── .env                     # Environment variables

```

## Database Tables

The application manages the following 14 database tables:

1. **companies** - Company information
2. **company_categories** - Company category master data
3. **branches** - Branch information
4. **warehouses** - Warehouse information
5. **products** - Product information
6. **product_categories** - Product category master data
7. **partners** - Partner information
8. **partner_categories** - Partner category master data
9. **master_provinces** - Province master data
10. **master_districts** - District master data
11. **master_subdistricts** - Subdistrict master data
12. **master_wards** - Ward master data
13. **master_zipcodes** - Zipcode master data
14. **users** - User information

## Setup Instructions

### 1. Install Dependencies

First, activate your virtual environment and install the required packages:

```bash
# Activate virtual environment (Windows)
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure Environment Variables

Update the `.env` file with your Neon PostgreSQL database credentials:

```env
DATABASE_URL=postgresql://user:password@ep-xxxxx.region.aws.neon.tech/dbname?sslmode=require
APP_NAME=FastAPI Application
APP_VERSION=1.0.0
DEBUG=True
SECRET_KEY=your-secret-key-here-change-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 3. Create Initial Migration

Generate the initial migration based on your models:

```bash
alembic revision --autogenerate -m "Initial migration"
```

### 4. Run Migrations

Apply the migrations to create all database tables:

```bash
alembic upgrade head
```

### 5. Run the Application

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

The API will be available at:
- **API**: http://localhost:8000
- **Interactive Docs (Swagger)**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## API Endpoints

All endpoints follow RESTful conventions with full CRUD operations:

### Companies
- `GET /api/companies/` - List all companies
- `GET /api/companies/{id}` - Get a specific company
- `POST /api/companies/` - Create a new company
- `PUT /api/companies/{id}` - Update a company
- `DELETE /api/companies/{id}` - Delete a company

### Company Categories
- `GET /api/companies/categories/` - List all company categories
- `GET /api/companies/categories/{id}` - Get a specific company category
- `POST /api/companies/categories/` - Create a new company category
- `PUT /api/companies/categories/{id}` - Update a company category
- `DELETE /api/companies/categories/{id}` - Delete a company category

### Branches
- `GET /api/branches/` - List all branches
- `GET /api/branches/{id}` - Get a specific branch
- `POST /api/branches/` - Create a new branch
- `PUT /api/branches/{id}` - Update a branch
- `DELETE /api/branches/{id}` - Delete a branch

### Warehouses
- `GET /api/warehouses/` - List all warehouses
- `GET /api/warehouses/{id}` - Get a specific warehouse
- `POST /api/warehouses/` - Create a new warehouse
- `PUT /api/warehouses/{id}` - Update a warehouse
- `DELETE /api/warehouses/{id}` - Delete a warehouse

### Products
- `GET /api/products/` - List all products
- `GET /api/products/{id}` - Get a specific product
- `POST /api/products/` - Create a new product
- `PUT /api/products/{id}` - Update a product
- `DELETE /api/products/{id}` - Delete a product

### Product Categories
- `GET /api/products/categories/` - List all product categories
- `GET /api/products/categories/{id}` - Get a specific product category
- `POST /api/products/categories/` - Create a new product category
- `PUT /api/products/categories/{id}` - Update a product category
- `DELETE /api/products/categories/{id}` - Delete a product category

### Partners
- `GET /api/partners/` - List all partners
- `GET /api/partners/{id}` - Get a specific partner
- `POST /api/partners/` - Create a new partner
- `PUT /api/partners/{id}` - Update a partner
- `DELETE /api/partners/{id}` - Delete a partner

### Partner Categories
- `GET /api/partners/categories/` - List all partner categories
- `GET /api/partners/categories/{id}` - Get a specific partner category
- `POST /api/partners/categories/` - Create a new partner category
- `PUT /api/partners/categories/{id}` - Update a partner category
- `DELETE /api/partners/categories/{id}` - Delete a partner category

### Location Master Data
- **Provinces**: `/api/provinces/`
- **Districts**: `/api/districts/`
- **Subdistricts**: `/api/subdistricts/`
- **Wards**: `/api/wards/`
- **Zipcodes**: `/api/zipcodes/`

All location endpoints support the same CRUD operations.

### Users
- `GET /api/users/` - List all users
- `GET /api/users/{id}` - Get a specific user
- `POST /api/users/` - Create a new user
- `PUT /api/users/{id}` - Update a user
- `DELETE /api/users/{id}` - Delete a user

## Features

✅ **Complete CRUD Operations** - Full Create, Read, Update, Delete for all entities  
✅ **UUID Primary Keys** - All tables use UUID for primary keys  
✅ **SQLAlchemy ORM** - Type-safe database operations  
✅ **Pydantic Validation** - Request/response validation  
✅ **Alembic Migrations** - Version-controlled database schema  
✅ **Neon PostgreSQL** - Cloud database ready  
✅ **Auto-generated API Docs** - Swagger UI and ReDoc  
✅ **CORS Enabled** - Ready for frontend integration  
✅ **Relationship Management** - Foreign key constraints and relationships  

## Migration Commands

```bash
# Create a new migration
alembic revision --autogenerate -m "description"

# Apply migrations
alembic upgrade head

# Rollback last migration
alembic downgrade -1

# View migration history
alembic history

# View current version
alembic current
```

## Development

The project uses:
- **FastAPI** - Modern web framework
- **SQLAlchemy 2.0** - SQL toolkit and ORM
- **Alembic** - Database migration tool
- **Pydantic v2** - Data validation
- **Uvicorn** - ASGI server
- **PostgreSQL** - Database (via Neon)

## Notes

- All models use UUID as primary keys
- Timestamps are automatically managed with `server_default` and `onupdate`
- The database URL must include `?sslmode=require` for Neon PostgreSQL
- Password fields in User model should be hashed before storing (consider adding password hashing utility)
