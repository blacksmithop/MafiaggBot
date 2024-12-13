import { fetchWithAuth } from "./api";
import { API_ENDPOINTS } from "./config";
import type { Message } from "../types/Chat";

export async function loadChatMessages(id: string) {
    return fetchWithAuth<Message>(`${API_ENDPOINTS.load_chat_messages}`);
}
