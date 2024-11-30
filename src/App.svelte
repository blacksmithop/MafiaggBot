<script lang="ts">
  import { Router, Route } from "svelte-routing";
  import Sidebar from "./lib/components/Sidebar.svelte";
  import Header from "./lib/components/Header.svelte";
  import Footer from "./lib/components/Footer.svelte";
  import PlayerSearch from "./lib/components/PlayerSearch.svelte";
  import GameStats from "./lib/components/GameStats.svelte";
  import Dashboard from "./lib/components/Dashboard.svelte";
  import Settings from "./lib/components/Settings.svelte";
  import Privacy from "./lib/components/Privacy.svelte";
</script>

<Router>
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
      </main>
      <Footer />
    </div>
  </div>
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