<script lang="ts">
  import { fade, slide } from 'svelte/transition';
  import { chatOpen, selectedChat } from '../../stores/chat';
  import ChatList from './ChatList.svelte';
  import Conversation from './Conversation.svelte';
</script>

{#if $chatOpen}
  <div class="chat-window" transition:slide={{ duration: 300 }}>
    {#if $selectedChat}
      <Conversation chat={$selectedChat} />
    {:else}
      <ChatList />
    {/if}
  </div>
{/if}

<style>
  .chat-window {
    position: fixed;
    right: 2rem;
    bottom: calc(var(--header-height) + 4rem);
    width: 320px;
    height: 480px;
    background-color: var(--bg-secondary);
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
    overflow: hidden;
    z-index: 89;
  }

  @media (max-width: 640px) {
    .chat-window {
      right: 1rem;
      bottom: calc(var(--header-height) + 4rem);
      width: calc(100% - 2rem);
      height: 400px;
    }
  }
</style>