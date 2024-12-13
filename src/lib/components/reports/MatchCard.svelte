<script lang="ts">
  import { slide } from 'svelte/transition';
  import { ChevronDown, ChevronUp } from 'lucide-svelte';
  import type { MatchReport } from '../../types/Report';
  import ActionList from './ActionList.svelte';
  
  export let match: MatchReport;
  
  let expanded = false;

  function toggleExpand() {
    expanded = !expanded;
  }

  $: roleColor = match.alignment === 'Town' ? 'var(--success)' :
                 match.alignment === 'Mafia' ? 'var(--danger)' :
                 'var(--neutral)';
</script>

<div class="match-card">
  <div class="match-header" on:click={toggleExpand}>
    <div class="match-info">
      <div class="role-badge" style="--role-color: {roleColor}">
        <span class="alignment">{match.alignment}</span>
        <span class="role">{match.role}</span>
      </div>
      <div class="match-details">
        <span class="date">{new Date(match.date).toLocaleDateString()}</span>
        <span class="result" class:win={match.result === 'Win'} class:loss={match.result === 'Loss'}>
          {match.result}
        </span>
      </div>
    </div>
    <button class="expand-btn">
      {#if expanded}
        <ChevronUp size={20} />
      {:else}
        <ChevronDown size={20} />
      {/if}
    </button>
  </div>

  {#if expanded}
    <div class="match-content" transition:slide>
      <ActionList actions={match.actions} />
    </div>
  {/if}
</div>

<style>
  .match-card {
    background-color: var(--bg-tertiary);
    border-radius: 8px;
    overflow: hidden;
  }

  .match-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1rem;
    cursor: pointer;
    transition: background-color 0.2s ease;
  }

  .match-header:hover {
    background-color: var(--bg-secondary);
  }

  .match-info {
    display: flex;
    align-items: center;
    gap: 1rem;
  }

  .role-badge {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 0.5rem 1rem;
    background-color: color-mix(in srgb, var(--role-color) 15%, var(--bg-secondary));
    border-left: 4px solid var(--role-color);
    border-radius: 6px;
  }

  .alignment {
    font-size: 0.75rem;
    color: var(--role-color);
    font-weight: 500;
  }

  .role {
    font-weight: 600;
    color: var(--text-primary);
  }

  .match-details {
    display: flex;
    flex-direction: column;
    gap: 0.25rem;
  }

  .date {
    font-size: 0.875rem;
    color: var(--text-secondary);
  }

  .result {
    font-weight: 500;
  }

  .result.win {
    color: var(--success);
  }

  .result.loss {
    color: var(--danger);
  }

  .expand-btn {
    background: none;
    border: none;
    color: var(--text-secondary);
    cursor: pointer;
    padding: 0.5rem;
    border-radius: 6px;
    transition: all 0.2s ease;
  }

  .expand-btn:hover {
    background-color: var(--bg-secondary);
    color: var(--text-primary);
  }

  .match-content {
    padding: 1rem;
    border-top: 1px solid var(--bg-secondary);
  }
</style>