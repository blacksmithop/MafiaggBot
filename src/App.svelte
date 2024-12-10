<script lang="ts">
  import { Router, Link, Route } from "svelte-routing";
  import { onMount } from "svelte";
  import { currentPath } from "./lib/stores/navigation";
  import Sidebar from "./lib/components/Sidebar.svelte";
  import Header from "./lib/components/Header.svelte";
  import Footer from "./lib/components/Footer.svelte";
  import PlayerSearch from "./lib/components/PlayerSearch.svelte";
  import GameStats from "./lib/components/GameStats.svelte";
  import Dashboard from "./lib/components/Dashboard.svelte";
  import Settings from "./lib/components/Settings.svelte";
  import Privacy from "./lib/components/Privacy.svelte";
  import Profile from "./lib/components/Profile.svelte";
  import BotManagement from "./lib/components/bot/BotManagement.svelte";
  import NotificationsPage from "./lib/components/notifications/NotificationsPage.svelte";
  import ReportsPage from "./lib/components/reports/ReportsPage.svelte";
  import Login from './lib/components/Login.svelte';
  import ChatButton from './lib/components/chat/ChatButton.svelte';
  import ChatWindow from './lib/components/chat/ChatWindow.svelte';
  
  let isAuthenticated = localStorage.getItem("isAuthenticated") === "true";
  isAuthenticated = true; // Temporary for development
  export let url = "";

  onMount(() => {
    currentPath.set(window.location.pathname);
    isAuthenticated = localStorage.getItem("isAuthenticated") === "true";
    isAuthenticated = true; // Temporary for development
    
    // Update current path on navigation
    window.addEventListener('popstate', () => {
      currentPath.set(window.location.pathname);
    });
  });
</script>

<Router {url}>
  {#if isAuthenticated}
  <div class="app-layout">
    <Sidebar />
    <div class="main-content">
      <Header />
      <main class="container">
        <Route path="/" component={Dashboard} />
        <Route path="/player-stats" component={PlayerSearch} />
        <Route path="/game-stats" component={GameStats} />
        <Route path="/settings" component={Settings} />
        <Route path="/privacy" component={Privacy} />
        <Route path="/profile" component={Profile} />
        <Route path="/bot" component={BotManagement} />
        <Route path="/notifications" component={NotificationsPage} />
        <Route path="/reports" component={ReportsPage} />
      </main>
      <ChatButton />
      <ChatWindow />
      <Footer />
    </div>
  </div>
  {:else}
  <Login />
  {/if}
</Router>

<style>
  .app-layout {
    display: flex;
    min-height: 100vh;
  }

  .main-content {
    flex: 1;
    margin-left: var(--sidebar-width);
    transition: margin-left 0.3s ease;
    display: flex;
    flex-direction: column;
    min-height: 100vh;
  }

  .container {
    padding: calc(var(--header-height) + 2rem) 2rem 2rem;
    flex: 1;
  }

  :global(body) {
    overflow-x: hidden;
  }

  @media (max-width: 768px) {
    .main-content {
      margin-left: 60px;
    }
  }
</style>