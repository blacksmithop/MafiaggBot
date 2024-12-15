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
  localStorage.setItem("cookie", data.cookie);
  localStorage.setItem("user_id", data.user_id);
  localStorage.setItem("user_name", data.user_name);
  localStorage.setItem("isAuthenticated", "true");
}

export function logout(): void {
  localStorage.removeItem('cookie'); // Clear token
  localStorage.removeItem("user_id");
  localStorage.removeItem("user_name");
  localStorage.removeItem('isAuthenticated'); // Clear auth state
  window.location.href = '/'; // Redirect
}
