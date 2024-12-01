<script lang="ts">
  import { Clock, Users, Settings } from 'lucide-svelte';
  import type { BotRoom } from '../../types/Bot';
  
  export let room: BotRoom;
  export let onEdit: () => void;
</script>

<div class="room-card">
  <div class="room-header">
    <h3>{room.name}</h3>
    <span class="status" class:active={room.status === 'active'}>
      {room.status}
    </span>
  </div>
  
  <div class="room-info">
    <div class="info-item">
      <Clock size={16} />
      <span>Uptime: {room.uptime}</span>
    </div>
    <div class="info-item">
      <Users size={16} />
      <span>{room.playerCount} players</span>
    </div>
    <div class="info-item">
      <Settings size={16} />
      <span>{room.deck}</span>
    </div>
  </div>
  
  {#if room.roles && room.roles.length > 0}
    <div class="roles-list">
      {#each room.roles as role}
        <span class="role-tag">{role}</span>
      {/each}
    </div>
  {/if}
  
  <div class="room-actions">
    <button class="action-btn" on:click={onEdit}>Configure</button>
    <button class="action-btn danger">Stop</button>
  </div>
</div>

<style>
  .room-card {
    background-color: var(--bg-secondary);
    border-radius: 12px;
    padding: 1.5rem;
    border: 1px solid var(--bg-tertiary);
    transition: all 0.2s ease;
  }

  .room-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  }

  .room-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1rem;
  }

  .room-header h3 {
    font-size: 1.25rem;
    font-weight: 600;
  }

  .status {
    font-size: 0.875rem;
    padding: 0.25rem 0.75rem;
    border-radius: 999px;
    background-color: var(--bg-tertiary);
    color: var(--text-secondary);
  }

  .status.active {
    background-color: var(--success);
    color: white;
  }

  .room-info {
    display: grid;
    gap: 0.75rem;
    margin-bottom: 1rem;
  }

  .info-item {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    color: var(--text-secondary);
    font-size: 0.875rem;
  }

  .roles-list {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin-bottom: 1rem;
  }

  .role-tag {
    font-size: 0.75rem;
    padding: 0.25rem 0.75rem;
    border-radius: 999px;
    background-color: var(--bg-tertiary);
    color: var(--text-secondary);
  }

  .room-actions {
    display: flex;
    gap: 0.75rem;
  }

  .action-btn {
    flex: 1;
    padding: 0.75rem;
    border-radius: 6px;
    border: none;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.2s ease;
    background-color: var(--bg-tertiary);
    color: var(--text-primary);
  }

  .action-btn:hover {
    opacity: 0.9;
  }

  .action-btn.danger {
    background-color: var(--danger);
    color: white;
  }
</style>