<script lang="ts">
  import { Search } from 'lucide-svelte';
  import { selectedChat } from '../../stores/chat';
  import type { Chat } from '../../types/Chat';
  
  const chats: Chat[] = [
    {
      id: '1',
      username: 'Alice',
      avatar: 'alice123',
      lastMessage: 'Good game! That was intense!',
      timestamp: new Date(Date.now() - 1000 * 60 * 5),
      unread: 2
    },
    {
      id: '2',
      username: 'Bob',
      avatar: 'bob456',
      lastMessage: 'I think the Jester is trying to get lynched',
      timestamp: new Date(Date.now() - 1000 * 60 * 30),
      unread: 0
    },
    {
      id: '3',
      username: 'Charlie',
      avatar: 'charlie789',
      lastMessage: '😂 That was hilarious!',
      timestamp: new Date(Date.now() - 1000 * 60 * 60),
      unread: 1
    }
  ];

  function selectChat(chat: Chat) {
    selectedChat.set(chat);
  }

  function getTimeString(date: Date): string {
    const now = new Date();
    const diff = now.getTime() - date.getTime();
    const minutes = Math.floor(diff / (1000 * 60));
    
    if (minutes < 1) return 'Just now';
    if (minutes < 60) return `${minutes}m`;
    if (minutes < 1440) return `${Math.floor(minutes / 60)}h`;
    return `${Math.floor(minutes / 1440)}d`;
  }
</script>

<div class="chat-list">
  <div class="header">
    <h3>Messages</h3>
  </div>

  <div class="search-bar">
    <Search size={16} />
    <input type="text" placeholder="Search messages..." />
  </div>

  <div class="chats">
    {#each chats as chat}
      <button 
        class="chat-item" 
        class:unread={chat.unread > 0}
        on:click={() => selectChat(chat)}
      >
        <img 
          src={`https://api.dicebear.com/7.x/avataaars/svg?seed=${chat.avatar}`} 
          alt={chat.username}
          class="avatar"
        />
        <div class="chat-info">
          <div class="top-line">
            <span class="username">{chat.username}</span>
            <span class="time">{getTimeString(chat.timestamp)}</span>
          </div>
          <div class="bottom-line">
            <span class="last-message">{chat.lastMessage}</span>
            {#if chat.unread > 0}
              <span class="unread-badge">{chat.unread}</span>
            {/if}
          </div>
        </div>
      </button>
    {/each}
  </div>
</div>

<style>
  .chat-list {
    height: 100%;
    display: flex;
    flex-direction: column;
  }

  .header {
    padding: 1rem;
    border-bottom: 1px solid var(--bg-tertiary);
  }

  .header h3 {
    margin: 0;
    font-size: 1.25rem;
  }

  .search-bar {
    position: relative;
    padding: 0.75rem;
    border-bottom: 1px solid var(--bg-tertiary);
  }

  .search-bar :global(svg) {
    position: absolute;
    left: 1.25rem;
    top: 50%;
    transform: translateY(-50%);
    color: var(--text-secondary);
    pointer-events: none;
  }

  .search-bar input {
    width: 100%;
    padding: 0.5rem 0.5rem 0.5rem 2rem;
    background-color: var(--bg-tertiary);
    border: none;
    border-radius: 6px;
    color: var(--text-primary);
  }

  .search-bar input:focus {
    outline: none;
  }

  .chats {
    flex: 1;
    overflow-y: auto;
  }

  .chat-item {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    width: 100%;
    padding: 0.75rem;
    background: none;
    border: none;
    cursor: pointer;
    text-align: left;
    border-bottom: 1px solid var(--bg-tertiary);
    transition: background-color 0.2s ease;
  }

  .chat-item:hover {
    background-color: var(--bg-tertiary);
  }

  .avatar {
    width: 40px;
    height: 40px;
    border-radius: 50%;
  }

  .chat-info {
    flex: 1;
    min-width: 0;
  }

  .top-line {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 0.25rem;
  }

  .username {
    font-weight: 500;
    color: var(--text-primary);
  }

  .time {
    font-size: 0.75rem;
    color: var(--text-secondary);
  }

  .bottom-line {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .last-message {
    font-size: 0.875rem;
    color: var(--text-secondary);
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    margin-right: 0.5rem;
  }

  .unread-badge {
    background-color: var(--accent);
    color: white;
    font-size: 0.75rem;
    padding: 0.125rem 0.375rem;
    border-radius: 999px;
  }

  .chat-item.unread .username {
    font-weight: 600;
  }

  .chat-item.unread .last-message {
    color: var(--text-primary);
    font-weight: 500;
  }
</style>