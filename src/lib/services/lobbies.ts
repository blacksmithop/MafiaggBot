import { fetchWithAuth } from './api';
import { API_ENDPOINTS } from './config';
import type { GameLobby } from '../types/Stats';

export async function getLobbies() {


  return fetchWithAuth<GameLobby[]>(
    API_ENDPOINTS.lobbies
  );
}

export async function getLobbyById(id: string) {
  return fetchWithAuth<GameLobby>(`${API_ENDPOINTS.lobbies}/${id}`);
}