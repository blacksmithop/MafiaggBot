<script lang="ts">
  import type { RegisteredPlayer, RegisteredPlayerReport } from '../types/Stats';
  import { getPlayerByName, getPlayerReport } from "../services";
  
  let searchQuery: string = '';
  let searchResults: RegisteredPlayer[] = [];
  let selectedPlayer: RegisteredPlayerReport | null = null;
  
  async function handleSearch() {
    const response = await getPlayerByName(searchQuery);
    searchResults = response;
  }

  async function selectPlayer(player: RegisteredPlayer) {
    const response = await getPlayerReport(player.username);
    selectedPlayer = response;
    console.log(selectedPlayer)
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
        <div class="player-card" on:click={() => selectPlayer(player)}>
          <div class="player-header">
            <h3>{player.username}</h3>
          </div>
          
          {#if selectedPlayer?.id === player.id}
            <div class="player-details">
              <div class="detail-row">
                <span class="label">User ID:</span>
                <span class="value">{player.id}</span>
              </div>
              <div class="detail-row">
                <span class="label">Joined:</span>
                <span class="value">{player.createdAt}</span>
              </div>
              <div class="detail-row">
                <span class="label">Total Games:</span>
                <span class="value">{player.totalGames}</span>
              </div>
              <div class="faction-stats">
                <div class="faction town">
                  <span class="label">Town</span>
                  <span class="value">{(player.townWinRate * 100).toFixed(1)}%</span>
                </div>
                <div class="faction mafia">
                  <span class="label">Mafia</span>
                  <span class="value">{(player.mafiaWinRate * 100).toFixed(1)}%</span>
                </div>
                <div class="faction neutral">
                  <span class="label">Neutral</span>
                  <span class="value">{(player.neutralWinRate * 100).toFixed(1)}%</span>
                </div>
              </div>
            </div>
          {/if}
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
    border-radius: 8px;
    color: var(--text-primary);
  }

  .player-card {
    background-color: var(--bg-tertiary);
    padding: 1rem;
    border-radius: 8px;
    margin-bottom: 0.75rem;
    cursor: pointer;
    transition: all 0.2s ease;
  }

  .player-card:hover {
    transform: translateX(4px);
  }

  .player-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .games-count {
    color: var(--text-secondary);
    font-size: 0.875rem;
  }

  .player-details {
    margin-top: 1rem;
    padding-top: 1rem;
    border-top: 1px solid var(--bg-secondary);
  }

  .detail-row {
    display: flex;
    justify-content: space-between;
    margin-bottom: 0.5rem;
  }

  .faction-stats {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 0.75rem;
    margin-top: 1rem;
  }

  .faction {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 0.75rem;
    border-radius: 6px;
    background-color: var(--bg-secondary);
  }

  .faction .label {
    font-size: 0.75rem;
    color: var(--text-secondary);
    margin-bottom: 0.25rem;
  }

  .faction .value {
    font-weight: 600;
    font-size: 1.125rem;
  }

  .town .value { color: var(--success); }
  .mafia .value { color: var(--danger); }
  .neutral .value { color: var(--neutral); }
</style>