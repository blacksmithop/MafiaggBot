<script lang="ts">
  import { Search, Bell, LogOut, Settings, User } from 'lucide-svelte';
  import NotificationDropdown from './header/NotificationDropdown.svelte';
  import UserDropdown from './header/UserDropdown.svelte';
  // import SearchBar from './header/SearchBar.svelte';
  
  let showNotifications = false;
  let showUserMenu = false;
  
  function handleClickOutside(event: MouseEvent) {
    const target = event.target as HTMLElement;
    if (!target.closest('.notification-btn')) showNotifications = false;
    if (!target.closest('.user-profile')) showUserMenu = false;
  }
</script>

<svelte:window on:click={handleClickOutside} />

<header class="header">
  <div class="header-content">
    <div class="header-left">
      <!-- <SearchBar /> -->
    </div>
    <div class="header-actions">
      <div class="notification-wrapper">
        <button 
          class="notification-btn"
          on:click={() => showNotifications = !showNotifications}
        >
          <Bell size={20} />
          <span class="notification-badge">3</span>
        </button>
        {#if showNotifications}
          <NotificationDropdown />
        {/if}
      </div>
      
      <div class="user-wrapper">
        <button 
          class="user-profile"
          on:click={() => showUserMenu = !showUserMenu}
        >
          <img 
            src="https://api.dicebear.com/7.x/avataaars/svg?seed=user123" 
            alt="User" 
            class="avatar"
          />
          <span class="username">Player123</span>
        </button>
        {#if showUserMenu}
          <UserDropdown />
        {/if}
      </div>
    </div>
  </div>
</header>

<style>
  .header {
    position: fixed;
    top: 0;
    right: 0;
    left: var(--sidebar-width);
    height: var(--header-height);
    background-color: var(--bg-secondary);
    border-bottom: 1px solid var(--bg-tertiary);
    z-index: 90;
    transition: left 0.3s ease;
  }

  .header-content {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 2rem;
    height: 100%;
    max-width: 1400px;
    margin: 0 auto;
  }

  .header-left {
    flex: 1;
    display: flex;
    justify-content: center;
  }

  .header-actions {
    display: flex;
    align-items: center;
    gap: 1.5rem;
  }

  .notification-wrapper, .user-wrapper {
    position: relative;
  }

  .notification-btn {
    position: relative;
    background: none;
    border: none;
    color: var(--text-secondary);
    cursor: pointer;
    padding: 0.5rem;
    border-radius: 6px;
    transition: all 0.2s ease;
  }

  .notification-btn:hover {
    background-color: var(--bg-tertiary);
    color: var(--text-primary);
  }

  .notification-badge {
    position: absolute;
    top: 0;
    right: 0;
    background-color: var(--accent);
    color: white;
    font-size: 0.75rem;
    padding: 0.125rem 0.375rem;
    border-radius: 999px;
    transform: translate(25%, -25%);
  }

  .user-profile {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    cursor: pointer;
    padding: 0.5rem 0.75rem;
    border-radius: 6px;
    background: none;
    border: none;
    color: var(--text-primary);
    transition: all 0.2s ease;
  }

  .user-profile:hover {
    background-color: var(--bg-tertiary);
  }

  .avatar {
    width: 32px;
    height: 32px;
    border-radius: 50%;
  }

  .username {
    color: var(--text-primary);
    font-weight: 500;
  }

  @media (max-width: 768px) {
    .username {
      display: none;
    }
  }
</style>