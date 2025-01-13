'use client';

import React, { useEffect, useState } from 'react';
import {
  getPizzas,
  createPizza,
  updatePizza,
  deletePizza,
  getToppings,
  createTopping,
  deleteTopping,
} from '../lib/api';
import { Pizza, Topping } from '../lib/types';

export default function Page() {
  const [pizzas, setPizzas] = useState<Pizza[]>([]);
  const [toppings, setToppings] = useState<Topping[]>([]);
  const [newPizzaName, setNewPizzaName] = useState('');
  const [newToppingName, setNewToppingName] = useState('');
  const [selectedTopping, setSelectedTopping] = useState<number | null>(null);

  useEffect(() => {
    async function fetchData() {
      setPizzas(await getPizzas());
      setToppings(await getToppings());
    }
    fetchData();
  }, []);

  const handleAddPizza = async () => {
    if (!newPizzaName) return;
    const newPizza = await createPizza({ name: newPizzaName, toppings: [] });
    setPizzas([...pizzas, newPizza]);
    setNewPizzaName('');
  };

  const handleAddToppingToPizza = async (pizzaId: number) => {
    if (!selectedTopping) return;

    const pizza = pizzas.find((p) => p.id === pizzaId);
    if (!pizza) return;

    const payload = {
      name: pizza.name,
      toppings: [...pizza.toppings.map((t) => t.id), selectedTopping],
    };

    const updatedPizza = await updatePizza(pizzaId, payload);
    setPizzas(pizzas.map((p) => (p.id === pizzaId ? updatedPizza : p)));
    setSelectedTopping(null);
  };

  const handleRemoveToppingFromPizza = async (pizzaId: number, toppingId: number) => {
    const pizza = pizzas.find((p) => p.id === pizzaId);
    if (!pizza) return;

    const payload = {
      name: pizza.name,
      toppings: pizza.toppings.map((t) => t.id).filter((id) => id !== toppingId),
    };

    const updatedPizza = await updatePizza(pizzaId, payload);
    setPizzas(pizzas.map((p) => (p.id === pizzaId ? updatedPizza : p)));
  };

  const handleRemovePizza = async (id: number) => {
    await deletePizza(id);
    setPizzas(pizzas.filter((pizza) => pizza.id !== id));
  };

  const handleAddTopping = async () => {
    if (!newToppingName) return;
    const newTopping = await createTopping({ name: newToppingName });
    setToppings([...toppings, newTopping]);
    setNewToppingName('');
  };

  const handleDeleteTopping = async (toppingId: number) => {
    await deleteTopping(toppingId);
    setToppings(toppings.filter((t) => t.id !== toppingId));

    const updatedPizzas = pizzas.map((pizza) => ({
      ...pizza,
      toppings: pizza.toppings.filter((t) => t.id !== toppingId),
    }));
    setPizzas(updatedPizzas);
  };

  return (
    <div style={styles.container}>
      <h1 style={styles.title}>Pizza Management</h1>
      <h2 style={styles.subtitle}>Full Stack Developer Candidate - Emilio (&quot;Leo&quot;) Segovia</h2>

      <section style={styles.section}>
        <h2 style={styles.subtitle}>Pizzas</h2>
        <div style={styles.inputContainer}>
          <input
            style={styles.input}
            placeholder="New Pizza Name"
            value={newPizzaName}
            onChange={(e) => setNewPizzaName(e.target.value)}
          />
          <button style={styles.button} onClick={handleAddPizza}>
            Add Pizza
          </button>
        </div>
        <ul style={styles.list}>
          {pizzas.map((pizza) => (
            <li key={pizza.id} style={styles.card}>
              <h3 style={styles.cardTitle}>{pizza.name}</h3>
              <ul style={styles.toppingList}>
                {pizza.toppings.map((topping) => (
                  <li key={topping.id} style={styles.toppingItem}>
                    {topping.name}{' '}
                    <button
                      style={styles.removeButton}
                      onClick={() => handleRemoveToppingFromPizza(pizza.id, topping.id)}
                    >
                      Remove
                    </button>
                  </li>
                ))}
              </ul>
              <select
                style={styles.select}
                value={selectedTopping || ''}
                onChange={(e) => setSelectedTopping(Number(e.target.value))}
              >
                <option value="" disabled>
                  Select Topping
                </option>
                {toppings.map((topping) => (
                  <option key={topping.id} value={topping.id}>
                    {topping.name}
                  </option>
                ))}
              </select>
              <button style={styles.button} onClick={() => handleAddToppingToPizza(pizza.id)}>
                Add Topping
              </button>
              <button style={styles.dangerButton} onClick={() => handleRemovePizza(pizza.id)}>
                Remove Pizza
              </button>
            </li>
          ))}
        </ul>
      </section>

      <section style={styles.section}>
        <h2 style={styles.subtitle}>Toppings</h2>
        <div style={styles.inputContainer}>
          <input
            style={styles.input}
            placeholder="New Topping Name"
            value={newToppingName}
            onChange={(e) => setNewToppingName(e.target.value)}
          />
          <button style={styles.button} onClick={handleAddTopping}>
            Add Topping
          </button>
        </div>
        <ul style={styles.list}>
          {toppings.map((topping) => (
            <li key={topping.id} style={styles.card}>
              {topping.name}{' '}
              <button style={styles.dangerButton} onClick={() => handleDeleteTopping(topping.id)}>
                Delete
              </button>
            </li>
          ))}
        </ul>
      </section>
    </div>
  );
}

import { CSSProperties } from 'react';

const styles: { [key: string]: CSSProperties } = {
  container: {
    fontSize: '16px',
    fontFamily: 'Arial, sans-serif',
    padding: '20px',
    maxWidth: '800px',
    margin: '0 auto',
    backgroundColor: '#f5f5f5', // Light gray background
    color: '#000', // Black text
  },
  title: {
    fontSize: '24px',
    textAlign: 'center',
    color: '#000',
  },
  section: {
    marginBottom: '40px',
  },
  subtitle: {
    textAlign: 'center',
    color: '#000',
    borderBottom: '2px solid #ccc',
    paddingBottom: '5px',
  },
  inputContainer: {
    display: 'flex',
    gap: '10px',
    marginBottom: '20px',
  },
  input: {
    flex: 1,
    padding: '8px',
    borderRadius: '4px',
    border: '1px solid #ccc',
  },
  button: {
    padding: '8px 12px',
    backgroundColor: '#007BFF',
    color: '#fff',
    border: 'none',
    borderRadius: '4px',
    cursor: 'pointer',
  },
  dangerButton: {
    padding: '8px 12px',
    backgroundColor: '#dc3545',
    color: '#fff',
    border: 'none',
    borderRadius: '4px',
    cursor: 'pointer',
  },
  removeButton: {
    padding: '4px 8px',
    backgroundColor: '#ffc107',
    color: '#000',
    border: 'none',
    borderRadius: '4px',
    cursor: 'pointer',
  },
  list: {
    listStyleType: 'none',
    padding: 0,
  },
  card: {
    padding: '15px',
    marginBottom: '10px',
    border: '1px solid #ddd',
    borderRadius: '4px',
    backgroundColor: '#fff', // White cards on light gray background
  },
  cardTitle: {
    margin: '0 0 10px 0',
  },
  toppingList: {
    listStyleType: 'none',
    padding: 0,
    marginBottom: '10px',
  },
  toppingItem: {
    marginBottom: '5px',
  },
  select: {
    padding: '8px',
    borderRadius: '4px',
    border: '1px solid #ccc',
    marginBottom: '10px',
  },
};
