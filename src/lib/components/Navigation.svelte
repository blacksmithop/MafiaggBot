<script lang="ts">
  import { Link } from "svelte-routing";
</script>

<nav class="navigation">
  <div class="container nav-content">
    <div class="logo">Mafia.gg Stats</div>
    <div class="nav-links">
      <Link to="/">Home</Link>
      <Link to="/player-stats">Player Stats</Link>
      <Link to="/game-stats">Game Stats</Link>
    </div>
  </div>
</nav>

<style>
  .navigation {
    background-color: var(--bg-tertiary);
    padding: 1rem 0;
    margin-bottom: 2rem;
  }

  .nav-content {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .logo {
    font-size: 1.5rem;
    font-weight: bold;
    color: var(--text-primary);
  }

  .nav-links {
    display: flex;
    gap: 2rem;
  }

  .nav-links :global(a) {
    color: var(--text-secondary);
    text-decoration: none;
    transition: color 0.2s;
  }

  .nav-links :global(a:hover) {
    color: var(--text-primary);
  }
</style>