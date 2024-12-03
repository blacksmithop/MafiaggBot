<script lang="ts">
  import { Plus, Clock } from 'lucide-svelte';
  import type { BotRoom } from '../../types/Bot';
  import CreateRoomModal from './CreateRoomModal.svelte';
  import EditRoomModal from './EditRoomModal.svelte';
  import RoomCard from './RoomCard.svelte';
  
  let showCreateModal = false;
  let showEditModal = false;
  let editingRoom: BotRoom | null = null;
  let rooms: BotRoom[] = [
    {
      id: '1',
      name: 'Ranked Practice',
      deck: 'Ranked',
      playerCount: 15,
      status: 'active',
      uptime: '2h 15m',
      roles: ['Cop', 'Doctor', 'Godfather', 'Mafioso', 'Jester']
    }
  ];

  function handleCreateRoom(room: BotRoom) {
    rooms = [...rooms, { ...room, id: (rooms.length + 1).toString() }];
    showCreateModal = false;
  }

  function handleEditRoom(room: BotRoom) {
    editingRoom = room;
    showEditModal = true;
  }

  function handleUpdateRoom(updatedRoom: BotRoom) {
    rooms = rooms.map(room => room.id === updatedRoom.id ? updatedRoom : room);
    showEditModal = false;
    editingRoom = null;
  }
</script>

<div class="bot-management">
  <div class="header-actions">
    <h2 class="section-title">Bot Rooms</h2>
    <button class="create-btn" on:click={() => showCreateModal = true}>
      <Plus size={20} />
      <span>Create Room</span>
    </button>
  </div>

  <div class="rooms-grid">
    {#each rooms as room (room.id)}
      <RoomCard {room} onEdit={() => handleEditRoom(room)} />
    {/each}
  </div>
</div>

{#if showCreateModal}
  <CreateRoomModal 
    onClose={() => showCreateModal = false}
    onSubmit={handleCreateRoom}
  />
{/if}

{#if showEditModal && editingRoom}
  <EditRoomModal 
    room={editingRoom}
    onClose={() => {
      showEditModal = false;
      editingRoom = null;
    }}
    onSubmit={handleUpdateRoom}
  />
{/if}

<style>
  .bot-management {
    max-width: 1200px;
    margin: 0 auto;
  }

  .header-actions {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 2rem;
  }

  .create-btn {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    background-color: var(--accent);
    color: white;
    border: none;
    padding: 0.75rem 1.5rem;
    border-radius: 8px;
    cursor: pointer;
    font-weight: 500;
    transition: all 0.2s ease;
  }

  .create-btn:hover {
    opacity: 0.9;
    transform: translateY(-1px);
  }

  .rooms-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 1.5rem;
  }

  @media (max-width: 640px) {
    .rooms-grid {
      grid-template-columns: 1fr;
    }
  }
</style>