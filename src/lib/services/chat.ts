import { fetchWithAuth } from "./api";
import { API_BASE_URL, API_ENDPOINTS } from "./config";
import type { Chat, Message } from "../types/Chat";


export async function loadRecentMessages(): Promise<Chat[]> {
  const response = await fetchWithAuth<Chat[]>(`${API_ENDPOINTS.recent_chat}`);
  
  return response.map((message) => ({
    ...message,
    timestamp: new Date(message.timestamp),
  }));
}


export async function loadChatMessages(
  senderId: number,
  receiverId: number
): Promise<Message[]> {
  const response = await fetchWithAuth(`${API_ENDPOINTS.chat_from_user}`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ senderId, receiverId }),
  });

  if (!response.ok) {
    throw new Error(`Failed to load chat messages: ${response.statusText}`);
  }

  const messages: Message[] = await response.json();

  return messages.map((message) => ({
    ...message,
    timestamp: new Date(message.timestamp),
  }));
}
