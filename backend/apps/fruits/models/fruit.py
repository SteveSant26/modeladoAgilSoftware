from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from db import Base


class FruitModel(Base):
    __tablename__ = "fruits"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, unique=True, index=True)
    price = Column(Float, nullable=True)
    category_id = Column(Integer, ForeignKey("categories.id"))

    category = relationship("CategoryModel", back_populates="fruits")
