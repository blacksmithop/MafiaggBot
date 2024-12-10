<script lang="ts">
  import { MessageCircle, X } from 'lucide-svelte';
  import { chatOpen } from '../../stores/chat';
  
  function toggleChat() {
    chatOpen.update(value => !value);
  }
</script>

<button 
  class="chat-button" 
  on:click={toggleChat}
  class:open={$chatOpen}
>
  {#if $chatOpen}
    <X size={24} />
  {:else}
    <MessageCircle size={24} />
  {/if}
</button>

<style>
  .chat-button {
    position: fixed;
    right: 2rem;
    bottom: calc(var(--header-height) + 1rem);
    width: 48px;
    height: 48px;
    border-radius: 50%;
    background-color: var(--accent);
    color: white;
    border: none;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.2s ease;
    z-index: 90;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
  }

  .chat-button:hover {
    transform: scale(1.05);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
  }

  .chat-button.open {
    background-color: var(--bg-secondary);
    color: var(--text-primary);
  }
</style>