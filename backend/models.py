from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from .database import Base

# Association table for Pizza-Topping many-to-many relationship
pizza_toppings = Table(
    "pizza_toppings",
    Base.metadata,
    Column("pizza_id", Integer, ForeignKey("pizzas.id"), primary_key=True),
    Column("topping_id", Integer, ForeignKey("toppings.id"), primary_key=True),
)

class Topping(Base):
    __tablename__ = "toppings"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

class Pizza(Base):
    __tablename__ = "pizzas"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    toppings = relationship(
        "Topping", secondary=pizza_toppings, back_populates="pizzas"
    )

Topping.pizzas = relationship(
    "Pizza", secondary=pizza_toppings, back_populates="toppings"
)
