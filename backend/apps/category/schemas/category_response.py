from .category_base import CategoryBase

class CategoryResponseSchema(CategoryBase):
    id: int

    class Config:
        from_attributes = True        
