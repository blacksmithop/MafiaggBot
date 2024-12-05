<script lang="ts">
  import { Plus, Minus } from 'lucide-svelte';
  import type { Role } from '../../types/Role';
  import roleData from '../../data/roles.json';

  export let selectedRoles: { [key: string]: number } = {};
  export let onChange: (roles: { [key: string]: number }) => void;

  const roles: Role[] = roleData.roles;
  const alignments = ['town', 'mafia', 'third'];
  let activeAlignment = 'town';

  const alignmentColors = {
    town: '#4180DB',    // Mafia.gg town blue
    mafia: '#C94A4A',   // Mafia.gg mafia red
    third: '#B85DE6'    // Mafia.gg third purple
  };

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

  $: alignmentColor = alignmentColors[activeAlignment];
</script>

<div class="role-selector">
  <div class="alignment-tabs">
    {#each alignments as alignment}
      <button
        class="tab-btn"
        class:active={activeAlignment === alignment}
        style="--alignment-color: {alignmentColors[alignment]}"
        on:click={() => activeAlignment = alignment}
      >
        {alignment.charAt(0).toUpperCase() + alignment.slice(1)}
      </button>
    {/each}
  </div>

  <div class="roles-content">
    <div class="roles-list">
      {#each getRolesByAlignment(activeAlignment) as role}
        <div 
          class="role-item"
          style="--role-color: {alignmentColor}"
        >
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
</div>

<style>
  .role-selector {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    height: 100%;
    max-height: 500px;
  }

  .alignment-tabs {
    display: flex;
    gap: 0.5rem;
    padding: 0.5rem;
    background-color: var(--bg-tertiary);
    border-radius: 8px;
  }

  .tab-btn {
    flex: 1;
    padding: 0.75rem 1rem;
    border: none;
    background: none;
    color: var(--text-secondary);
    font-weight: 500;
    cursor: pointer;
    border-radius: 6px;
    transition: all 0.2s ease;
    border: 2px solid transparent;
  }

  .tab-btn:hover {
    color: var(--alignment-color);
    background-color: var(--bg-secondary);
  }

  .tab-btn.active {
    color: var(--alignment-color);
    background-color: var(--bg-secondary);
    border-color: var(--alignment-color);
  }

  .roles-content {
    flex: 1;
    overflow-y: auto;
  }

  .roles-list {
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
    padding: 0.5rem;
  }

  .role-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.75rem;
    background-color: var(--bg-tertiary);
    border-radius: 6px;
    border-left: 3px solid var(--role-color);
    transition: all 0.2s ease;
  }

  .role-item:hover {
    transform: translateX(4px);
    background-color: color-mix(in srgb, var(--role-color) 10%, var(--bg-tertiary));
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
    background-color: var(--role-color);
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