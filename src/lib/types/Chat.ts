export interface Chat {
  _id: string;
  senderId: string;
  receiverId: string;
  content: string;
  timestamp: Date;
}

export interface Message {
  id: string;
  sender: string;
  content: string;
  timestamp: Date;
  type: 'text' | 'emoji';
}