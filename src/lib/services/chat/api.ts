import { fetchWithAuth } from '../api';
import { API_ENDPOINTS } from '../config';
import type { Chat, Message } from '../../types/Chat';
import { formatChatMessages } from './utils';

export async function fetchRecentMessages(): Promise<Chat[]> {
  const response = await fetchWithAuth<Chat[]>(API_ENDPOINTS.recent_chat);
  return response;
}

export async function fetchChatMessages(senderId: number, receiverId: number | string): Promise<Message[]> {
  if (receiverId === 'Mafia Assistant') {
    return fetchChatbotMessages();
  }

  const response = await fetchWithAuth(API_ENDPOINTS.chat_from_user, {
    method: "POST",
    body: JSON.stringify({ senderId, receiverId }),
  });

  if (!response.ok) {
    throw new Error(`Failed to load chat messages: ${response.statusText}`);
  }

  const messages = await response.json();
  return formatChatMessages(messages);
}

async function fetchChatbotMessages(): Promise<Message[]> {
  const response = await fetchWithAuth(API_ENDPOINTS.chatbot, {
    method: "POST",
    body: JSON.stringify({ message: "Hello" }),
  });

  if (!response.ok) {
    throw new Error(`Failed to load chatbot messages: ${response.statusText}`);
  }

  const messages = await response.json();
  return formatChatMessages(messages);
}