<script lang="ts">
  import { mockGameLobbies } from '../data/mockData';
  import { Users } from 'lucide-svelte';
</script>

<div class="dashboard">
  <div class="card">
    <h2 class="section-title">Active Games</h2>
    <div class="lobbies-list">
      {#each mockGameLobbies as lobby}
        <a href={lobby.link} target="_blank" rel="noopener noreferrer" class="lobby-card">
          <div class="lobby-info">
            <h3>{lobby.name}</h3>
            <span class="host">Hosted by {lobby.host}</span>
          </div>
          <div class="lobby-stats">
            <div class="players-count">
              <Users size={16} />
              <span>{lobby.playerCount}/{lobby.maxPlayers}</span>
            </div>
            <span class="status" class:in-progress={lobby.status === 'In Progress'}>
              {lobby.status}
            </span>
          </div>
        </a>
      {/each}
    </div>
  </div>
</div>

<style>
  .dashboard {
    display: grid;
    gap: 1.5rem;
  }

  .lobbies-list {
    display: grid;
    gap: 1rem;
  }

  .lobby-card {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1rem;
    background-color: var(--bg-tertiary);
    border-radius: 8px;
    text-decoration: none;
    color: var(--text-primary);
    transition: all 0.2s ease;
  }

  .lobby-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  }

  .lobby-info h3 {
    margin-bottom: 0.25rem;
  }

  .host {
    font-size: 0.875rem;
    color: var(--text-secondary);
  }

  .lobby-stats {
    display: flex;
    align-items: center;
    gap: 1.5rem;
  }

  .players-count {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    color: var(--text-secondary);
  }

  .status {
    font-size: 0.875rem;
    padding: 0.25rem 0.75rem;
    border-radius: 999px;
    background-color: var(--success);
    color: white;
  }

  .status.in-progress {
    background-color: var(--accent);
  }
</style>