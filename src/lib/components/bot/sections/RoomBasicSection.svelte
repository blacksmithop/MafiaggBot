<script lang="ts">
  import DeckSelect from '../DeckSelect.svelte';
  
  export let name: string;
  export let deck: string;
</script>

<div class="section">
  <div class="form-group">
    <label for="name">Room Name</label>
    <input
      type="text"
      id="name"
      bind:value={name}
      placeholder="Enter room name"
    />
  </div>

  <div class="form-group">
    <label for="deck">Deck</label>
    <DeckSelect 
      value={deck} 
      onChange={(value) => deck = value} 
    />
  </div>
</div>

<style>
  .section {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
  }

  .form-group {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
  }

  label {
    color: var(--text-secondary);
    font-size: 0.875rem;
  }

  input {
    width: 100%;
    padding: 0.75rem;
    background-color: var(--bg-tertiary);
    border: 1px solid var(--bg-tertiary);
    color: var(--text-primary);
    border-radius: 6px;
    transition: all 0.2s ease;
  }

  input:focus {
    outline: none;
    border-color: var(--accent);
  }
</style>