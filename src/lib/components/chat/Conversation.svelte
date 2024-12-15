<script lang="ts">
  import { ArrowLeft, Send, Smile } from "lucide-svelte";
  import { selectedChat } from "../../stores/chat";
  import type { Chat, Message } from "../../types/Chat";
  import { loadChatMessages } from "../../services";
  import { onMount } from "svelte";
    import { login } from "../../services/auth";

  export let chat: Chat;

  let messages: Message[] = [];
  let messageInput = "";
  let messagesContainer: HTMLDivElement;
  const user_id = Number(localStorage.getItem("user_id"));

  // Load messages when a chat is selected
  async function loadMessages() {
    if (chat.senderId && user_id) {
      messages = await loadChatMessages(user_id, chat.senderId);
    }

    // Scroll to bottom after loading messages
    setTimeout(() => {
      if (messagesContainer) {
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
      }
    });
  }

  onMount(() => {
    loadMessages();
  });

  function sendMessage() {
    if (!messageInput.trim()) return;

    const newMessage: Message = {
      id: Date.now().toString(),
      sender: user_id, // Set sender as user_id
      content: messageInput,
      timestamp: new Date(),
      type: "text",
    };

    messages = [...messages, newMessage];
    messageInput = "";

    // Scroll to bottom after sending a message
    setTimeout(() => {
      if (messagesContainer) {
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
      }
    });
  }

  function handleKeyDown(event: KeyboardEvent) {
    if (event.key === "Enter" && !event.shiftKey) {
      event.preventDefault();
      sendMessage();
    }
  }
</script>

<div class="conversation">
  <div class="header">
    <button class="back-btn" on:click={() => selectedChat.set(null)}>
      <ArrowLeft size={20} />
    </button>
    <div class="user-info">
      <img
        src={`https://api.dicebear.com/7.x/avataaars/svg?seed=${chat.senderId}`}
        alt={chat.senderId}
        class="avatar"
      />
      <span class="username">{chat.senderId}</span>
    </div>
  </div>

  <div class="messages" bind:this={messagesContainer}>
    {#each messages as message}
      <div class="message" class:sent={message.sender === user_id}>
        <div class="message-content">
          <!-- class:emoji={message.type === "emoji"} -->
          {message.content}
        </div>
        <span class="time">
          {new Date(message.timestamp).toLocaleTimeString([], {
            hour: "2-digit",
            minute: "2-digit",
          })}
        </span>
      </div>
    {/each}
  </div>

  <div class="input-area">
    <button class="emoji-btn">
      <Smile size={20} />
    </button>
    <textarea
      placeholder="Type a message..."
      bind:value={messageInput}
      on:keydown={handleKeyDown}
      rows="1"
    />
    <button
      class="send-btn"
      on:click={sendMessage}
      disabled={!messageInput.trim()}
    >
      <Send size={20} />
    </button>
  </div>
</div>

<style>
  .conversation {
    height: 100%;
    display: flex;
    flex-direction: column;
  }

  .header {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    padding: 0.75rem;
    border-bottom: 1px solid var(--bg-tertiary);
  }

  .back-btn {
    background: none;
    border: none;
    color: var(--text-secondary);
    cursor: pointer;
    padding: 0.5rem;
    border-radius: 6px;
    transition: all 0.2s ease;
  }

  .back-btn:hover {
    background-color: var(--bg-tertiary);
    color: var(--text-primary);
  }

  .user-info {
    display: flex;
    align-items: center;
    gap: 0.75rem;
  }

  .avatar {
    width: 32px;
    height: 32px;
    border-radius: 50%;
  }

  .username {
    font-weight: 500;
  }

  .messages {
    flex: 1;
    overflow-y: auto;
    padding: 1rem;
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
  }

  .message {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    max-width: 80%;
  }

  .message.sent {
    align-self: flex-end;
    align-items: flex-end;
  }

  .message-content {
    background-color: var(--bg-tertiary);
    padding: 0.75rem;
    border-radius: 12px;
    border-bottom-left-radius: 4px;
    color: var(--text-primary);
  }

  .message.sent .message-content {
    background-color: var(--accent);
    color: white;
    border-bottom-left-radius: 12px;
    border-bottom-right-radius: 4px;
  }

  .message-content.emoji {
    font-size: 1.5rem;
    padding: 0.5rem;
  }

  .time {
    font-size: 0.75rem;
    color: var(--text-secondary);
    margin-top: 0.25rem;
  }

  .input-area {
    padding: 0.75rem;
    border-top: 1px solid var(--bg-tertiary);
    display: flex;
    align-items: flex-end;
    gap: 0.75rem;
  }

  .emoji-btn,
  .send-btn {
    background: none;
    border: none;
    color: var(--text-secondary);
    cursor: pointer;
    padding: 0.5rem;
    border-radius: 6px;
    transition: all 0.2s ease;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .emoji-btn:hover,
  .send-btn:hover:not(:disabled) {
    background-color: var(--bg-tertiary);
    color: var(--text-primary);
  }

  .send-btn:disabled {
    opacity: 0.5;
    cursor: not-allowed;
  }

  textarea {
    flex: 1;
    background-color: var(--bg-tertiary);
    border: none;
    border-radius: 6px;
    padding: 0.75rem;
    resize: none;
    color: var(--text-primary);
    font-family: inherit;
    line-height: 1.4;
    max-height: 120px;
  }

  textarea:focus {
    outline: none;
  }
</style>