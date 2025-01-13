import axios from 'axios';
import { Pizza, Topping } from './types';

// Create an Axios instance
const api = axios.create({
  baseURL: process.env.NEXT_PUBLIC_API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Fetch all pizzas
export async function getPizzas(): Promise<Pizza[]> {
  const response = await api.get('/pizzas');
  return response.data;
}

// Create a new pizza
export async function createPizza(pizza: Omit<Pizza, 'id'>): Promise<Pizza> {
  const response = await api.post('/pizzas', pizza);
  return response.data;
}

export const updatePizza = async (id: number, payload: { name: string; toppings: number[] }) => {
  try {
    const response = await api.put(`/pizzas/${id}`, payload);
    return response.data;
  } catch (error) {
    console.error("Failed to update pizza:", error);
    throw error;
  }
};

// Delete a pizza
export async function deletePizza(pizzaId: number): Promise<Pizza> {
  const response = await api.delete(`/pizzas/${pizzaId}`);
  return response.data;
}

// Fetch all toppings
export async function getToppings(): Promise<Topping[]> {
  const response = await api.get('/toppings');
  return response.data;
}

// Create a new topping
export async function createTopping(
  topping: Omit<Topping, 'id'>
): Promise<Topping> {
  const response = await api.post('/toppings', topping);
  return response.data;
}

// Update an existing topping
export async function updateTopping(
  toppingId: number,
  topping: Omit<Topping, 'id'>
): Promise<Topping> {
  const response = await api.put(`/toppings/${toppingId}`, topping);
  return response.data;
}

// Delete a topping
export async function deleteTopping(toppingId: number): Promise<Topping> {
  const response = await api.delete(`/toppings/${toppingId}`);
  return response.data;
}

export default api;
