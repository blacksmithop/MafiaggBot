import type { PlayerReport } from '../types/Stats';

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