import { fetchWithAuth } from './api';
import { API_ENDPOINTS } from './config';
import type { GameLobby } from '../types/Stats';

export async function getLobbies(params: {
  page?: number;
  limit?: number;
  status?: 'active' | 'waiting';
}) {
  const queryParams = new URLSearchParams();
  Object.entries(params).forEach(([key, value]) => {
    if (value) queryParams.append(key, value.toString());
  });

  return fetchWithAuth<GameLobby[]>(
    `${API_ENDPOINTS.lobbies}?${queryParams.toString()}`
  );
}

export async function getLobbyById(id: string) {
  return fetchWithAuth<GameLobby>(`${API_ENDPOINTS.lobbies}/${id}`);
}