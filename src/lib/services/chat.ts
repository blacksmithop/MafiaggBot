import { fetchWithAuth } from "./api";
import { API_BASE_URL, API_ENDPOINTS } from "./config";
import type { Chat, Message } from "../types/Chat";

export async function loadRecentMessages(): Promise<Chat[]> {
  const response = await fetchWithAuth<Chat[]>(`${API_ENDPOINTS.recent_chat}`);
  
  // Add chatbot to the list
  const chatbot: Chat = {
    _id: 'chatbot',
    senderId: 'Mafia Assistant',
    receiverId: '',
    content: 'Hello! I can help you with game strategies and rules.',
    timestamp: new Date()
  };

  return [chatbot, ...response.map((message) => ({
    ...message,
    timestamp: new Date(message.timestamp),
  }))];
}

export async function loadChatMessages(
  senderId: number,
  receiverId: number | string
): Promise<Message[]> {
  // Handle chatbot messages separately
  if (receiverId === 'Mafia Assistant') {
    const response = await fetchWithAuth(`${API_ENDPOINTS.chatbot}`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Cookie": localStorage.getItem("cookie") || ""
      },
      body: JSON.stringify({ message: "Hello" }) // Initial greeting
    });
    if (!response.ok) {
      throw new Error(`Failed to load chatbot messages: ${response.statusText}`);
    }

    const messages: Chat[] = await response.json();
    return messages.map((message) => ({
      ...message,
      timestamp: new Date(message.timestamp),
    }));
  }

  // Regular user chat messages
  const response = await fetchWithAuth(`${API_ENDPOINTS.chat_from_user}`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Cookie": localStorage.getItem("cookie") || ""
    },
    body: JSON.stringify({ senderId, receiverId }),
  });

  const messages: Chat[] = await response
  // .json();
  return messages.map((message) => ({
    ...message,
    timestamp: new Date(message.timestamp),
  }));
}

export async function sendChatbotMessage(message: string): Promise<Message> {
  const response = await fetchWithAuth(`${API_ENDPOINTS.chatbot}`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Cookie": localStorage.getItem("cookie") || ""
    },
    body: JSON.stringify({ message })
  });

  if (!response.ok) {
    throw new Error(`Failed to send message to chatbot: ${response.statusText}`);
  }

  const data = await response.json();
  return {
    ...data,
    timestamp: new Date(data.timestamp)
  };
}