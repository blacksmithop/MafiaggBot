<script lang="ts">
  import { 
    LayoutDashboard,
    Users,
    GamepadIcon,
    TrendingUp,
    Settings,
    HelpCircle
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
    { path: "/trends", icon: TrendingUp, text: "Trends" },
    { path: "/settings", icon: Settings, text: "Settings" },
    { path: "/help", icon: HelpCircle, text: "Help" }
  ];

  // Get current path for active state
  let currentPath = window.location.pathname;
</script>

<ToggleButton {isExpanded} onClick={toggleSidebar} />

<aside class="sidebar" class:collapsed={!isExpanded}>
  <div class="sidebar-content">
    <nav class="sidebar-nav">
      {#each navItems as { path, icon, text }}
        <SidebarItem
          {path}
          {icon}
          {text}
          {isExpanded}
          isActive={currentPath === path}
        />
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