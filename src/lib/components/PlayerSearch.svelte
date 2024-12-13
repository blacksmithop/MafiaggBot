<script lang="ts">
  import type { RegisteredPlayer, RegisteredPlayerReport } from '../types/Stats';
  import { getPlayerByName, getPlayerReport, getPlayerById } from "../services";
  import { Search } from 'lucide-svelte';
  
  let searchQuery: string = '';
  let selectedPlayer: RegisteredPlayer | RegisteredPlayerReport | null = null;
  let loading = false;
  let error: string | null = null;
  
  async function handleSearch() {
    if (!searchQuery.trim()) return;
    
    loading = true;
    error = null;
    selectedPlayer = null;

    try {
      // Check if search query is a number (ID) or string (username)
      const isId = !isNaN(Number(searchQuery));
      
      if (isId) {
        const response = await getPlayerById(parseInt(searchQuery));
        if (response) {
          selectedPlayer = response;
        }
      } else {
        const response = await getPlayerReport(searchQuery);
        if (response) {
          console.log(response)
          selectedPlayer = response;
        } else {
          error = "No player found with that username";
        }
      }
    } catch (e) {
      error = e instanceof Error ? e.message : "Failed to search for player";
    } finally {
      loading = false;
    }
  }
</script>

<div class="card">
  <h2 class="section-title">Player Search</h2>
  
  <div class="search-container">
    <div class="search-input">
      <Search size={20} class="search-icon" />
      <input
        type="text"
        bind:value={searchQuery}
        placeholder="Search by username or ID..."
        on:keydown={(e) => e.key === 'Enter' && handleSearch()}
      />
      <button class="search-btn" on:click={handleSearch} disabled={loading}>
        {loading ? 'Searching...' : 'Search'}
      </button>
    </div>
    
    {#if error}
      <div class="error-message">
        {error}
      </div>
    {/if}
  </div>
  
  {#if selectedPlayer}
    <div class="player-card">
      <div class="player-header">
        <h3>{selectedPlayer.username}</h3>
        <span class="player-id">ID: {selectedPlayer.id}</span>
      </div>
      
      <div class="player-details">
        <div class="detail-row">
          <span class="label">Joined:</span>
          {#if selectedPlayer.createdAt}
            <span class="value">{new Date(selectedPlayer.createdAt).toLocaleDateString()}</span>
          {:else}
            <span class="value">N/A</span>
          {/if}
        </div>
        <div class="detail-row">
          <span class="label">Total Games:</span>
          {#if typeof selectedPlayer.totalGames === 'number' && !isNaN(selectedPlayer.totalGames)}
            <span class="value">{selectedPlayer.totalGames}</span>
          {:else}
            <span class="value">N/A</span>
          {/if}
        </div>
        <div class="detail-row">
          <span class="label">Overall Win Rate:</span>
          {#if typeof selectedPlayer.winRate === 'number' && !isNaN(selectedPlayer.winRate)}
            <span class="value">{(selectedPlayer.winRate * 100).toFixed(1)}%</span>
          {:else}
            <span class="value">N/A</span>
          {/if}
        </div>
        
        <div class="faction-stats">
          {#if selectedPlayer.townWinRate !== undefined && !isNaN(selectedPlayer.townWinRate)}
            <div class="faction town">
              <span class="label">Town</span>
              <span class="value">{(selectedPlayer.townWinRate * 100).toFixed(1)}%</span>
            </div>
          {/if}
          {#if selectedPlayer.mafiaWinRate !== undefined && !isNaN(selectedPlayer.mafiaWinRate)}
            <div class="faction mafia">
              <span class="label">Mafia</span>
              <span class="value">{(selectedPlayer.mafiaWinRate * 100).toFixed(1)}%</span>
            </div>
          {/if}
          {#if selectedPlayer.neutralWinRate !== undefined && !isNaN(selectedPlayer.neutralWinRate)}
            <div class="faction neutral">
              <span class="label">Neutral</span>
              <span class="value">{(selectedPlayer.neutralWinRate * 100).toFixed(1)}%</span>
            </div>
          {/if}
        </div>
      </div>
      
    </div>
  {/if}
</div>

<style>
  .search-container {
    margin-bottom: 1.5rem;
  }

  .search-input {
    position: relative;
    display: flex;
    gap: 0.5rem;
  }

  .search-icon {
    position: absolute;
    left: 1rem;
    top: 50%;
    transform: translateY(-50%);
    color: var(--text-secondary);
    pointer-events: none;
  }

  input {
    flex: 1;
    padding: 0.75rem 1rem 0.75rem 2.75rem;
    background-color: var(--bg-tertiary);
    border: 1px solid var(--bg-tertiary);
    border-radius: 8px;
    color: var(--text-primary);
    font-size: 0.95rem;
    transition: all 0.2s ease;
  }

  input:focus {
    outline: none;
    border-color: var(--accent);
    box-shadow: 0 0 0 2px var(--accent-alpha);
  }

  .search-btn {
    padding: 0.75rem 1.5rem;
    background-color: var(--accent);
    color: white;
    border: none;
    border-radius: 8px;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.2s ease;
  }

  .search-btn:hover:not(:disabled) {
    opacity: 0.9;
  }

  .search-btn:disabled {
    opacity: 0.5;
    cursor: not-allowed;
  }

  .error-message {
    margin-top: 0.5rem;
    padding: 0.75rem;
    background-color: var(--danger);
    color: white;
    border-radius: 6px;
    font-size: 0.875rem;
  }

  .player-card {
    background-color: var(--bg-tertiary);
    padding: 1.5rem;
    border-radius: 8px;
  }

  .player-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1rem;
  }

  .player-id {
    color: var(--text-secondary);
    font-size: 0.875rem;
  }

  .player-details {
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }

  .detail-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .label {
    color: var(--text-secondary);
  }

  .value {
    font-weight: 500;
  }

  .faction-stats {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1rem;
    margin-top: 0.5rem;
  }

  .faction {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 1rem;
    background-color: var(--bg-secondary);
    border-radius: 6px;
  }

  .faction .label {
    font-size: 0.875rem;
    margin-bottom: 0.25rem;
  }

  .faction .value {
    font-size: 1.25rem;
    font-weight: 600;
  }

  .town .value { color: var(--success); }
  .mafia .value { color: var(--danger); }
  .neutral .value { color: var(--neutral); }

  @media (max-width: 640px) {
    .search-input {
      flex-direction: column;
    }

    .search-btn {
      width: 100%;
    }

    .faction-stats {
      grid-template-columns: 1fr;
    }
  }
</style>