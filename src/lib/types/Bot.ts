export interface BotRoom {
    id: string; // Unique identifier
    deck: string;
    name: string; // Room name
    playerCount: number;
    roles: Array<object>;
    status: string;
    uptime: string;
  }
  