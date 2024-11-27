<script lang="ts">
  import { Menu, X } from 'lucide-svelte';
  
  export let isExpanded: boolean;
  export let onClick: () => void;
</script>

<button class="toggle-btn" on:click={onClick}>
  {#if isExpanded}
    <X size={20} />
  {:else}
    <Menu size={20} />
  {/if}
</button>

<style>
  .toggle-btn {
    position: fixed;
    top: 1rem;
    left: 1rem;
    z-index: 110;
    background-color: var(--bg-secondary);
    border: 1px solid var(--bg-tertiary);
    color: var(--text-secondary);
    cursor: pointer;
    padding: 0.625rem;
    border-radius: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.2s ease;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
  }

  .toggle-btn:hover {
    background-color: var(--bg-tertiary);
    color: var(--text-primary);
    transform: scale(1.05);
  }

  .toggle-btn:active {
    transform: scale(0.95);
  }
</style>