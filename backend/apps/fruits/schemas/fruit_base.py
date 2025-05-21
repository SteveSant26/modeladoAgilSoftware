from pydantic import BaseModel

class FruitBase(BaseModel):
    name: str
    price: float | None
