import type { RegisteredPlayerReport, RoleStats, FactionStats, GameLobby, PlayerReport } from '../types/Stats';

export const mockPlayerStats: RegisteredPlayerReport[] = [
  {
    id: 123456,
    username: "ProMafioso",
    createdAt: "2023-01-15",
    totalGames: 500,
    winRate: 0.65,
    townWinRate: 0.70,
    mafiaWinRate: 0.62,
    neutralWinRate: 0.55
  },
  {
    id: 789012,
    username: "TownHunter",
    createdAt: "2023-03-20",
    totalGames: 320,
    winRate: 0.58,
    townWinRate: 0.65,
    mafiaWinRate: 0.55,
    neutralWinRate: 0.45
  },
  {
    id: 345678,
    username: "NeutralChaos",
    createdAt: "2023-02-10",
    totalGames: 450,
    winRate: 0.60,
    townWinRate: 0.62,
    mafiaWinRate: 0.58,
    neutralWinRate: 0.65
  }
];



export const mockPlayerReport: PlayerReport = {
  recentGames: [
    {
      id: "game123",
      date: "2024-03-15",
      role: "Cop",
      alignment: "Town",
      result: "Win"
    },
    {
      id: "game124",
      date: "2024-03-15",
      role: "Godfather",
      alignment: "Mafia",
      result: "Loss"
    },
    {
      id: "game125",
      date: "2024-03-14",
      role: "Jester",
      alignment: "Neutral",
      result: "Win"
    }
  ],
  statistics: {
    totalGames: 500,
    winRate: 0.65,
    townGames: 250,
    mafiaGames: 200,
    neutralGames: 50
  }
};