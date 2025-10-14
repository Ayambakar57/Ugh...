from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.deps import get_current_user
from app.routers import (
    company, branch, warehouse, product,
    partner, province, district, subdistrict,
    ward, zipcode, user, location, auth
)

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    debug=settings.DEBUG,
    redirect_slashes=False
)



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])


app.include_router(
    user.router, 
    prefix="/api/users", 
    tags=["Users"],
    dependencies=[Depends(get_current_user)]
)
app.include_router(
    company.router, 
    prefix="/api/companies", 
    tags=["Companies"],
    dependencies=[Depends(get_current_user)]
)
app.include_router(
    branch.router, 
    prefix="/api/branches", 
    tags=["Branches"],
    dependencies=[Depends(get_current_user)]
)
app.include_router(
    warehouse.router, 
    prefix="/api/warehouses", 
    tags=["Warehouses"],
    dependencies=[Depends(get_current_user)]
)
app.include_router(
    product.router, 
    prefix="/api/products", 
    tags=["Products"],
    dependencies=[Depends(get_current_user)]
)
app.include_router(
    partner.router, 
    prefix="/api/partners", 
    tags=["Partners"],
    dependencies=[Depends(get_current_user)]
)
app.include_router(
    location.router, 
    prefix="/api/locations", 
    tags=["Locations"],
    dependencies=[Depends(get_current_user)]
)
app.include_router(
    province.router, 
    prefix="/api/provinces", 
    tags=["Provinces"],
    dependencies=[Depends(get_current_user)]
)
app.include_router(
    district.router, 
    prefix="/api/districts", 
    tags=["Districts"],
    dependencies=[Depends(get_current_user)]
)
app.include_router(
    subdistrict.router, 
    prefix="/api/subdistricts", 
    tags=["Subdistricts"],
    dependencies=[Depends(get_current_user)]
)
app.include_router(
    ward.router, 
    prefix="/api/wards", 
    tags=["Wards"],
    dependencies=[Depends(get_current_user)]
)
app.include_router(
    zipcode.router, 
    prefix="/api/zipcodes", 
    tags=["Zipcodes"],
    dependencies=[Depends(get_current_user)]
)



@app.get("/")
def root():
    return {
        "message": "Welcome to FastAPI Application",
        "version": settings.APP_VERSION,
        "docs": "/docs",
        "redoc": "/redoc"
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}
