import { Achievement } from '../types/Achievement';
import { 
  Trophy, Crown, Target, Users, Sword, Shield, 
  Brain, Ghost, Award, Star, Medal, Lightning
} from 'lucide-svelte';

export const achievements: Achievement[] = [
  {
    id: 'first_win',
    name: 'First Victory',
    description: 'Win your first game',
    icon: Trophy,
    unlocked: true,
    category: 'gameplay'
  },
  {
    id: 'town_master',
    name: 'Town Master',
    description: 'Win 50 games as Town',
    icon: Shield,
    unlocked: false,
    progress: {
      current: 32,
      required: 50
    },
    category: 'gameplay'
  },
  {
    id: 'mafia_boss',
    name: 'Mafia Boss',
    description: 'Win 30 games as Mafia',
    icon: Sword,
    unlocked: false,
    progress: {
      current: 18,
      required: 30
    },
    category: 'gameplay'
  },
  {
    id: 'social_butterfly',
    name: 'Social Butterfly',
    description: 'Play with 100 different players',
    icon: Users,
    unlocked: false,
    progress: {
      current: 75,
      required: 100
    },
    category: 'social'
  },
  {
    id: 'perfect_detective',
    name: 'Perfect Detective',
    description: 'Correctly identify all mafia members as Cop',
    icon: Target,
    unlocked: true,
    category: 'gameplay'
  },
  {
    id: 'mastermind',
    name: 'Mastermind',
    description: 'Win 10 games in a row',
    icon: Brain,
    unlocked: false,
    category: 'special'
  }
];