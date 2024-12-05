<script lang="ts">
  import { Link } from "svelte-routing";
  import type { ComponentType } from 'svelte';
  import { currentPath } from '../../stores/navigation';
  import { navigate } from "svelte-routing";

  export let icon: ComponentType;
  export let text: string;
  export let path: string;
  export let isExpanded: boolean;

  $: isActive = $currentPath === path;

  function handleClick() {
    currentPath.set(path);
    navigate(path);
  }
</script>

<div class="nav-item-wrapper" class:active={isActive}>
  <button class="nav-button" on:click={handleClick}>
    <div class="nav-item">
      <div class="icon-wrapper">
        <svelte:component this={icon} size={20} />
      </div>
      {#if isExpanded}
        <span class="text" class:fade-in={isExpanded}>{text}</span>
      {/if}
    </div>
  </button>
</div>

<style>
  .nav-item-wrapper {
    margin: 0.125rem 0.75rem;
    border-radius: 8px;
    background-color: transparent;
    transition: all 0.2s ease;
  }

  .nav-button {
    width: 100%;
    background: none;
    border: none;
    padding: 0;
    cursor: pointer;
    text-align: left;
  }

  .nav-item-wrapper:hover {
    background-color: var(--bg-tertiary);
  }

  .nav-item-wrapper.active {
    background-color: var(--accent);
  }

  .nav-item-wrapper.active:hover {
    opacity: 0.9;
  }

  .nav-item {
    display: flex;
    align-items: center;
    gap: 0.875rem;
    padding: 0.875rem 1rem;
    color: var(--text-secondary);
    transition: color 0.2s ease;
  }

  .nav-item-wrapper:hover .nav-item {
    color: var(--text-primary);
  }

  .nav-item-wrapper.active .nav-item {
    color: var(--text-primary);
  }

  .icon-wrapper {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 24px;
    height: 24px;
  }

  .text {
    font-weight: 500;
    font-size: 0.9375rem;
    white-space: nowrap;
    opacity: 0;
    animation: fadeIn 0.3s ease forwards;
  }

  @keyframes fadeIn {
    from {
      opacity: 0;
      transform: translateX(-10px);
    }
    to {
      opacity: 1;
      transform: translateX(0);
    }
  }
</style>