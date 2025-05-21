from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload
from apps.fruits.schemas import FruitsSchema, FruitResponseSchema, FruitCreateSchema
from apps.fruits.models import FruitModel

from apps.category.models import CategoryModel

from db import get_db


fruit_router = APIRouter()


@fruit_router.get("/fruits", response_model=FruitsSchema)
def get_fruits(db: Session = Depends(get_db)) -> FruitsSchema:
    fruits = db.query(FruitModel).all()

    return FruitsSchema(
        fruits=[FruitResponseSchema.model_validate(fruit) for fruit in fruits]
    )


@fruit_router.get("/fruits/{fruit_id}", response_model=FruitResponseSchema)
def get_fruit(fruit_id: int, db: Session = Depends(get_db)):
    fruit = db.query(FruitModel).filter(FruitModel.id == fruit_id).first()
    if not fruit:
        raise HTTPException(status_code=404, detail="Fruit not found")
    return fruit


@fruit_router.post("/fruits", response_model=FruitResponseSchema)
def add_fruit(fruit: FruitCreateSchema, db: Session = Depends(get_db)):
    category = (
        db.query(CategoryModel).filter(CategoryModel.id == fruit.category_id).first()
    )

    existing_fruit = db.query(FruitModel).filter(FruitModel.name == fruit.name).first()
    if existing_fruit:
        raise HTTPException(status_code=409, detail="Fruit already added")

    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    new_fruit = FruitModel(
        name=fruit.name, category_id=fruit.category_id, price=fruit.price
    )
    db.add(new_fruit)
    db.commit()
    db.refresh(new_fruit)
    return new_fruit


@fruit_router.put("/fruits/{fruit_id}", response_model=FruitResponseSchema)
def update_fruit(
    fruit_id: int, fruit_data: FruitCreateSchema, db: Session = Depends(get_db)
):
    fruit = db.query(FruitModel).filter(FruitModel.id == fruit_id).first()

    if not fruit:
        raise HTTPException(status_code=404, detail="Fruit not found")

    fruit.name = fruit_data.name
    fruit.category_id = fruit_data.category_id
    fruit.price = fruit_data.price

    db.commit()
    db.refresh(fruit)
    return fruit


@fruit_router.delete("/fruits/{fruit_id}", response_model=FruitResponseSchema)
def delete_fruit(fruit_id: int, db: Session = Depends(get_db)):
    fruit = (
        db.query(FruitModel)
        .options(joinedload(FruitModel.category))
        .filter(FruitModel.id == fruit_id)
        .first()
    )

    if not fruit:
        raise HTTPException(status_code=404, detail="Fruit not found")

    db.delete(fruit)
    db.commit()

    return fruit
