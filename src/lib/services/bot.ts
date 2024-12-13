import { fetchWithAuth } from './api';
import { API_ENDPOINTS } from './config';
import type { BotRoom } from '../types/Bot';

export async function getBotRooms() {
  return fetchWithAuth<BotRoom[]>(API_ENDPOINTS.bot);
}

export async function createBotRoom(roomData: Omit<BotRoom, 'id'>) {
  return fetchWithAuth<BotRoom>(API_ENDPOINTS.bot, {
    method: 'POST',
    body: JSON.stringify(roomData)
  });
}

export async function updateBotRoom(id: string, roomData: Partial<BotRoom>) {
  return fetchWithAuth<BotRoom>(`${API_ENDPOINTS.bot}/${id}`, {
    method: 'PATCH',
    body: JSON.stringify(roomData)
  });
}

export async function deleteBotRoom(id: string) {
  return fetchWithAuth(`${API_ENDPOINTS.bot}/${id}`, {
    method: 'DELETE'
  });
}