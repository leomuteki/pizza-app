import unittest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .main import app
from .database import Base, get_db
from .schemas import ToppingCreate, PizzaCreate
from .models import Topping, Pizza

# Setup an SQLite test database
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency override to use the test database
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

# Apply the override
app.dependency_overrides[get_db] = override_get_db

# Create tables for the test database
Base.metadata.create_all(bind=engine)

# Test client
client = TestClient(app)

class TestApp(unittest.TestCase):
    def setUp(self):
        """Create a fresh database before each test."""
        # Drop and recreate the database schema
        Base.metadata.drop_all(bind=engine)
        Base.metadata.create_all(bind=engine)
        # Create a new session for the test
        self.db = TestingSessionLocal()

        # Ensure the database is empty by deleting all rows in the tables
        self.db.query(Topping).delete()
        self.db.query(Pizza).delete()
        self.db.commit()

    def tearDown(self):
        """Close the database session after each test."""
        self.db.close()

    def test_create_topping(self):
        """Test the creation of a topping."""
        response = client.post("/toppings", json={"name": "Tomato"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["name"], "Tomato")

    def test_get_toppings(self):
        """Test retrieving toppings."""
        client.post("/toppings", json={"name": "Tomato"})
        client.post("/toppings", json={"name": "Mushroom"})
        response = client.get("/toppings")
        self.assertEqual(response.status_code, 200)
        toppings = response.json()
        self.assertEqual(len(toppings), 2)

    def test_update_topping(self):
        """Test updating a topping."""
        response = client.post("/toppings", json={"name": "Mushroom"})
        topping_id = response.json()["id"]
        update_response = client.put(f"/toppings/{topping_id}", json={"name": "Olive"})
        self.assertEqual(update_response.status_code, 200)
        self.assertEqual(update_response.json()["name"], "Olive")

    def test_delete_topping(self):
        """Test deleting a topping."""
        response = client.post("/toppings", json={"name": "Mushroom"})
        topping_id = response.json()["id"]
        delete_response = client.delete(f"/toppings/{topping_id}")
        self.assertEqual(delete_response.status_code, 200)
        self.assertEqual(delete_response.json()["name"], "Mushroom")

    def test_create_pizza(self):
        """Test creating a pizza with toppings."""
        client.post("/toppings", json={"name": "Tomato"})
        client.post("/toppings", json={"name": "Cheese"})
        response = client.post("/pizzas", json={"name": "Margherita1", "toppings": [1, 2]})
        self.assertEqual(response.status_code, 200)
        pizza = response.json()
        self.assertEqual(pizza["name"], "Margherita1")
        self.assertEqual(len(pizza["toppings"]), 2)

    def test_update_pizza(self):
        """Test updating a pizza."""
        client.post("/toppings", json={"name": "Tomato"})
        client.post("/toppings", json={"name": "Cheese"})
        pizza_response = client.post("/pizzas", json={"name": "Veggie", "toppings": [1]})
        pizza_id = pizza_response.json()["id"]
        update_response = client.put(f"/pizzas/{pizza_id}", json={"name": "Deluxe Veggie", "toppings": [1, 2]})
        self.assertEqual(update_response.status_code, 200)
        updated_pizza = update_response.json()
        self.assertEqual(updated_pizza["name"], "Deluxe Veggie")
        self.assertEqual(len(updated_pizza["toppings"]), 2)

    def test_delete_pizza(self):
        """Test deleting a pizza."""
        client.post("/toppings", json={"name": "Tomato"})
        pizza_response = client.post("/pizzas", json={"name": "Plain", "toppings": [1]})
        pizza_id = pizza_response.json()["id"]
        delete_response = client.delete(f"/pizzas/{pizza_id}")
        self.assertEqual(delete_response.status_code, 200)
        self.assertEqual(delete_response.json()["name"], "Plain")

if __name__ == "__main__":
    unittest.main()
