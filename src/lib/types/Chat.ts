export interface Chat {
  id: string;
  username: string;
  avatar: string;
  lastMessage: string;
  timestamp: Date;
  unread: number;
}

export interface Message {
  id: string;
  sender: string;
  content: string;
  timestamp: Date;
  type: 'text' | 'emoji';
}