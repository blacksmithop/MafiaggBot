import type { Notification } from '../types/Notification';

export const notifications: Notification[] = [
  {
    id: '1',
    type: 'achievement',
    title: 'Achievement Unlocked!',
    message: 'Perfect Detective - Correctly identify all mafia members as Cop',
    datetime: new Date(Date.now() - 1000 * 60 * 30),
    read: false
  },
  {
    id: '2',
    type: 'game_report',
    title: 'Game Report Available',
    message: 'Your game report for Match #1234 is ready',
    datetime: new Date(Date.now() - 1000 * 60 * 60 * 2),
    read: false
  },
  {
    id: '3',
    type: 'invite',
    title: 'Game Invitation',
    message: 'ProMafioso has invited you to join their game',
    datetime: new Date(Date.now() - 1000 * 60 * 5),
    read: false,
    data: {
      lobbyId: '1234',
      lobbyName: 'Pro Players Only',
      host: 'ProMafioso',
      playerCount: 12,
      maxPlayers: 15
    }
  }
];