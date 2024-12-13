<script lang="ts">
  export let settings: {
    revealRoles: string;
    forceVote: boolean;
    majorityVote: number;
    mafiaKillPower: number;
    deadlockPrevention: number;
    hostRoleSelection: boolean;
    hideSetup: boolean;
    preventNightDiscussion: boolean;
    mafiaLosesAfter: number;
    townLosesAfter: number;
  };

  const revealRoleOptions = [
    { value: 'allReveal', label: 'On' },
    { value: 'alignmentReveal', label: 'Reveal alignment only' },
    { value: 'noReveal', label: 'Off' }
  ];

  const majorityOptions = [
    { value: -1, label: 'Turned off' },
    { value: 51, label: 'Simple majority' },
    { value: 66, label: 'Two-thirds majority' },
    { value: 75, label: 'Three-quarters majority' }
  ];

  const killPowerOptions = [
    { value: 0, label: 'Turned off' },
    { value: 1, label: 'Two kill power always' },
    { value: 2, label: 'Two kill power until 1' },
    { value: 3, label: 'Two kill power until 2' },
    { value: 4, label: 'Two kill power until 3' },
    { value: 5, label: 'Two kill power until 4' },
    { value: 6, label: 'Two kill power until 5' },
    { value: 7, label: 'Two kill power until 6' }
  ];

  const deadlockOptions = [
    { value: -1, label: 'Punish randomly' },
    { value: 5, label: 'Punish initiators' },
    { value: 6, label: 'Punish responders' },
    { value: -2, label: 'Disable meteor' }
  ];
</script>

<div class="settings-section">
  <h3>Mechanics Settings</h3>

  <div class="setting-group">
    <label>
      Reveal Roles Upon Death
      <select bind:value={settings.revealRoles}>
        {#each revealRoleOptions as option}
          <option value={option.value}>{option.label}</option>
        {/each}
      </select>
    </label>
  </div>

  <div class="setting-group">
    <label class="checkbox-label">
      <input 
        type="checkbox" 
        bind:checked={settings.forceVote}
      />
      Force Vote
    </label>
  </div>

  <div class="setting-group">
    <label>
      Finalize Vote on Majority
      <select bind:value={settings.majorityVote}>
        {#each majorityOptions as option}
          <option value={option.value}>{option.label}</option>
        {/each}
      </select>
    </label>
  </div>

  <div class="setting-group">
    <label>
      Extra Mafia Kill Power
      <select bind:value={settings.mafiaKillPower}>
        {#each killPowerOptions as option}
          <option value={option.value}>{option.label}</option>
        {/each}
      </select>
    </label>
  </div>

  <div class="setting-group">
    <label>
      Deadlock Prevention
      <select bind:value={settings.deadlockPrevention}>
        {#each deadlockOptions as option}
          <option value={option.value}>{option.label}</option>
        {/each}
      </select>
    </label>
  </div>

  <div class="setting-group">
    <label class="checkbox-label">
      <input 
        type="checkbox" 
        bind:checked={settings.hostRoleSelection}
      />
      Host Role Selection
    </label>
  </div>

  <div class="setting-group">
    <label class="checkbox-label">
      <input 
        type="checkbox" 
        bind:checked={settings.hideSetup}
      />
      Hide Setup
    </label>
  </div>

  <div class="setting-group">
    <label class="checkbox-label">
      <input 
        type="checkbox" 
        bind:checked={settings.preventNightDiscussion}
      />
      Prevent Night Meeting Discussion
    </label>
  </div>

  <div class="setting-group">
    <label>
      Mafia Loses After: {settings.mafiaLosesAfter} rounds
      <input 
        type="range" 
        bind:value={settings.mafiaLosesAfter} 
        min="0" 
        max="10" 
        step="1"
      />
    </label>
  </div>

  <div class="setting-group">
    <label>
      Town Loses After: {settings.townLosesAfter} rounds
      <input 
        type="range" 
        bind:value={settings.townLosesAfter} 
        min="0" 
        max="20" 
        step="1"
      />
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