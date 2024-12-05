<script lang="ts">
  import { createEventDispatcher } from 'svelte';
  import type { Notification } from '../../types/Notification';
  import { Trophy, FileText, Users } from 'lucide-svelte';
  import { navigate } from 'svelte-routing';
  
  export let notification: Notification;
  
  const dispatch = createEventDispatcher();
  
  const typeIcons = {
    achievement: Trophy,
    game_report: FileText,
    invite: Users
  };

  const typeColors = {
    achievement: 'var(--success)',
    game_report: 'var(--accent)',
    invite: 'var(--neutral)'
  };
  
  function handleClick() {
    if (notification.type === 'game_report') {
      navigate('/game-stats');
    } else {
      dispatch('click', notification);
    }
  }
</script>

<div 
  class="notification-item" 
  class:unread={!notification.read}
  on:click={handleClick}
  style="--notification-color: {typeColors[notification.type]}"
>
  <div class="icon-wrapper" style="background-color: {typeColors[notification.type]}">
    <svelte:component this={typeIcons[notification.type]} size={20} />
  </div>
  <div class="content">
    <div class="title">{notification.title}</div>
    <div class="message">{notification.message}</div>
    <div class="time">
      {new Date(notification.datetime).toLocaleString()}
    </div>
  </div>
</div>

<style>
  .notification-item {
    display: flex;
    gap: 1rem;
    padding: 1rem;
    background-color: var(--bg-tertiary);
    border-radius: 8px;
    cursor: pointer;
    transition: all 0.2s ease;
    border-left: 4px solid var(--notification-color);
  }

  .notification-item:hover {
    transform: translateX(4px);
    background-color: color-mix(in srgb, var(--notification-color) 10%, var(--bg-tertiary));
  }

  .notification-item.unread {
    background-color: color-mix(in srgb, var(--notification-color) 5%, var(--bg-tertiary));
  }

  .icon-wrapper {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 40px;
    height: 40px;
    border-radius: 8px;
    color: white;
  }

  .content {
    flex: 1;
  }

  .title {
    font-weight: 500;
    margin-bottom: 0.25rem;
    color: var(--notification-color);
  }

  .message {
    color: var(--text-secondary);
    font-size: 0.875rem;
    margin-bottom: 0.5rem;
  }

  .time {
    font-size: 0.75rem;
    color: var(--text-secondary);
  }
</style>