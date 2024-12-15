export interface Chat {
  _id: string;
  senderId: number;
  receiverId: number;
  content: string;
  timestamp: Date;
}

export interface Message {
  id?: string;
  sender: number;
  content: string;
  timestamp: Date;
}