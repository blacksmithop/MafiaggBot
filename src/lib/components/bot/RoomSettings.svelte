<script lang="ts">
    import { Plus, Minus } from 'lucide-svelte';
  
    export let roomSettings: { [key: string]: any } = {};
    export let onChange: (settings: { [key: string]: any }) => void;
  
    const timerSettings = {
      dayLength: 3,
      nightLength: 9,
      scaleTimer: false,
    };
  
    const mechanicsSettings = {
      revealRoles: "allReveal",
      forceVote: false,
      majorityVote: -1,
      mafiaKillPower: 0,
      deadlockPrevention: -1,
      hostRoleSelection: false,
      hideSetup: false,
      preventNightDiscussion: false,
    };
  
    const revealRoleOptions = [
      { value: "allReveal", label: "On" },
      { value: "alignmentReveal", label: "Reveal alignment only" },
      { value: "noReveal", label: "Off" },
    ];
  
    const majorityOptions = [
      { value: -1, label: "Turned off" },
      { value: 51, label: "Simple majority" },
      { value: 66, label: "Two-thirds majority" },
      { value: 75, label: "Three-quarters majority" },
    ];
  
    function updateSetting(group: "timer" | "mechanics", key: string, value: any) {
      const updatedSettings = { ...roomSettings };
      if (group === "timer") {
        updatedSettings[key] = value;
      } else if (group === "mechanics") {
        updatedSettings[key] = value;
      }
      onChange(updatedSettings);
    }
  </script>
  
  <div class="room-settings">
    <div class="section">
      <h2>Timer Settings</h2>
      <div class="setting">
        <label>Day Length</label>
        <button on:click={() => updateSetting("timer", "dayLength", timerSettings.dayLength - 1)} disabled={timerSettings.dayLength <= 3}>
          <Minus size={16} />
        </button>
        <span>{timerSettings.dayLength} minutes</span>
        <button on:click={() => updateSetting("timer", "dayLength", timerSettings.dayLength + 1)} disabled={timerSettings.dayLength >= 20}>
          <Plus size={16} />
        </button>
      </div>
      <div class="setting">
        <label>Night Length</label>
        <button on:click={() => updateSetting("timer", "nightLength", timerSettings.nightLength - 1)} disabled={timerSettings.nightLength <= 1}>
          <Minus size={16} />
        </button>
        <span>{timerSettings.nightLength} minutes</span>
        <button on:click={() => updateSetting("timer", "nightLength", timerSettings.nightLength + 1)} disabled={timerSettings.nightLength >= 9}>
          <Plus size={16} />
        </button>
      </div>
      <div class="setting">
        <label>
          <input type="checkbox" bind:checked={timerSettings.scaleTimer} on:change={() => updateSetting("timer", "scaleTimer", timerSettings.scaleTimer)} />
          Scale Timer
        </label>
      </div>
    </div>
  
    <div class="section">
      <h2>Mechanics Settings</h2>
      <div class="setting">
        <label>Reveal Roles Upon Death</label>
        <select bind:value={mechanicsSettings.revealRoles} on:change={() => updateSetting("mechanics", "revealRoles", mechanicsSettings.revealRoles)}>
          {#each revealRoleOptions as option}
            <option value={option.value}>{option.label}</option>
          {/each}
        </select>
      </div>
      <div class="setting">
        <label>
          <input type="checkbox" bind:checked={mechanicsSettings.forceVote} on:change={() => updateSetting("mechanics", "forceVote", mechanicsSettings.forceVote)} />
          Force Vote
        </label>
      </div>
      <div class="setting">
        <label>Finalize Vote on Majority</label>
        <select bind:value={mechanicsSettings.majorityVote} on:change={() => updateSetting("mechanics", "majorityVote", mechanicsSettings.majorityVote)}>
          {#each majorityOptions as option}
            <option value={option.value}>{option.label}</option>
          {/each}
        </select>
      </div>
    </div>
  </div>
  
  <style>
    .room-settings {
      display: flex;
      flex-direction: column;
      gap: 2rem;
      padding: 1rem;
    }
  
    .section {
      background: var(--bg-tertiary);
      border-radius: 8px;
      padding: 1rem;
      display: flex;
      flex-direction: column;
      gap: 1rem;
    }
  
    .section h2 {
      color: var(--text-primary);
      margin-bottom: 0.5rem;
    }
  
    .setting {
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }
  
    .setting label {
      font-weight: 500;
      color: var(--text-secondary);
      flex: 1;
    }
  
    button {
      border: none;
      background: var(--bg-secondary);
      color: var(--text-secondary);
      border-radius: 4px;
      cursor: pointer;
      width: 32px;
      height: 32px;
      display: flex;
      align-items: center;
      justify-content: center;
    }
  
    button:disabled {
      opacity: 0.5;
      cursor: not-allowed;
    }
  
    select {
      background: var(--bg-secondary);
      color: var(--text-secondary);
      border-radius: 4px;
      border: none;
      padding: 0.5rem;
    }
  
    input[type="checkbox"] {
      margin-right: 0.5rem;
    }
  </style>
  