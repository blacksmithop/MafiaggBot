<script lang="ts">
  import { mockPlayerStats } from '../data/mockData';
  import type { PlayerStats } from '../types/Stats';
  
  let searchQuery = '';
  let searchResults: PlayerStats[] = [];
  
  function handleSearch() {
    searchResults = mockPlayerStats.filter(player => 
      player.username.toLowerCase().includes(searchQuery.toLowerCase())
    );
  }
</script>

<div class="card">
  <h2 class="section-title">Player Search</h2>
  <div class="search-container">
    <input
      type="text"
      bind:value={searchQuery}
      placeholder="Search players..."
      on:input={handleSearch}
    />
  </div>
  
  {#if searchResults.length > 0}
    <div class="results">
      {#each searchResults as player}
        <div class="player-card">
          <h3>{player.username}</h3>
          <div class="stats-grid">
            <div class="stat">
              <span class="label">Total Games:</span>
              <span class="value">{player.totalGames}</span>
            </div>
            <div class="stat">
              <span class="label">Win Rate:</span>
              <span class="value">{(player.winRate * 100).toFixed(1)}%</span>
            </div>
            <div class="stat">
              <span class="label">Town Win Rate:</span>
              <span class="value">{(player.townWinRate * 100).toFixed(1)}%</span>
            </div>
            <div class="stat">
              <span class="label">Mafia Win Rate:</span>
              <span class="value">{(player.mafiaWinRate * 100).toFixed(1)}%</span>
            </div>
          </div>
        </div>
      {/each}
    </div>
  {/if}
</div>

<style>
  .search-container {
    margin-bottom: 1rem;
  }

  input {
    width: 100%;
    padding: 0.75rem;
    background-color: var(--bg-primary);
    border: 1px solid var(--bg-tertiary);
    border-radius: 4px;
    color: var(--text-primary);
  }

  .player-card {
    background-color: var(--bg-tertiary);
    padding: 1rem;
    border-radius: 4px;
    margin-bottom: 1rem;
  }

  .stats-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1rem;
    margin-top: 0.5rem;
  }

  .stat {
    display: flex;
    justify-content: space-between;
  }

  .label {
    color: var(--text-secondary);
  }

  .value {
    font-weight: bold;
  }
</style>