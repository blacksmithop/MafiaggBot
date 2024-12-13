export type ActionType = 'vote' | 'shoot' | 'taze' | 'protect' | 'investigate' | 'whisper' | 'lynch' | 'save';
export type GamePhase = 'Day' | 'Night';
export type GameResult = 'Win' | 'Loss';
export type Alignment = 'Town' | 'Mafia' | 'Neutral';

export interface MatchAction {
  type: ActionType;
  description: string;
  day: number;
  phase: GamePhase;
  target?: string;
}

export interface MatchReport {
  id: string;
  date: string;
  role: string;
  alignment: Alignment;
  result: GameResult;
  actions: MatchAction[];
}