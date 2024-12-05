<script lang="ts">
  import { notifications } from '../../data/notifications';
  import NotificationItem from './NotificationItem.svelte';
  import InviteModal from './InviteModal.svelte';
  import type { Notification } from '../../types/Notification';
  
  let selectedInvite = null;
  let filter = 'all';
  
  $: filteredNotifications = filter === 'all' 
    ? notifications 
    : notifications.filter(n => n.type === filter);
    
  function handleNotificationClick(event: CustomEvent<Notification>) {
    const notification = event.detail;
    if (notification.type === 'invite') {
      selectedInvite = notification.data;
    }
  }
</script>

<div class="notifications-page">
  <div class="header">
    <h2 class="section-title">Notifications</h2>
    <div class="filters">
      <button 
        class:active={filter === 'all'} 
        on:click={() => filter = 'all'}
      >
        All
      </button>
      <button 
        class:active={filter === 'achievement'} 
        on:click={() => filter = 'achievement'}
      >
        Achievements
      </button>
      <button 
        class:active={filter === 'game_report'} 
        on:click={() => filter = 'game_report'}
      >
        Reports
      </button>
      <button 
        class:active={filter === 'invite'} 
        on:click={() => filter = 'invite'}
      >
        Invites
      </button>
    </div>
  </div>
  
  <div class="notifications-list">
    {#each filteredNotifications as notification (notification.id)}
      <NotificationItem 
        {notification}
        on:click={handleNotificationClick}
      />
    {/each}
  </div>
</div>

{#if selectedInvite}
  <InviteModal 
    invite={selectedInvite}
    on:close={() => selectedInvite = null}
    on:join={(event) => {
      console.log('Joining game:', event.detail);
      selectedInvite = null;
    }}
  />
{/if}

<style>
  .notifications-page {
    max-width: 800px;
    margin: 0 auto;
  }

  .header {
    margin-bottom: 2rem;
  }

  .filters {
    display: flex;
    gap: 0.5rem;
    margin-top: 1rem;
    background-color: var(--bg-tertiary);
    padding: 0.5rem;
    border-radius: 8px;
  }

  .filters button {
    flex: 1;
    padding: 0.75rem;
    border: none;
    background: none;
    color: var(--text-secondary);
    border-radius: 6px;
    cursor: pointer;
    transition: all 0.2s ease;
  }

  .filters button:hover {
    color: var(--text-primary);
    background-color: var(--bg-secondary);
  }

  .filters button.active {
    color: var(--text-primary);
    background-color: var(--bg-secondary);
  }

  .notifications-list {
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
  }
</style>