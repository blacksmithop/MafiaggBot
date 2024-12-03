<script lang="ts">
  import RoleSelector from '../RoleSelector.svelte';
  
  export let selectedRoles: { [key: string]: number };
</script>

<div class="section">
  <RoleSelector 
    {selectedRoles}
    onChange={(roles) => selectedRoles = roles}
  />
</div>

<style>
  .section {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
  }

  :global(.role-selector) {
    --town-color: #3b82f6;
    --mafia-color: #ef4444;
    --neutral-color: #8b5cf6;
  }

  :global(.alignment-section:nth-child(1) .alignment-title) {
    color: var(--town-color);
  }

  :global(.alignment-section:nth-child(2) .alignment-title) {
    color: var(--mafia-color);
  }

  :global(.alignment-section:nth-child(3) .alignment-title) {
    color: var(--neutral-color);
  }
</style>