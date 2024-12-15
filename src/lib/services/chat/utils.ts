import type { Message } from '../../types/Chat';

export function formatChatMessages(messages: any[]): Message[] {
  return messages.map(message => ({
    id: message.id || Date.now().toString(),
    sender: message.senderId,
    content: message.content,
    timestamp: new Date(message.timestamp),
    type: 'text'
  }));
}

export function formatTimestamp(date: Date): string {
  return date.toLocaleTimeString([], {
    hour: '2-digit',
    minute: '2-digit'
  });
}