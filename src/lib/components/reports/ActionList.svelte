<script lang="ts">
  import type { MatchAction } from '../../types/Report';
  import { 
    Vote, ArrowRight, Zap, Shield, Eye, 
    MessageCircle, UserX, UserCheck 
  } from 'lucide-svelte';

  export let actions: MatchAction[];

  const actionIcons = {
    vote: Vote,
    shoot: ArrowRight,
    taze: Zap,
    protect: Shield,
    investigate: Eye,
    whisper: MessageCircle,
    lynch: UserX,
    save: UserCheck
  };

  const actionColors = {
    vote: '#4CAF50',
    shoot: '#F44336',
    taze: '#2196F3',
    protect: '#4CAF50',
    investigate: '#9C27B0',
    whisper: '#FF9800',
    lynch: '#F44336',
    save: '#4CAF50'
  };
</script>

<div class="actions-list">
  {#each actions as action}
    <div 
      class="action-item"
      style="--action-color: {actionColors[action.type]}"
    >
      <div class="action-icon">
        <svelte:component this={actionIcons[action.type]} size={20} />
      </div>
      <div class="action-content">
        <span class="action-text">{action.description}</span>
        <span class="action-time">Day {action.day}, {action.phase}</span>
      </div>
    </div>
  {/each}
</div>

<style>
  .actions-list {
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
  }

  .action-item {
    display: flex;
    align-items: center;
    gap: 1rem;
    padding: 0.75rem;
    background-color: color-mix(in srgb, var(--action-color) 10%, var(--bg-secondary));
    border-radius: 6px;
    border-left: 3px solid var(--action-color);
  }

  .action-icon {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 32px;
    height: 32px;
    background-color: color-mix(in srgb, var(--action-color) 20%, transparent);
    border-radius: 6px;
    color: var(--action-color);
  }

  .action-content {
    display: flex;
    flex-direction: column;
    gap: 0.25rem;
  }

  .action-text {
    color: var(--text-primary);
  }

  .action-time {
    font-size: 0.75rem;
    color: var(--text-secondary);
  }
</style>