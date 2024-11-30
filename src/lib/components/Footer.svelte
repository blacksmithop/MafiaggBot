<script lang="ts">
  import { navigate } from "svelte-routing";
  import { Heart } from 'lucide-svelte';

  function goToPrivacy() {
    navigate("/privacy");
  }
</script>

<footer class="footer">
  <div class="footer-content">
    <div class="footer-left">
      <span>© 2024 blacksmithop</span>
    </div>
    <div class="footer-center">
      Made with <Heart size={16} class="heart-icon" /> by the Mafia.gg community
    </div>
    <div class="footer-right">
      <button on:click={goToPrivacy}>Privacy</button>
      <a href="mailto:angstycoder101@gmail.com">Contact</a>
    </div>
  </div>
</footer>

<style>
  .footer {
    position: sticky;
    bottom: 0;
    width: 100%;
    background-color: var(--bg-secondary);
    border-top: 1px solid var(--bg-tertiary);
    padding: 1rem 0;
    margin-top: auto;
  }

  .footer-content {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 2rem;
    max-width: 1200px;
    margin: 0 auto;
  }

  .footer-center {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    color: var(--text-secondary);
  }

  :global(.heart-icon) {
    color: var(--accent);
  }

  .footer-right {
    display: flex;
    gap: 1.5rem;
  }

  .footer-right button,
  .footer-right a {
    color: var(--text-secondary);
    text-decoration: none;
    background: none;
    border: none;
    cursor: pointer;
    padding: 0;
    font-size: inherit;
    transition: color 0.2s;
  }

  .footer-right button:hover,
  .footer-right a:hover {
    color: var(--text-primary);
  }

  @media (max-width: 768px) {
    .footer-content {
      flex-direction: column;
      gap: 1rem;
      text-align: center;
    }

    .footer-right {
      justify-content: center;
    }
  }
</style>