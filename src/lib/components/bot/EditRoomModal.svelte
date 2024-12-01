<script lang="ts">
  import { createEventDispatcher } from 'svelte';
  import { X } from 'lucide-svelte';
  import type { BotRoom } from '../../types/Bot';
  
  const dispatch = createEventDispatcher();
  
  export let room: BotRoom;
  export let onClose: () => void;
  export let onSubmit: (room: BotRoom) => void;
  
  let name = room.name;
  let deck = room.deck;
  let playerCount = room.playerCount;
  let selectedRoles = room.roles || [];
  
  const availableDecks = ['Ranked', 'Custom', 'All Any', 'Rainbow'];
  const availableRoles = [
    'Cop', 'Doctor', 'Vigilante', 'Jailor',
    'Godfather', 'Mafioso', 'Consigliere', 'Janitor',
    'Jester', 'Serial Killer', 'Arsonist', 'Witch'
  ];
  
  function handleSubmit() {
    if (!name) return;
    
    onSubmit({
      ...room,
      name,
      deck,
      playerCount,
      roles: selectedRoles
    });
  }
</script>

<div class="modal-overlay" on:click={onClose}>
  <div class="modal" on:click|stopPropagation>
    <div class="modal-header">
      <h3>Edit Bot Room</h3>
      <button class="close-btn" on:click={onClose}>
        <X size={20} />
      </button>
    </div>

    <div class="modal-content">
      <div class="form-group">
        <label for="name">Room Name</label>
        <input
          type="text"
          id="name"
          bind:value={name}
          placeholder="Enter room name"
        />
      </div>

      <div class="form-group">
        <label for="deck">Deck</label>
        <select id="deck" bind:value={deck}>
          {#each availableDecks as deckOption}
            <option value={deckOption}>{deckOption}</option>
          {/each}
        </select>
      </div>

      <div class="form-group">
        <label for="playerCount">Player Count</label>
        <input
          type="number"
          id="playerCount"
          bind:value={playerCount}
          min="5"
          max="15"
        />
      </div>

      {#if deck === 'Custom'}
        <div class="form-group">
          <label>Roles</label>
          <div class="roles-grid">
            {#each availableRoles as role}
              <label class="role-checkbox">
                <input
                  type="checkbox"
                  bind:group={selectedRoles}
                  value={role}
                />
                <span>{role}</span>
              </label>
            {/each}
          </div>
        </div>
      {/if}
    </div>

    <div class="modal-footer">
      <button class="cancel-btn" on:click={onClose}>Cancel</button>
      <button class="submit-btn" on:click={handleSubmit}>Update Room</button>
    </div>
  </div>
</div>

<style>
  .modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 1000;
  }

  .modal {
    background-color: var(--bg-secondary);
    border-radius: 12px;
    width: 90%;
    max-width: 500px;
    max-height: 90vh;
    overflow-y: auto;
  }

  .modal-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1.5rem;
    border-bottom: 1px solid var(--bg-tertiary);
  }

  .modal-header h3 {
    font-size: 1.25rem;
    font-weight: 600;
  }

  .close-btn {
    background: none;
    border: none;
    color: var(--text-secondary);
    cursor: pointer;
    padding: 0.5rem;
    border-radius: 6px;
    transition: all 0.2s ease;
  }

  .close-btn:hover {
    background-color: var(--bg-tertiary);
    color: var(--text-primary);
  }

  .modal-content {
    padding: 1.5rem;
  }

  .form-group {
    margin-bottom: 1.5rem;
  }

  .form-group label {
    display: block;
    margin-bottom: 0.5rem;
    color: var(--text-secondary);
    font-size: 0.875rem;
  }

  input, select {
    width: 100%;
    padding: 0.75rem;
    background-color: var(--bg-tertiary);
    border: 1px solid var(--bg-tertiary);
    color: var(--text-primary);
    border-radius: 6px;
    transition: all 0.2s ease;
  }

  input:focus, select:focus {
    outline: none;
    border-color: var(--accent);
  }

  .roles-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(120px, 1fr));
    gap: 0.75rem;
  }

  .role-checkbox {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    cursor: pointer;
  }

  .role-checkbox input {
    width: auto;
  }

  .modal-footer {
    padding: 1.5rem;
    border-top: 1px solid var(--bg-tertiary);
    display: flex;
    justify-content: flex-end;
    gap: 1rem;
  }

  .cancel-btn, .submit-btn {
    padding: 0.75rem 1.5rem;
    border-radius: 6px;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.2s ease;
  }

  .cancel-btn {
    background-color: var(--bg-tertiary);
    color: var(--text-primary);
    border: none;
  }

  .submit-btn {
    background-color: var(--accent);
    color: white;
    border: none;
  }

  .cancel-btn:hover {
    background-color: var(--bg-primary);
  }

  .submit-btn:hover {
    opacity: 0.9;
  }
</style>