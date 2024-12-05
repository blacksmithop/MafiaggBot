<script lang="ts">
  import { notifications } from '../../data/notifications';
  import NotificationItem from './NotificationItem.svelte';
  import InviteModal from './InviteModal.svelte';
  import type { Notification, GameInvite } from '../../types/Notification';
  import { Trophy, FileText, Users } from 'lucide-svelte';

  let selectedInvite: GameInvite | null = null;
  let activeCategory: 'all' | 'achievement' | 'game_report' | 'invite' = 'all';

  const categories = [
    { id: 'all', label: 'All Notifications', icon: null },
    { id: 'achievement', label: 'Achievements', icon: Trophy, color: 'var(--success)' },
    { id: 'game_report', label: 'Game Reports', icon: FileText, color: 'var(--accent)' },
    { id: 'invite', label: 'Invites', icon: Users, color: 'var(--neutral)' }
  ];

  $: filteredNotifications = activeCategory === 'all'
    ? notifications
    : notifications.filter(n => n.type === activeCategory);

  function handleNotificationClick(event: CustomEvent<Notification>) {
    const notification = event.detail;
    if (notification.type === 'invite') {
      selectedInvite = notification.data;
    }
  }

  function markAllAsRead() {
    // In a real app, this would update the backend
    console.log('Marking all notifications as read');
  }
</script>

<div class="notifications-page">
  <div class="header">
    <div class="title-section">
      <h2 class="section-title">Notifications</h2>
      <button class="mark-read-btn" on:click={markAllAsRead}>
        Mark all as read
      </button>
    </div>

    <div class="categories">
      {#each categories as category}
        <button
          class="category-btn"
          class:active={activeCategory === category.id}
          style="--category-color: {category.color || 'var(--text-primary)'}"
          on:click={() => activeCategory = category.id}
        >
          {#if category.icon}
            <svelte:component this={category.icon} size={16} />
          {/if}
          <span>{category.label}</span>
        </button>
      {/each}
    </div>
  </div>

  <div class="notifications-list">
    {#if filteredNotifications.length === 0}
      <div class="empty-state">
        <p>No notifications in this category</p>
      </div>
    {:else}
      {#each filteredNotifications as notification (notification.id)}
        <NotificationItem
          {notification}
          on:click={handleNotificationClick}
        />
      {/each}
    {/if}
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

  .title-section {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1.5rem;
  }

  .mark-read-btn {
    background: none;
    border: none;
    color: var(--accent);
    font-size: 0.875rem;
    cursor: pointer;
    padding: 0.5rem 1rem;
    border-radius: 6px;
    transition: all 0.2s ease;
  }

  .mark-read-btn:hover {
    background-color: var(--bg-tertiary);
  }

  .categories {
    display: flex;
    gap: 0.5rem;
    background-color: var(--bg-tertiary);
    padding: 0.5rem;
    border-radius: 8px;
  }

  .category-btn {
    flex: 1;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
    padding: 0.75rem;
    border: none;
    background: none;
    color: var(--text-secondary);
    border-radius: 6px;
    cursor: pointer;
    transition: all 0.2s ease;
    font-size: 0.875rem;
  }

  .category-btn:hover {
    color: var(--category-color);
    background-color: var(--bg-secondary);
  }

  .category-btn.active {
    color: var(--category-color);
    background-color: var(--bg-secondary);
  }

  .notifications-list {
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
  }

  .empty-state {
    text-align: center;
    padding: 2rem;
    color: var(--text-secondary);
    background-color: var(--bg-tertiary);
    border-radius: 8px;
  }

  @media (max-width: 640px) {
    .categories {
      flex-direction: column;
    }

    .category-btn {
      justify-content: flex-start;
    }
  }
</style>