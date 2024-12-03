<script lang="ts">
  import { createEventDispatcher } from 'svelte';
  import { X } from 'lucide-svelte';
  import type { BotRoom } from '../../types/Bot';
  import RoomBasicSection from './sections/RoomBasicSection.svelte';
  import RoomRolesSection from './sections/RoomRolesSection.svelte';
  import RoomSettingsSection from './sections/RoomSettingsSection.svelte';
  
  const dispatch = createEventDispatcher();
  
  export let onClose: () => void;
  export let onSubmit: (room: BotRoom) => void;
  
  let name = '';
  let deck = '';
  let selectedRoles: { [key: string]: number } = {};
  let currentSection = 'basic';

  const sections = [
    { id: 'basic', label: 'Room Details' },
    { id: 'roles', label: 'Role Setup' },
    { id: 'settings', label: 'Settings' }
  ];
  
  function handleSubmit() {
    if (!name) return;
    
    onSubmit({
      id: '',
      name,
      deck,
      playerCount: 15,
      roles: Object.entries(selectedRoles).map(([roleId, count]) => ({
        id: parseInt(roleId),
        count
      })),
      status: 'active',
      uptime: '0m'
    });
  }
</script>

<div class="modal-overlay" on:click={onClose}>
  <div class="modal" on:click|stopPropagation>
    <div class="modal-header">
      <h3>Create Bot Room</h3>
      <button class="close-btn" on:click={onClose}>
        <X size={20} />
      </button>
    </div>

    <div class="sections-nav">
      {#each sections as section}
        <button
          class="section-btn"
          class:active={currentSection === section.id}
          on:click={() => currentSection = section.id}
        >
          {section.label}
        </button>
      {/each}
    </div>

    <div class="modal-content">
      {#if currentSection === 'basic'}
        <RoomBasicSection
          bind:name
          bind:deck
        />
      {:else if currentSection === 'roles'}
        <RoomRolesSection
          bind:selectedRoles
        />
      {:else if currentSection === 'settings'}
        <RoomSettingsSection />
      {/if}
    </div>

    <div class="modal-footer">
      <button class="cancel-btn" on:click={onClose}>Cancel</button>
      <button class="submit-btn" on:click={handleSubmit}>Create Room</button>
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
    max-width: 800px;
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

  .sections-nav {
    display: flex;
    gap: 0.5rem;
    padding: 1rem 1.5rem;
    border-bottom: 1px solid var(--bg-tertiary);
    background-color: var(--bg-tertiary);
  }

  .section-btn {
    padding: 0.75rem 1.5rem;
    border: none;
    background: none;
    color: var(--text-secondary);
    font-weight: 500;
    cursor: pointer;
    border-radius: 6px;
    transition: all 0.2s ease;
  }

  .section-btn:hover {
    color: var(--text-primary);
    background-color: var(--bg-secondary);
  }

  .section-btn.active {
    color: var(--text-primary);
    background-color: var(--bg-secondary);
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
    min-height: 400px;
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