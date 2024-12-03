<script lang="ts">
  import { Plus, Minus } from 'lucide-svelte';
  import type { Role } from '../../types/Role';
  import roleData from '../../data/roles.json';

  export let selectedRoles: { [key: string]: number } = {};
  export let onChange: (roles: { [key: string]: number }) => void;

  const roles: Role[] = roleData.roles;
  const alignments = ['town', 'mafia', 'neutral'];

  function getRolesByAlignment(alignment: string) {
    return roles.filter(role => role.alignment === alignment);
  }

  function updateRoleCount(roleId: number, increment: boolean) {
    const newCount = (selectedRoles[roleId] || 0) + (increment ? 1 : -1);
    if (newCount >= 0) {
      const updatedRoles = {
        ...selectedRoles,
        [roleId]: newCount
      };
      if (newCount === 0) {
        delete updatedRoles[roleId];
      }
      onChange(updatedRoles);
    }
  }
</script>

<div class="role-selector">
  {#each alignments as alignment}
    <div class="alignment-section">
      <h3 class="alignment-title">{alignment.charAt(0).toUpperCase() + alignment.slice(1)}</h3>
      <div class="roles-list">
        {#each getRolesByAlignment(alignment) as role}
          <div class="role-item">
            <div class="role-info">
              <span class="role-name">{role.name}</span>
              <div class="role-tags">
                {#each role.tags as tag}
                  <span class="tag">{tag}</span>
                {/each}
              </div>
            </div>
            <div class="role-controls">
              <button 
                class="control-btn"
                on:click={() => updateRoleCount(role.id, false)}
                disabled={!selectedRoles[role.id]}
              >
                <Minus size={16} />
              </button>
              <span class="count">{selectedRoles[role.id] || 0}</span>
              <button 
                class="control-btn"
                on:click={() => updateRoleCount(role.id, true)}
              >
                <Plus size={16} />
              </button>
            </div>
          </div>
        {/each}
      </div>
    </div>
  {/each}
</div>

<style>
  .role-selector {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
    max-height: 400px;
    overflow-y: auto;
  }

  .alignment-section {
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }

  .alignment-title {
    font-size: 1.125rem;
    font-weight: 600;
    color: var(--text-primary);
    padding-bottom: 0.5rem;
    border-bottom: 1px solid var(--bg-tertiary);
  }

  .roles-list {
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
  }

  .role-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.75rem;
    background-color: var(--bg-tertiary);
    border-radius: 6px;
  }

  .role-info {
    display: flex;
    flex-direction: column;
    gap: 0.25rem;
  }

  .role-name {
    font-weight: 500;
    color: var(--text-primary);
  }

  .role-tags {
    display: flex;
    gap: 0.5rem;
  }

  .tag {
    font-size: 0.75rem;
    padding: 0.125rem 0.375rem;
    background-color: var(--bg-secondary);
    color: var(--text-secondary);
    border-radius: 999px;
  }

  .role-controls {
    display: flex;
    align-items: center;
    gap: 0.5rem;
  }

  .control-btn {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 24px;
    height: 24px;
    border: none;
    background-color: var(--bg-secondary);
    color: var(--text-secondary);
    border-radius: 4px;
    cursor: pointer;
    transition: all 0.2s ease;
  }

  .control-btn:hover:not(:disabled) {
    background-color: var(--accent);
    color: white;
  }

  .control-btn:disabled {
    opacity: 0.5;
    cursor: not-allowed;
  }

  .count {
    min-width: 24px;
    text-align: center;
    font-weight: 500;
  }
</style>