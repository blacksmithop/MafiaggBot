<script lang="ts">
  import { createEventDispatcher } from 'svelte';
  import type { GameInvite } from '../../types/Notification';
  import { X, Users } from 'lucide-svelte';
  
  export let invite: GameInvite;
  
  const dispatch = createEventDispatcher();
  
  function handleClose() {
    dispatch('close');
  }
  
  function handleJoin() {
    dispatch('join', invite.lobbyId);
  }
</script>

<div class="modal-overlay" on:click={handleClose}>
  <div class="modal" on:click|stopPropagation>
    <button class="close-btn" on:click={handleClose}>
      <X size={20} />
    </button>
    
    <div class="modal-content">
      <h2>Game Invitation</h2>
      
      <div class="invite-details">
        <div class="host-info">
          <img 
            src={`https://api.dicebear.com/7.x/avataaars/svg?seed=${invite.host}`}
            alt={invite.host}
            class="host-avatar"
          />
          <span class="host-name">{invite.host}</span>
        </div>
        
        <div class="lobby-info">
          <h3>{invite.lobbyName}</h3>
          <div class="player-count">
            <Users size={16} />
            <span>{invite.playerCount}/{invite.maxPlayers} players</span>
          </div>
        </div>
      </div>
      
      <div class="actions">
        <button class="cancel-btn" on:click={handleClose}>Decline</button>
        <button class="join-btn" on:click={handleJoin}>Join Game</button>
      </div>
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
    position: relative;
    background-color: var(--bg-secondary);
    border-radius: 12px;
    width: 90%;
    max-width: 400px;
    padding: 2rem;
  }

  .close-btn {
    position: absolute;
    top: 1rem;
    right: 1rem;
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

  h2 {
    margin: 0 0 1.5rem;
    text-align: center;
  }

  .invite-details {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
    margin-bottom: 2rem;
  }

  .host-info {
    display: flex;
    align-items: center;
    gap: 1rem;
  }

  .host-avatar {
    width: 48px;
    height: 48px;
    border-radius: 50%;
  }

  .host-name {
    font-weight: 500;
  }

  .lobby-info {
    background-color: var(--bg-tertiary);
    padding: 1rem;
    border-radius: 8px;
  }

  .lobby-info h3 {
    margin: 0 0 0.5rem;
  }

  .player-count {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    color: var(--text-secondary);
    font-size: 0.875rem;
  }

  .actions {
    display: flex;
    gap: 1rem;
  }

  .cancel-btn, .join-btn {
    flex: 1;
    padding: 0.75rem;
    border-radius: 6px;
    border: none;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.2s ease;
  }

  .cancel-btn {
    background-color: var(--bg-tertiary);
    color: var(--text-primary);
  }

  .join-btn {
    background-color: var(--accent);
    color: white;
  }

  .cancel-btn:hover {
    background-color: var(--bg-primary);
  }

  .join-btn:hover {
    opacity: 0.9;
  }
</style>