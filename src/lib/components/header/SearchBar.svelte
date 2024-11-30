<script lang="ts">
  import { Search } from 'lucide-svelte';
</script>

<div class="search-container">
</div>

<style>
  .search-container {
    width: 100%;
    max-width: 600px;
    padding: 0 1rem;
  }

  .search-bar {
    position: relative;
    width: 100%;
  }

  .search-icon {
    position: absolute;
    left: 12px;
    top: 50%;
    transform: translateY(-50%);
    color: var(--text-secondary);
    pointer-events: none;
  }

  input {
    width: 100%;
    padding: 0.75rem 1rem 0.75rem 2.5rem;
    border-radius: 8px;
    border: 1px solid var(--bg-tertiary);
    background-color: var(--bg-primary);
    color: var(--text-primary);
    font-size: 0.95rem;
    transition: all 0.2s ease;
  }

  input:focus {
    outline: none;
    border-color: var(--accent);
    box-shadow: 0 0 0 2px var(--accent-alpha);
  }

  input::placeholder {
    color: var(--text-secondary);
  }
</style>