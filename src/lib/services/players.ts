import { fetchWithAuth } from './api';
import { API_ENDPOINTS } from './config';
import type { PlayerStats, PlayerReport } from '../types/Stats';

export async function getPlayerStats(username: string) {
  return fetchWithAuth<PlayerStats>(
    `${API_ENDPOINTS.players}/${username}/stats`
  );
}

export async function getPlayerReport(username: string) {
  return fetchWithAuth<PlayerReport>(
    `${API_ENDPOINTS.players}/${username}/report`
  );
}

export async function searchPlayers(query: string) {
  return fetchWithAuth<PlayerStats[]>(
    `${API_ENDPOINTS.players}/search?q=${encodeURIComponent(query)}`
  );
}