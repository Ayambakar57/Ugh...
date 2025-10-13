from app.crud.base import CRUDBase
from app.models.product import Product, ProductCategory
from app.schemas.product import (
    ProductCreate, ProductUpdate,
    ProductCategoryCreate, ProductCategoryUpdate
)


class CRUDProduct(CRUDBase[Product, ProductCreate, ProductUpdate]):
    pass


class CRUDProductCategory(CRUDBase[ProductCategory, ProductCategoryCreate, ProductCategoryUpdate]):
    pass


crud_product = CRUDProduct(Product)
crud_product_category = CRUDProductCategory(ProductCategory)
