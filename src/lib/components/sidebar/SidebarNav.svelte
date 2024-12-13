<script lang="ts">
  import { 
    LayoutDashboard,
    Users,
    GamepadIcon,
    Github,
    Bot,
    Bell,
    FileText
  } from 'lucide-svelte';
  import SidebarItem from './SidebarItem.svelte';
  
  export let isExpanded: boolean;

  const navItems = [
    { path: "/", icon: LayoutDashboard, text: "Dashboard" },
    { path: "/player-stats", icon: Users, text: "Player Stats" },
    { path: "/game-stats", icon: GamepadIcon, text: "Game Stats" },
    { path: "/reports", icon: FileText, text: "Reports" },
    { path: "/notifications", icon: Bell, text: "Notifications" },
    { path: "/bot", icon: Bot, text: "Bot" },
    { 
      path: "https://github.com/blacksmithop/MafiaggBot",
      icon: Github,
      text: "GitHub",
      external: true
    }
  ];
</script>

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
      />
    {/if}
  {/each}
</nav>

<style>
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
</style>