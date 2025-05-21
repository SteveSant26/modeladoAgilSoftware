from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from db import Base


class CategoryModel(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, unique=True, index=True)

    fruits = relationship("FruitModel", back_populates="category")


