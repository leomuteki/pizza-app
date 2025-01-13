from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from . import models, schemas, crud
from .database import engine, SessionLocal
from fastapi.middleware.cors import CORSMiddleware

# Create the database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoints for toppings
@app.get("/toppings", response_model=List[schemas.Topping])
def read_toppings(db: Session = Depends(get_db)):
    return crud.get_toppings(db)

@app.post("/toppings", response_model=schemas.Topping)
def create_topping(topping: schemas.ToppingCreate, db: Session = Depends(get_db)):
    db_topping = crud.get_topping_by_name(db, name=topping.name)
    if db_topping:
        raise HTTPException(status_code=400, detail="Topping already exists")
    return crud.create_topping(db, topping)

@app.put("/toppings/{topping_id}", response_model=schemas.Topping)
def update_topping(topping_id: int, topping: schemas.ToppingCreate, db: Session = Depends(get_db)):
    db_topping = crud.get_topping_by_id(db, topping_id)
    if not db_topping:
        raise HTTPException(status_code=404, detail="Topping not found")
    if db_topping.name != topping.name and crud.get_topping_by_name(db, topping.name):
        raise HTTPException(status_code=400, detail="Topping with this name already exists")
    return crud.update_topping(db, topping_id, topping)

@app.delete("/toppings/{topping_id}", response_model=schemas.Topping)
def delete_topping(topping_id: int, db: Session = Depends(get_db)):
    return crud.delete_topping(db, topping_id)

# Endpoints for pizzas
@app.get("/pizzas", response_model=List[schemas.Pizza])
def read_pizzas(db: Session = Depends(get_db)):
    return crud.get_pizzas(db)

@app.post("/pizzas", response_model=schemas.Pizza)
def create_pizza(pizza: schemas.PizzaCreate, db: Session = Depends(get_db)):
    return crud.create_pizza(db, pizza)

# Update a pizza
@app.put("/pizzas/{pizza_id}", response_model=schemas.Pizza)
def update_pizza(pizza_id: int, pizza: schemas.PizzaCreate, db: Session = Depends(get_db)):
    db_pizza = crud.get_pizza_by_id(db, pizza_id)
    if not db_pizza:
        raise HTTPException(status_code=404, detail="Pizza not found")
    if db_pizza.name != pizza.name and any(
        p.name == pizza.name for p in crud.get_pizzas(db)
    ):
        raise HTTPException(status_code=400, detail="Pizza with this name already exists")
    return crud.update_pizza(db, pizza_id, pizza)

# Delete a pizza
@app.delete("/pizzas/{pizza_id}", response_model=schemas.Pizza)
def delete_pizza(pizza_id: int, db: Session = Depends(get_db)):
    db_pizza = crud.get_pizza_by_id(db, pizza_id)
    if not db_pizza:
        raise HTTPException(status_code=404, detail="Pizza not found")
    return crud.delete_pizza(db, pizza_id)