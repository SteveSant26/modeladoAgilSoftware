from .fruit_base import FruitBase
from typing import Optional
from apps.category.schemas import CategoryResponseSchema

class FruitResponseSchema(FruitBase):
    id: int
    category: Optional[CategoryResponseSchema] 

    class Config:
        from_attributes = True        
