<script lang="ts">
  import { mockPlayerReport } from '../data/mockData';
  
  const { recentGames, statistics } = mockPlayerReport;
</script>

<div class="stats-container">
  <div class="card overview">
    <h2 class="section-title">Player Report</h2>
    <div class="stats-summary">
      <div class="stat-item">
        <span class="label">Total Games</span>
        <span class="value">{statistics.totalGames}</span>
      </div>
      <div class="stat-item">
        <span class="label">Win Rate</span>
        <span class="value">{(statistics.winRate * 100).toFixed(1)}%</span>
      </div>
      <div class="stat-item">
        <span class="label">Town Games</span>
        <span class="value">{statistics.townGames}</span>
      </div>
      <div class="stat-item">
        <span class="label">Mafia Games</span>
        <span class="value">{statistics.mafiaGames}</span>
      </div>
      <div class="stat-item">
        <span class="label">Neutral Games</span>
        <span class="value">{statistics.neutralGames}</span>
      </div>
    </div>
  </div>

  <div class="card recent-games">
    <h3>Recent Games</h3>
    <div class="games-list">
      {#each recentGames as game}
        <div class="game-item" class:win={game.result === 'Win'} class:loss={game.result === 'Loss'}>
          <div class="game-info">
            <span class="role">{game.role}</span>
            <span class="alignment">{game.alignment}</span>
          </div>
          <div class="game-result">
            <span class="date">{game.date}</span>
            <span class="result">{game.result}</span>
          </div>
        </div>
      {/each}
    </div>
  </div>
</div>

<style>
  .stats-container {
    display: grid;
    gap: 1.5rem;
  }

  .stats-summary {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
    gap: 1rem;
    margin-top: 1rem;
  }

  .stat-item {
    background-color: var(--bg-tertiary);
    padding: 1rem;
    border-radius: 8px;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
  }

  .label {
    color: var(--text-secondary);
    font-size: 0.875rem;
    margin-bottom: 0.5rem;
  }

  .value {
    font-size: 1.5rem;
    font-weight: 600;
    font-family: 'Poppins', sans-serif;
  }

  .games-list {
    margin-top: 1rem;
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
  }

  .game-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.75rem;
    background-color: var(--bg-tertiary);
    border-radius: 6px;
    border-left: 4px solid transparent;
  }

  .game-item.win {
    border-left-color: var(--success);
  }

  .game-item.loss {
    border-left-color: var(--danger);
  }

  .game-info {
    display: flex;
    gap: 1rem;
    align-items: center;
  }

  .role {
    font-weight: 500;
  }

  .alignment {
    color: var(--text-secondary);
    font-size: 0.875rem;
  }

  .game-result {
    display: flex;
    gap: 1rem;
    align-items: center;
  }

  .date {
    color: var(--text-secondary);
    font-size: 0.875rem;
  }

  .result {
    font-weight: 500;
  }

  .win .result {
    color: var(--success);
  }

  .loss .result {
    color: var(--danger);
  }
</style>