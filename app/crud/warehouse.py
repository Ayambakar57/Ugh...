from app.crud.base import CRUDBase
from app.models.warehouse import Warehouse
from app.schemas.warehouse import WarehouseCreate, WarehouseUpdate


class CRUDWarehouse(CRUDBase[Warehouse, WarehouseCreate, WarehouseUpdate]):
    pass


crud_warehouse = CRUDWarehouse(Warehouse)
