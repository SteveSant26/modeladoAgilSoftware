from pydantic import BaseModel
    
from .fruit_response import FruitResponseSchema

class FruitsSchema(BaseModel):
    fruits: list[FruitResponseSchema]
    