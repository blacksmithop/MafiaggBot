<script lang="ts">
  import { navigate } from "svelte-routing";
  import { LogOut, Settings, User } from 'lucide-svelte';
  
  const menuItems = [
    { icon: User, label: 'Profile', href: '/profile' },
    { icon: Settings, label: 'Settings', href: '/settings' },
    { icon: LogOut, label: 'Logout', href: '/logout' }
  ];

  function handleMenuClick(href: string) {
    if (href === '/logout') {
      // Handle logout logic
      return;
    }
    navigate(href);
  }
</script>

<div class="dropdown">
  <div class="user-info">
    <img 
      src="https://api.dicebear.com/7.x/avataaars/svg?seed=user123" 
      alt="User" 
      class="avatar"
    />
    <div class="user-details">
      <div class="name">Player123</div>
    </div>
  </div>
  
  <div class="menu-items">
    {#each menuItems as item}
      <button class="menu-item" on:click={() => handleMenuClick(item.href)}>
        <svelte:component this={item.icon} size={18} />
        <span>{item.label}</span>
      </button>
    {/each}
  </div>
</div>

<style>
  .dropdown {
    position: absolute;
    top: calc(100% + 0.5rem);
    right: 0;
    width: 240px;
    background-color: var(--bg-secondary);
    border: 1px solid var(--bg-tertiary);
    border-radius: 8px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    z-index: 100;
  }

  .user-info {
    display: flex;
    align-items: center;
    gap: 1rem;
    padding: 1rem;
    border-bottom: 1px solid var(--bg-tertiary);
  }

  .avatar {
    width: 40px;
    height: 40px;
    border-radius: 50%;
  }

  .user-details {
    flex: 1;
  }

  .name {
    font-weight: 600;
  }

  .menu-items {
    padding: 0.5rem;
  }

  .menu-item {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    width: 100%;
    padding: 0.75rem;
    color: var(--text-primary);
    background: none;
    border: none;
    cursor: pointer;
    border-radius: 6px;
    transition: all 0.2s ease;
    text-align: left;
  }

  .menu-item:hover {
    background-color: var(--bg-tertiary);
  }

  .menu-item:last-child {
    color: #ef4444;
  }
</style>