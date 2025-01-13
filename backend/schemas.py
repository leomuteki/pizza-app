from pydantic import BaseModel
from typing import List

class ToppingBase(BaseModel):
    name: str

class ToppingCreate(ToppingBase):
    pass

class Topping(ToppingBase):
    id: int

    class Config:
        from_attributes = True

class PizzaBase(BaseModel):
    name: str

class PizzaCreate(PizzaBase):
    toppings: List[int]  # List of topping IDs

class Pizza(PizzaBase):
    id: int
    toppings: List[Topping]

    class Config:
        from_attributes = True
