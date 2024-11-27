import type { PlayerStats, RoleStats, FactionStats } from '../types/Stats';

export const mockPlayerStats: PlayerStats[] = [
  {
    username: "ProMafioso",
    totalGames: 500,
    winRate: 0.65,
    townWinRate: 0.70,
    mafiaWinRate: 0.62,
    neutralWinRate: 0.55
  },
  // Add more mock players...
];

export const mockRoleStats: RoleStats[] = [
  {
    name: "Cop",
    alignment: "Town",
    winRate: 0.55,
    totalGames: 1000
  },
  {
    name: "Godfather",
    alignment: "Mafia",
    winRate: 0.48,
    totalGames: 800
  },
  {
    name: "Jester",
    alignment: "Neutral",
    winRate: 0.25,
    totalGames: 400
  }
];

export const mockFactionStats: FactionStats[] = [
  {
    name: "Town",
    winRate: 0.52,
    totalGames: 5000
  },
  {
    name: "Mafia",
    winRate: 0.42,
    totalGames: 5000
  },
  {
    name: "Neutral",
    winRate: 0.06,
    totalGames: 5000
  }
];