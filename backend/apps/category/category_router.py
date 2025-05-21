from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import get_db
from .models import CategoryModel
from .schemas import CategoriesSchema, CategoryCreateSchema, CategoryResponseSchema

category_router = APIRouter()


@category_router.get("/categories", response_model=CategoriesSchema)
def get_categories(db: Session = Depends(get_db)):
    categories = db.query(CategoryModel).all()
    return CategoriesSchema(
        categories=[
            CategoryResponseSchema.model_validate(category) for category in categories
        ]
    )


@category_router.get("/categories/{category_id}", response_model=CategoryResponseSchema)
def get_category(category_id: int, db: Session = Depends(get_db)):
    category = db.query(CategoryModel).filter(CategoryModel.id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category


@category_router.post("/categories", response_model=CategoryResponseSchema)
def create_category(category: CategoryCreateSchema, db: Session = Depends(get_db)):
    new_category = CategoryModel(name=category.name)
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category


@category_router.put("/categories/{category_id}", response_model=CategoryResponseSchema)
def update_category(
    category_id: int, category_data: CategoryCreateSchema, db: Session = Depends(get_db)
):
    category = db.query(CategoryModel).filter(CategoryModel.id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    category.name = category_data.name
    db.commit()
    db.refresh(category)
    return category


@category_router.delete("/categories/{category_id}")
def delete_category(category_id: int, db: Session = Depends(get_db)):
    category = db.query(CategoryModel).filter(CategoryModel.id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    db.delete(category)
    db.commit()
    return {"message": "Category deleted successfully"}
