<script lang="ts">
  let isDeleting = false;
  let showConfirmDialog = false;

  function handleDeleteRequest() {
    showConfirmDialog = true;
  }

  function confirmDelete() {
    isDeleting = true;
    showConfirmDialog = false;
    // Simulated deletion process
    setTimeout(() => {
      isDeleting = false;
    }, 2000);
  }

  function cancelDelete() {
    showConfirmDialog = false;
  }
</script>

<div class="privacy-container">
  <div class="card">
    <h2 class="section-title">Privacy Policy</h2>
    
    <div class="content">
      <p>At Mafia.gg Stats, we take your privacy seriously. Here's what you need to know about our data practices:</p>
      
      <ul>
        <li>We only store game outcomes and statistical data</li>
        <li>No chat logs or personal communications are stored</li>
        <li>Game data is used solely for statistical analysis</li>
        <li>You can request complete deletion of your data at any time</li>
      </ul>

      <div class="data-deletion">
        <h3>Data Deletion</h3>
        {#if isDeleting}
          <p class="status">Data deletion in progress...</p>
        {:else}
          <button class="delete-btn" on:click={handleDeleteRequest}>
            Delete My Data
          </button>
        {/if}
      </div>
    </div>
  </div>
</div>

{#if showConfirmDialog}
  <div class="modal-overlay">
    <div class="modal">
      <h3>Confirm Data Deletion</h3>
      <p>Are you sure you want to delete all your data? This action cannot be undone.</p>
      <div class="modal-actions">
        <button class="cancel-btn" on:click={cancelDelete}>Cancel</button>
        <button class="confirm-btn" on:click={confirmDelete}>Confirm Delete</button>
      </div>
    </div>
  </div>
{/if}

<style>
  .privacy-container {
    max-width: 800px;
    margin: 0 auto;
  }

  .content {
    color: var(--text-secondary);
    line-height: 1.6;
  }

  .content p {
    margin-bottom: 1.5rem;
  }

  .content ul {
    margin-bottom: 2rem;
    padding-left: 1.5rem;
  }

  .content li {
    margin-bottom: 0.5rem;
  }

  .data-deletion {
    margin-top: 2rem;
    padding-top: 2rem;
    border-top: 1px solid var(--bg-tertiary);
  }

  .data-deletion h3 {
    color: var(--text-primary);
    margin-bottom: 1rem;
  }

  .delete-btn {
    background-color: var(--danger);
    color: white;
    border: none;
    padding: 0.75rem 1.5rem;
    border-radius: 6px;
    cursor: pointer;
    font-weight: 500;
    transition: opacity 0.2s;
  }

  .delete-btn:hover {
    opacity: 0.9;
  }

  .status {
    color: var(--accent);
    font-weight: 500;
  }

  .modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 1000;
  }

  .modal {
    background-color: var(--bg-secondary);
    padding: 2rem;
    border-radius: 12px;
    width: 90%;
    max-width: 400px;
  }

  .modal h3 {
    color: var(--text-primary);
    margin-bottom: 1rem;
  }

  .modal p {
    color: var(--text-secondary);
    margin-bottom: 1.5rem;
  }

  .modal-actions {
    display: flex;
    gap: 1rem;
    justify-content: flex-end;
  }

  .cancel-btn {
    background-color: var(--bg-tertiary);
    color: var(--text-primary);
    border: none;
    padding: 0.75rem 1.5rem;
    border-radius: 6px;
    cursor: pointer;
    transition: background-color 0.2s;
  }

  .confirm-btn {
    background-color: var(--danger);
    color: white;
    border: none;
    padding: 0.75rem 1.5rem;
    border-radius: 6px;
    cursor: pointer;
    transition: opacity 0.2s;
  }

  .cancel-btn:hover {
    background-color: var(--bg-primary);
  }

  .confirm-btn:hover {
    opacity: 0.9;
  }
</style>