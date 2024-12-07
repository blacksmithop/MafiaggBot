import { fetchWithAuth } from './api';
import { API_BASE_URL, } from './config';

import type { LoginResponse } from '../types/Auth';

export async function login(username: string, password: string): Promise<LoginResponse> {
  const response = await fetch(`${API_BASE_URL}/login`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ username, password })
  });

  if (!response.ok) {
    const error = await response.json();
    throw new Error(error.message || 'Login failed');
  }

  const data = await response.json();
  console.log(data)
  localStorage.setItem("isAuthenticated", "true")
  return data;
}

export function logout() {
  localStorage.removeItem('userSessionToken');
  localStorage.removeItem('isAuthenticated');
  window.location.href = '/';
}