<script lang="ts">
  import { format } from 'date-fns';

  const notifications = [
    {
      id: 1,
      author: "GameMaster",
      message: "Your game report is ready!",
      datetime: new Date(Date.now() - 1000 * 60 * 30),
      read: false
    },
    {
      id: 2,
      author: "System",
      message: "New achievement unlocked: Perfect Town Game",
      datetime: new Date(Date.now() - 1000 * 60 * 60 * 2),
      read: false
    },
    {
      id: 3,
      author: "MafiaBot",
      message: "You've been invited to a custom game",
      datetime: new Date(Date.now() - 1000 * 60 * 60 * 24),
      read: true
    }
  ];
</script>

<div class="dropdown">
  <div class="dropdown-header">
    <h3>Notifications</h3>
    <button class="mark-all-read">Mark all as read</button>
  </div>
  <div class="notifications-list">
    {#each notifications as notification}
      <div class="notification-item" class:unread={!notification.read}>
        <div class="notification-content">
          <div class="author">{notification.author}</div>
          <div class="message">{notification.message}</div>
          <div class="datetime">
            {format(notification.datetime, 'MMM d, h:mm a')}
          </div>
        </div>
      </div>
    {/each}
  </div>
  <div class="dropdown-footer">
    <a href="/notifications">View all notifications</a>
  </div>
</div>

<style>
  .dropdown {
    position: absolute;
    top: calc(100% + 0.5rem);
    right: 0;
    width: 320px;
    background-color: var(--bg-secondary);
    border: 1px solid var(--bg-tertiary);
    border-radius: 8px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    z-index: 100;
  }

  .dropdown-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1rem;
    border-bottom: 1px solid var(--bg-tertiary);
  }

  .dropdown-header h3 {
    font-size: 1rem;
    font-weight: 600;
  }

  .mark-all-read {
    background: none;
    border: none;
    color: var(--accent);
    font-size: 0.875rem;
    cursor: pointer;
  }

  .notifications-list {
    max-height: 400px;
    overflow-y: auto;
  }

  .notification-item {
    padding: 1rem;
    border-bottom: 1px solid var(--bg-tertiary);
    transition: background-color 0.2s ease;
  }

  .notification-item:hover {
    background-color: var(--bg-tertiary);
  }

  .notification-item.unread {
    background-color: var(--bg-tertiary);
  }

  .author {
    font-weight: 600;
    margin-bottom: 0.25rem;
  }

  .message {
    color: var(--text-secondary);
    font-size: 0.875rem;
    margin-bottom: 0.5rem;
  }

  .datetime {
    font-size: 0.75rem;
    color: var(--text-secondary);
  }

  .dropdown-footer {
    padding: 0.75rem;
    text-align: center;
    border-top: 1px solid var(--bg-tertiary);
  }

  .dropdown-footer a {
    color: var(--accent);
    text-decoration: none;
    font-size: 0.875rem;
  }

  .dropdown-footer a:hover {
    text-decoration: underline;
  }
</style>