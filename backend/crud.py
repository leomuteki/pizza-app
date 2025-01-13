from sqlalchemy.orm import Session
from . import models, schemas

def get_toppings(db: Session):
    return db.query(models.Topping).all()

def get_topping_by_name(db: Session, name: str):
    return db.query(models.Topping).filter(models.Topping.name == name).first()

def get_topping_by_id(db: Session, topping_id: int):
    return db.query(models.Topping).filter(models.Topping.id == topping_id).first()

def create_topping(db: Session, topping: schemas.ToppingCreate):
    db_topping = models.Topping(name=topping.name)
    db.add(db_topping)
    db.commit()
    db.refresh(db_topping)
    return db_topping

def update_topping(db: Session, topping_id: int, topping: schemas.ToppingCreate):
    db_topping = db.query(models.Topping).filter(models.Topping.id == topping_id).first()
    db_topping.name = topping.name
    db.commit()
    db.refresh(db_topping)
    return db_topping

def delete_topping(db: Session, topping_id: int):
    topping = db.query(models.Topping).filter(models.Topping.id == topping_id).first()
    db.delete(topping)
    db.commit()
    return topping

def get_pizzas(db: Session):
    return db.query(models.Pizza).all()

def get_pizza_by_id(db: Session, pizza_id: int):
    return db.query(models.Pizza).filter(models.Pizza.id == pizza_id).first()

def create_pizza(db: Session, pizza: schemas.PizzaCreate):
    db_pizza = models.Pizza(name=pizza.name)
    db_pizza.toppings = db.query(models.Topping).filter(
        models.Topping.id.in_(pizza.toppings)
    ).all()
    db.add(db_pizza)
    db.commit()
    db.refresh(db_pizza)
    return db_pizza

def update_pizza(db: Session, pizza_id: int, pizza: schemas.PizzaCreate):
    db_pizza = db.query(models.Pizza).filter(models.Pizza.id == pizza_id).first()
    db_pizza.name = pizza.name
    db_pizza.toppings = db.query(models.Topping).filter(
        models.Topping.id.in_(pizza.toppings)
    ).all()
    db.commit()
    db.refresh(db_pizza)
    return db_pizza

def delete_pizza(db: Session, pizza_id: int):
    pizza = db.query(models.Pizza).filter(models.Pizza.id == pizza_id).first()
    db.delete(pizza)
    db.commit()
    return pizza