from app.crud.base import CRUDBase
from app.models.partner import Partner, PartnerCategory
from app.schemas.partner import (
    PartnerCreate, PartnerUpdate,
    PartnerCategoryCreate, PartnerCategoryUpdate
)


class CRUDPartner(CRUDBase[Partner, PartnerCreate, PartnerUpdate]):
    pass


class CRUDPartnerCategory(CRUDBase[PartnerCategory, PartnerCategoryCreate, PartnerCategoryUpdate]):
    pass


crud_partner = CRUDPartner(Partner)
crud_partner_category = CRUDPartnerCategory(PartnerCategory)
