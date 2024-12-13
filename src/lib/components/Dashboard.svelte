<script lang="ts">
  import { onMount } from "svelte";
  import { getLobbies } from "../services";
  import type { GameLobby } from "../types/Stats";
  import { Users, Plus } from "lucide-svelte";

  let loading = true;
  let error: string | null = null;
  let gameLobbies: GameLobby[] = [];

  async function fetchLobbies() {
    try {
      loading = true;
      error = null;
      const response = await getLobbies();

      if (Array.isArray(response)) {
        gameLobbies = response;
      } else {
        throw new Error("Unexpected response format");
      }
    } catch (e) {
      error = e instanceof Error ? e.message : "Failed to load game lobbies";
    } finally {
      loading = false;
    }
  }

  onMount(fetchLobbies);
</script>

<div class="dashboard">
  <div class="card">
    <h2 class="section-title">Active Games</h2>

    {#if loading}
      <div class="loading-state">
        <div class="loader"></div>
        <span>Loading games...</span>
      </div>
    {:else if error}
      <div class="error-state">
        <p>{error}</p>
        <button class="retry-btn" on:click={fetchLobbies}>Retry</button>
      </div>
    {:else if gameLobbies.length === 0}
      <div class="empty-state">
        <p>No active games found</p>
        <a href="/bot" class="create-btn">
          <Plus size={16} />
          <span>Create a game</span>
        </a>
      </div>
    {:else}
      <div class="lobbies-list">
        {#each gameLobbies as lobby}
          <a
            href="https://mafia.gg/game/{lobby.id}"
            target="_blank"
            rel="noopener noreferrer"
            class="lobby-card"
          >
            <div class="lobby-info">
              <h3>{lobby.name}</h3>
              <span class="host">Hosted by {lobby.hostUser.username}</span>
            </div>
            <div class="lobby-stats">
              <div class="players-count">
                <Users size={16} />
                <span>{lobby.playerCount}/{lobby.setupSize}</span>
              </div>
              <span class="status" class:in-progress={lobby.hasStarted == true}>
                {lobby.hasStarted ? "Ongoing" : "In lobby"}
              </span>
            </div>
          </a>
        {/each}
      </div>
    {/if}
  </div>
</div>

<style>
  .dashboard {
    display: grid;
    gap: 1.5rem;
  }

  .loading-state,
  .error-state,
  .empty-state {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 2rem;
    text-align: center;
    color: var(--text-secondary);
  }

  .loader {
    width: 24px;
    height: 24px;
    border: 2px solid var(--text-secondary);
    border-top-color: var(--accent);
    border-radius: 50%;
    animation: spin 1s linear infinite;
    margin-bottom: 1rem;
  }

  @keyframes spin {
    to {
      transform: rotate(360deg);
    }
  }

  .retry-btn,
  .create-btn {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    margin-top: 1rem;
    padding: 0.75rem 1.5rem;
    background-color: var(--accent);
    color: white;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    font-weight: 500;
    text-decoration: none;
    transition: opacity 0.2s;
  }

  .retry-btn:hover,
  .create-btn:hover {
    opacity: 0.9;
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
