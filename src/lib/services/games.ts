import { fetchWithAuth } from './api';
import { API_ENDPOINTS } from './config';

export interface GameStats {
  id: string;
  date: string;
  players: Array<{
    username: string;
    role: string;
    alignment: string;
    result: 'win' | 'loss';
  }>;
  setup: {
    name: string;
    roles: string[];
  };
  duration: number;
  winner: 'town' | 'mafia' | 'neutral';
}

export async function getGameStats(gameId: string) {
  return fetchWithAuth<GameStats>(`${API_ENDPOINTS.games}/${gameId}`);
}

export async function getRecentGames(params: {
  page?: number;
  limit?: number;
  username?: string;
}) {
  const queryParams = new URLSearchParams();
  Object.entries(params).forEach(([key, value]) => {
    if (value) queryParams.append(key, value.toString());
  });

  return fetchWithAuth<GameStats[]>(
    `${API_ENDPOINTS.games}/recent?${queryParams.toString()}`
  );
}