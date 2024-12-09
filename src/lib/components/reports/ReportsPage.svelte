<script lang="ts">
  import { onMount } from 'svelte';
  import MatchCard from './MatchCard.svelte';
  import type { MatchReport } from '../../types/Report';
  import { getRecentMatches } from '../../services/reports';

  let matches: MatchReport[] = [];
  let loading = true;
  let error: string | null = null;

  onMount(async () => {
    try {
      matches = await getRecentMatches();
    } catch (e) {
      error = e instanceof Error ? e.message : 'Failed to load matches';
    } finally {
      loading = false;
    }
  });
</script>

<div class="reports-page">
  <h2 class="section-title">Match Reports</h2>

  {#if loading}
    <div class="loading-state">Loading match reports...</div>
  {:else if error}
    <div class="error-state">{error}</div>
  {:else if matches.length === 0}
    <div class="empty-state">No match reports found</div>
  {:else}
    <div class="matches-list">
      {#each matches as match (match.id)}
        <MatchCard {match} />
      {/each}
    </div>
  {/if}
</div>

<style>
  .reports-page {
    max-width: 800px;
    margin: 0 auto;
  }

  .matches-list {
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }

  .loading-state,
  .error-state,
  .empty-state {
    text-align: center;
    padding: 2rem;
    background-color: var(--bg-tertiary);
    border-radius: 8px;
    color: var(--text-secondary);
  }

  .error-state {
    color: var(--danger);
  }
</style>