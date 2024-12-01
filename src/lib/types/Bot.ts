export interface BotRoom {
  id: string;
  name: string;
  deck: string;
  playerCount: number;
  status: 'active' | 'inactive';
  uptime: string;
  roles?: string[];
}