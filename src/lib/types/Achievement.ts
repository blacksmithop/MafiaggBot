export interface Achievement {
  id: string;
  name: string;
  description: string;
  icon: string;
  unlocked: boolean;
  progress?: {
    current: number;
    required: number;
  };
  category: 'gameplay' | 'social' | 'special';
}