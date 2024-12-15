export interface Chat {
  senderId: number;
  receiverId: number;
  content: string;
  timestamp: Date;
}