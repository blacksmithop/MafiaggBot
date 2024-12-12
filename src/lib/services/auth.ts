import { fetchWithAuth } from './api';
import { API_BASE_URL } from './config';

export async function login(username: string, password: string): Promise<void> {
  const response = await fetch(`${API_BASE_URL}/login`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ username, password }),
  });

  if (!response.ok) {
    const error = await response.json();
    throw new Error(error.message || 'Login failed');
  }

  const data = await response.json();
  localStorage.setItem('auth_token', data.token); // Store token
  localStorage.setItem('isAuthenticated', 'true'); // Update auth state
}

export function logout(): void {
  localStorage.removeItem('auth_token'); // Clear token
  localStorage.removeItem('isAuthenticated'); // Clear auth state
  window.location.href = '/'; // Redirect
}
