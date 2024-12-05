<script lang="ts">
  import SidebarNav from './sidebar/SidebarNav.svelte';
  import ToggleButton from './sidebar/ToggleButton.svelte';

  let isExpanded = true;

  const toggleSidebar = () => {
    isExpanded = !isExpanded;
    document.body.style.setProperty('--sidebar-width', isExpanded ? '240px' : '72px');
  };
</script>

<ToggleButton {isExpanded} onClick={toggleSidebar} />

<aside class="sidebar" class:collapsed={!isExpanded}>
  <div class="sidebar-content">
    <SidebarNav {isExpanded} />
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