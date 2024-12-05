<script lang="ts">
  import type { Achievement } from '../../types/Achievement';
  
  export let achievement: Achievement;
  
  $: progress = achievement.progress 
    ? Math.round((achievement.progress.current / achievement.progress.required) * 100)
    : null;
</script>

<div class="achievement-card" class:unlocked={achievement.unlocked}>
  <div class="icon-wrapper">
    <svelte:component this={achievement.icon} size={24} />
  </div>
  <div class="achievement-info">
    <h3>{achievement.name}</h3>
    <p>{achievement.description}</p>
    {#if progress !== null}
      <div class="progress-bar">
        <div class="progress" style="width: {progress}%"></div>
        <span class="progress-text">
          {achievement.progress.current}/{achievement.progress.required}
        </span>
      </div>
    {/if}
  </div>
</div>

<style>
  .achievement-card {
    display: flex;
    gap: 1rem;
    padding: 1rem;
    background-color: var(--bg-tertiary);
    border-radius: 8px;
    opacity: 0.5;
    transition: all 0.2s ease;
  }

  .achievement-card.unlocked {
    opacity: 1;
  }

  .achievement-card:hover {
    transform: translateY(-2px);
  }

  .icon-wrapper {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 48px;
    height: 48px;
    background-color: var(--bg-secondary);
    border-radius: 8px;
    color: var(--accent);
  }

  .unlocked .icon-wrapper {
    background-color: var(--accent);
    color: white;
  }

  .achievement-info {
    flex: 1;
  }

  h3 {
    margin: 0;
    font-size: 1rem;
    margin-bottom: 0.25rem;
  }

  p {
    margin: 0;
    font-size: 0.875rem;
    color: var(--text-secondary);
    margin-bottom: 0.5rem;
  }

  .progress-bar {
    position: relative;
    height: 4px;
    background-color: var(--bg-secondary);
    border-radius: 2px;
    overflow: hidden;
  }

  .progress {
    position: absolute;
    top: 0;
    left: 0;
    height: 100%;
    background-color: var(--accent);
    transition: width 0.3s ease;
  }

  .progress-text {
    position: absolute;
    top: -1.5rem;
    right: 0;
    font-size: 0.75rem;
    color: var(--text-secondary);
  }
</style>