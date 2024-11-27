export interface PlayerStats {
  username: string;
  totalGames: number;
  winRate: number;
  townWinRate: number;
  mafiaWinRate: number;
  neutralWinRate: number;
}

export interface RoleStats {
  name: string;
  alignment: 'Town' | 'Mafia' | 'Neutral';
  winRate: number;
  totalGames: number;
}

export interface FactionStats {
  name: string;
  winRate: number;
  totalGames: number;
}