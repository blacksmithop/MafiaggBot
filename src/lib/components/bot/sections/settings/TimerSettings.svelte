<script lang="ts">
  export let settings: {
    dayLength: number;
    nightLength: number;
    scaleTimer: boolean;
    gameStart: string;
    disableVoteLock: boolean;
  };

  const gameStartOptions = [
    { value: 'off', label: 'Night (Normal)' },
    { value: 'mafiaNKn1', label: 'Night (No Kill Night 1)' },
    { value: 'dayStart', label: 'Day (Uninformed)' },
    { value: 'dawnStart', label: 'Day (Informed)' }
  ];
</script>

<div class="settings-section">
  <h3>Timer Settings</h3>
  
  <div class="setting-group">
    <label>
      Day Length: {settings.dayLength} minutes
      <input 
        type="range" 
        bind:value={settings.dayLength} 
        min="3" 
        max="20" 
        step="1"
      />
    </label>
  </div>

  <div class="setting-group">
    <label>
      Night Length: {settings.nightLength} minutes
      <input 
        type="range" 
        bind:value={settings.nightLength} 
        min="1" 
        max="9" 
        step="1"
      />
    </label>
  </div>

  <div class="setting-group">
    <label class="checkbox-label">
      <input 
        type="checkbox" 
        bind:checked={settings.scaleTimer}
      />
      Scale Timer
    </label>
  </div>

  <div class="setting-group">
    <label>
      Game Start
      <select bind:value={settings.gameStart}>
        {#each gameStartOptions as option}
          <option value={option.value}>{option.label}</option>
        {/each}
      </select>
    </label>
  </div>

  <div class="setting-group">
    <label class="checkbox-label">
      <input 
        type="checkbox" 
        bind:checked={settings.disableVoteLock}
      />
      Disable Vote Lock Period
    </label>
  </div>
</div>

<style>
  .settings-section {
    background: var(--bg-tertiary);
    border-radius: 8px;
    padding: 1rem;
    margin-bottom: 1rem;
  }

  h3 {
    margin-bottom: 1rem;
    color: var(--text-primary);
  }

  .setting-group {
    margin-bottom: 1rem;
  }

  label {
    display: block;
    color: var(--text-secondary);
    margin-bottom: 0.5rem;
  }

  input[type="range"] {
    width: 100%;
    margin-top: 0.5rem;
  }

  select {
    width: 100%;
    padding: 0.5rem;
    background: var(--bg-secondary);
    border: 1px solid var(--bg-tertiary);
    color: var(--text-primary);
    border-radius: 4px;
    margin-top: 0.5rem;
  }

  .checkbox-label {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    cursor: pointer;
  }

  input[type="checkbox"] {
    width: 1rem;
    height: 1rem;
  }
</style>