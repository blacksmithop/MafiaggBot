export const API_BASE_URL = 'http://localhost';

export const API_ENDPOINTS = {
  lobbies: '/get_rooms',
  players: '/players',
  games: '/games',
  notifications: '/notifications',
  bot: '/bot',
  load_chat_messages: '/load_chat_messages',
} as const;

export const DEFAULT_HEADERS = {
  'Content-Type': 'application/json',
};

export type ApiResponse<T> = {
  data: T;
  error?: string;
  meta?: {
    total: number;
    page: number;
    limit: number;
  };
};
