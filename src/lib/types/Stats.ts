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

export interface HostUser {
  id: number;
  username: string;
  activePatreon: boolean;
  hostBannedUsernames: Array<string>;
  isPatreonLinked: boolean;
  needsVerification: boolean;
  createdAt: string;
}

export interface GameLobby {
  id: string;
  name: string;
  hasStarted: boolean;
  playerCount: number;
  setupSize: number;
  hostUser: HostUser;
  createdAt: string;
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