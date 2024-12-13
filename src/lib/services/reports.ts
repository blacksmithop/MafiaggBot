import { fetchWithAuth } from './api';
import type { MatchReport } from '../types/Report';

// Temporary mock data until API is ready
const mockReports: MatchReport[] = [
  {
    id: '1',
    date: '2024-03-15',
    role: 'Cop',
    alignment: 'Town',
    result: 'Win',
    actions: [
      {
        type: 'investigate',
        description: 'Investigated Player2 - Found Suspicious',
        day: 1,
        phase: 'Night',
        target: 'Player2'
      },
      {
        type: 'vote',
        description: 'Voted against Player2',
        day: 2,
        phase: 'Day',
        target: 'Player2'
      },
      {
        type: 'lynch',
        description: 'Player2 was lynched (Mafioso)',
        day: 2,
        phase: 'Day',
        target: 'Player2'
      }
    ]
  },
  {
    id: '2',
    date: '2024-03-14',
    role: 'Vigilante',
    alignment: 'Town',
    result: 'Loss',
    actions: [
      {
        type: 'shoot',
        description: 'Shot Player3',
        day: 2,
        phase: 'Night',
        target: 'Player3'
      },
      {
        type: 'vote',
        description: 'Voted against Player4',
        day: 3,
        phase: 'Day',
        target: 'Player4'
      }
    ]
  }
];

export async function getRecentMatches(): Promise<MatchReport[]> {
  // TODO: Replace with actual API call
  return new Promise(resolve => {
    setTimeout(() => resolve(mockReports), 1000);
  });
}