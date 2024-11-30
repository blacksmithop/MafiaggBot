<script lang="ts">
  let settings = {
    theme: 'dark',
    notifications: true,
    soundEffects: true,
    language: 'en',
    autoJoinLobby: false
  };

  function handleSettingChange(setting: string, value: any) {
    settings = { ...settings, [setting]: value };
  }
</script>

<div class="settings-container">
  <div class="card">
    <h2 class="section-title">Settings</h2>
    
    <div class="settings-group">
      <h3>Appearance</h3>
      <div class="setting-item">
        <label for="theme">Theme</label>
        <select 
          id="theme" 
          bind:value={settings.theme}
          on:change={(e) => handleSettingChange('theme', e.target.value)}
        >
          <option value="dark">Dark</option>
          <option value="light">Light</option>
        </select>
      </div>
    </div>

    <div class="settings-group">
      <h3>Notifications</h3>
      <div class="setting-item">
        <label for="notifications">Enable Notifications</label>
        <input 
          type="checkbox" 
          id="notifications"
          bind:checked={settings.notifications}
          on:change={(e) => handleSettingChange('notifications', e.target.checked)}
        />
      </div>
      <div class="setting-item">
        <label for="soundEffects">Sound Effects</label>
        <input 
          type="checkbox" 
          id="soundEffects"
          bind:checked={settings.soundEffects}
          on:change={(e) => handleSettingChange('soundEffects', e.target.checked)}
        />
      </div>
    </div>

    <div class="settings-group">
      <h3>Game Preferences</h3>
      <div class="setting-item">
        <label for="language">Language</label>
        <select 
          id="language"
          bind:value={settings.language}
          on:change={(e) => handleSettingChange('language', e.target.value)}
        >
          <option value="en">English</option>
          <option value="es">Español</option>
          <option value="fr">Français</option>
        </select>
      </div>
      <div class="setting-item">
        <label for="autoJoinLobby">Auto-join Lobby</label>
        <input 
          type="checkbox" 
          id="autoJoinLobby"
          bind:checked={settings.autoJoinLobby}
          on:change={(e) => handleSettingChange('autoJoinLobby', e.target.checked)}
        />
      </div>
    </div>
  </div>
</div>

<style>
  .settings-container {
    max-width: 800px;
    margin: 0 auto;
  }

  .settings-group {
    margin-bottom: 2rem;
  }

  .settings-group h3 {
    color: var(--text-primary);
    font-size: 1.25rem;
    margin-bottom: 1rem;
    padding-bottom: 0.5rem;
    border-bottom: 1px solid var(--bg-tertiary);
  }

  .setting-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1rem;
    background-color: var(--bg-tertiary);
    border-radius: 8px;
    margin-bottom: 0.75rem;
  }

  label {
    color: var(--text-primary);
    font-weight: 500;
  }

  select {
    background-color: var(--bg-secondary);
    color: var(--text-primary);
    border: 1px solid var(--bg-tertiary);
    padding: 0.5rem 1rem;
    border-radius: 6px;
    cursor: pointer;
  }

  select:focus {
    outline: none;
    border-color: var(--accent);
  }

  input[type="checkbox"] {
    width: 1.25rem;
    height: 1.25rem;
    cursor: pointer;
    accent-color: var(--accent);
  }
</style>