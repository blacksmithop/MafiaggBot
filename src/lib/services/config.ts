export const API_BASE_URL = 'http://localhost:8081';

export const API_ENDPOINTS = {
  lobbies: '/get_rooms',
  players: '/players',
  games: '/games',
  notifications: '/notifications',
  bot: '/bot',
  recent_chat: '/get_recent_messages',
  chat_from_user: '/get_chat_with_user'
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
