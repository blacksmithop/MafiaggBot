export type NotificationType = 'achievement' | 'game_report' | 'invite';

export interface Notification {
  id: string;
  type: NotificationType;
  title: string;
  message: string;
  datetime: Date;
  read: boolean;
  data?: any;
}

export interface GameInvite {
  lobbyId: string;
  lobbyName: string;
  host: string;
  playerCount: number;
  maxPlayers: number;
}