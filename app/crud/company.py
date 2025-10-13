from app.crud.base import CRUDBase
from app.models.company import Company, CompanyCategory
from app.schemas.company import (
    CompanyCreate, CompanyUpdate,
    CompanyCategoryCreate, CompanyCategoryUpdate
)


class CRUDCompany(CRUDBase[Company, CompanyCreate, CompanyUpdate]):
    pass


class CRUDCompanyCategory(CRUDBase[CompanyCategory, CompanyCategoryCreate, CompanyCategoryUpdate]):
    pass


crud_company = CRUDCompany(Company)
crud_company_category = CRUDCompanyCategory(CompanyCategory)
