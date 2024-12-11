<script lang="ts">
  import { format } from "date-fns";

  let displayName = "Player123";
  let avatarSeed = "user123";
  let joinDate = new Date(2023, 0, 15); // January 15, 2023

  function generateRandomSeed() {
    avatarSeed = Math.random().toString(36).substring(7);
  }

  function handleDisplayNameChange(event: Event) {
    const input = event.target as HTMLInputElement;
    displayName = input.value;
  }

  $: avatarUrl = `https://api.dicebear.com/7.x/avataaars/svg?seed=${avatarSeed}`;
</script>

<div class="profile-container">
  <div class="card">
    <h2 class="section-title">Edit Profile</h2>

    <div class="profile-content">
      <div class="avatar-section">
        <div class="avatar-container">
          <img src={avatarUrl} alt="User Avatar" class="avatar" />
        </div>
        <button class="randomize-btn" on:click={generateRandomSeed}>
          Randomize Avatar
        </button>
      </div>

      <div class="profile-details">
        <div class="form-group">
          <label for="displayName">Display Name</label>
          <input
            type="text"
            id="displayName"
            value={displayName}
            on:input={handleDisplayNameChange}
            maxlength="20"
          />
        </div>

        <div class="info-group">
          <label>Join Date</label>
          <span class="join-date">{format(joinDate, "MMMM d, yyyy")}</span>
        </div>
      </div>
    </div>
  </div>
</div>

<style>
  .profile-container {
    max-width: 600px;
    margin: 0 auto;
  }

  .profile-content {
    display: grid;
    gap: 2rem;
  }

  .section-title {
    text-align: center;
    font-size: 1.5rem;
    margin-bottom: 1.5rem;
  }
  .avatar-section {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1rem;
  }

  .avatar-container {
    width: 128px;
    height: 128px;
    border-radius: 50%;
    overflow: hidden;
    background-color: var(--bg-tertiary);
    padding: 0.5rem;
  }

  .avatar {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }

  .randomize-btn {
    background-color: var(--accent);
    color: white;
    border: none;
    padding: 0.75rem 1.5rem;
    border-radius: 6px;
    cursor: pointer;
    font-weight: 500;
    transition: opacity 0.2s;
  }

  .randomize-btn:hover {
    opacity: 0.9;
  }

  .profile-details {
    display: grid;
    gap: 1.5rem;
  }

  .form-group,
  .info-group {
    display: grid;
    gap: 0.5rem;
  }

  label {
    color: var(--text-secondary);
    font-size: 0.875rem;
  }

  input {
    background-color: var(--bg-tertiary);
    border: 1px solid var(--bg-tertiary);
    color: var(--text-primary);
    padding: 0.75rem;
    border-radius: 6px;
    font-size: 1rem;
    transition: all 0.2s ease;
  }

  input:focus {
    outline: none;
    border-color: var(--accent);
    box-shadow: 0 0 0 2px var(--accent-alpha);
  }

  .join-date {
    color: var(--text-primary);
    font-size: 1rem;
    padding: 0.75rem;
    background-color: var(--bg-tertiary);
    border-radius: 6px;
    display: block;
  }

  @media (max-width: 480px) {
    .profile-content {
      gap: 1.5rem;
    }

    .avatar-container {
      width: 96px;
      height: 96px;
    }
  }
</style>
