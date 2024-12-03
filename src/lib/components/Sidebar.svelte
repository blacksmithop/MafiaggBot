<script lang="ts">
  import { 
    LayoutDashboard,
    Users,
    GamepadIcon,
    Github,
    Bot
  } from 'lucide-svelte';
  import SidebarItem from './sidebar/SidebarItem.svelte';
  import ToggleButton from './sidebar/ToggleButton.svelte';

  let isExpanded = true;

  const toggleSidebar = () => {
    isExpanded = !isExpanded;
    document.body.style.setProperty('--sidebar-width', isExpanded ? '240px' : '72px');
  };

  const navItems = [
    { path: "/", icon: LayoutDashboard, text: "Dashboard" },
    { path: "/player-stats", icon: Users, text: "Player Stats" },
    { path: "/game-stats", icon: GamepadIcon, text: "Game Stats" },
    { path: "/bot", icon: Bot, text: "Bot" },
    { 
      path: "https://github.com/blacksmithop/MafiaggBot",
      icon: Github,
      text: "GitHub",
      external: true
    }
  ];

  // Get current path for active state
  let currentPath = window.location.pathname;
</script>

<ToggleButton {isExpanded} onClick={toggleSidebar} />

<aside class="sidebar" class:collapsed={!isExpanded}>
  <div class="sidebar-content">
    <nav class="sidebar-nav">
      {#each navItems as { path, icon, text, external }}
        {#if external}
          <a href={path} target="_blank" rel="noopener noreferrer" class="nav-item-wrapper">
            <div class="nav-item">
              <div class="icon-wrapper">
                <svelte:component this={icon} size={20} />
              </div>
              {#if isExpanded}
                <span class="text">{text}</span>
              {/if}
            </div>
          </a>
        {:else}
          <SidebarItem
            {path}
            {icon}
            {text}
            {isExpanded}
            isActive={currentPath === path}
          />
        {/if}
      {/each}
    </nav>
  </div>
</aside>

<style>
  .sidebar {
    position: fixed;
    left: 0;
    top: 0;
    height: 100vh;
    width: var(--sidebar-width);
    background-color: var(--bg-secondary);
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    box-shadow: 2px 0 5px rgba(0, 0, 0, 0.1);
    z-index: 100;
    overflow: hidden;
  }

  .sidebar.collapsed {
    width: 72px;
  }

  .sidebar-content {
    height: 100%;
    display: flex;
    flex-direction: column;
    padding-top: calc(var(--header-height) + 0.5rem);
  }

  .sidebar-nav {
    display: flex;
    flex-direction: column;
    gap: 0.25rem;
    padding: 0.5rem 0;
  }

  .nav-item-wrapper {
    margin: 0.125rem 0.75rem;
    border-radius: 8px;
    background-color: transparent;
    transition: all 0.2s ease;
    text-decoration: none;
  }

  .nav-item-wrapper:hover {
    background-color: var(--bg-tertiary);
  }

  .nav-item {
    display: flex;
    align-items: center;
    gap: 0.875rem;
    padding: 0.875rem 1rem;
    color: var(--text-secondary);
    transition: color 0.2s ease;
  }

  .nav-item-wrapper:hover .nav-item {
    color: var(--text-primary);
  }

  .icon-wrapper {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 24px;
    height: 24px;
  }

  .text {
    font-weight: 500;
    font-size: 0.9375rem;
    white-space: nowrap;
  }

  @media (max-width: 768px) {
    .sidebar {
      transform: translateX(-100%);
    }

    .sidebar.collapsed {
      transform: translateX(0);
      width: 72px;
    }
  }
</style>