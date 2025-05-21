from pydantic import BaseModel
    
from .category_response import CategoryResponseSchema

class CategoriesSchema(BaseModel):
    categories: list[CategoryResponseSchema]
    