<script lang="ts">
  import type { Deck } from '../../types/Deck';
  import deckData from '../../data/decks.json';
  
  export let value: string;
  export let onChange: (value: string) => void;
  
  const decks: Deck[] = deckData.decks;

  function getImageUrl(url: string): string {
    return url.replace('mafiagg.com', 'mafia.gg');
  }
</script>

<div class="deck-select">
  <select 
    bind:value 
    on:change={(e) => onChange(e.currentTarget.value)}
    class="select-input"
  >
    <option value="">Select a deck</option>
    {#each decks as deck (deck.key)}
      <option value={deck.key}>
        {deck.name} ({deck.deckSize} characters)
      </option>
    {/each}
  </select>
  
  {#if value}
    {#each decks as deck}
      {#if deck.key === value}
        <div class="deck-preview">
          <div class="sample-characters">
            {#each deck.sampleCharacters.slice(0, 3) as character}
              <div 
                class="character-avatar"
                style:background-color={character.backgroundColor}
              >
                <img 
                  src={getImageUrl(character.avatarUrl)} 
                  alt={character.name}
                  class="avatar-image"
                />
                <span class="character-name">{character.name}</span>
              </div>
            {/each}
          </div>
          <div class="deck-info">
            <span class="deck-name">{deck.name}</span>
            <span class="deck-size">{deck.deckSize} characters</span>
          </div>
        </div>
      {/if}
    {/each}
  {/if}
</div>

<style>
  .deck-select {
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }

  .select-input {
    width: 100%;
    padding: 0.75rem;
    background-color: var(--bg-tertiary);
    border: 1px solid var(--bg-tertiary);
    color: var(--text-primary);
    border-radius: 6px;
    transition: all 0.2s ease;
  }

  .select-input:focus {
    outline: none;
    border-color: var(--accent);
  }

  .deck-preview {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    padding: 1rem;
    background-color: var(--bg-tertiary);
    border-radius: 8px;
  }

  .sample-characters {
    display: flex;
    gap: 1rem;
    flex-wrap: wrap;
  }

  .character-avatar {
    position: relative;
    width: 64px;
    height: 64px;
    border-radius: 8px;
    overflow: hidden;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: transform 0.2s ease;
  }

  .character-avatar:hover {
    transform: translateY(-2px);
  }

  .avatar-image {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }

  .character-name {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    padding: 4px;
    background-color: rgba(0, 0, 0, 0.7);
    color: white;
    font-size: 0.75rem;
    text-align: center;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }

  .deck-info {
    display: flex;
    flex-direction: column;
    gap: 0.25rem;
  }

  .deck-name {
    font-weight: 600;
    color: var(--text-primary);
  }

  .deck-size {
    font-size: 0.875rem;
    color: var(--text-secondary);
  }
</style>