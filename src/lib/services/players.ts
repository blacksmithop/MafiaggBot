import { fetchWithAuth } from './api';
import { API_ENDPOINTS } from './config';
import type { PlayerReport, RegisteredPlayer, RegisteredPlayerReport, UnregisteredPlayer } from '../types/Stats';


export async function getPlayerById(player_id: number) {
  return fetchWithAuth<UnregisteredPlayer>(
    `${API_ENDPOINTS.players}/get_player_by_id/${player_id}`
  );
}

export async function getPlayerByName(username: string) {
  return fetchWithAuth<RegisteredPlayer[]>(
    `${API_ENDPOINTS.players}/get_player_by_name/${username}`
  );
}

export async function getPlayerReport(username: string) {
  return fetchWithAuth<RegisteredPlayerReport>(
    `${API_ENDPOINTS.players}/get_player_report/${username}`
  );
}

// export async function searchPlayers(query: string) {
//   return fetchWithAuth<PlayerStats[]>(
//     `${API_ENDPOINTS.players}/search?q=${encodeURIComponent(query)}`
//   );
// }