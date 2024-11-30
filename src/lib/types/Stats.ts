export interface PlayerStats {
  id: string;
  username: string;
  joinedDate: string;
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

export interface GameLobby {
  id: string;
  name: string;
  host: string;
  playerCount: number;
  maxPlayers: number;
  status: 'Waiting' | 'In Progress';
  link: string;
}

export interface PlayerReport {
  recentGames: {
    id: string;
    date: string;
    role: string;
    alignment: string;
    result: 'Win' | 'Loss';
  }[];
  statistics: {
    totalGames: number;
    winRate: number;
    townGames: number;
    mafiaGames: number;
    neutralGames: number;
  };
}