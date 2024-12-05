<script lang="ts">
  import RoomSettings from '../RoomSettings.svelte';

  export let roomSettings: { [key: string]: any } = {};
</script>

<div class="section">
  <RoomSettings 
    {roomSettings}
    onChange={(settings) => roomSettings = settings}
  />
</div>

<style>
  .section {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
    align-items: center;
    justify-content: center;
    height: 100%;
    min-height: 300px;
  }

  .placeholder {
    color: var(--text-secondary);
    font-style: italic;
  }
</style>