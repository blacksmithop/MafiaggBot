<script lang="ts">
  import { onMount } from 'svelte';
  import { mockFactionStats, mockRoleStats } from '../data/mockData';
  import TrendChart from './TrendChart.svelte';

  // Mock historical data
  const generateHistoricalData = (days: number, baseValue: number) => {
    const data = [];
    const now = new Date();
    for (let i = days; i >= 0; i--) {
      data.push({
        date: new Date(now.getTime() - i * 24 * 60 * 60 * 1000),
        value: baseValue + Math.random() * 10 - 5
      });
    }
    return data;
  };

  const townTrend = generateHistoricalData(30, 52);
  const mafiaTrend = generateHistoricalData(30, 42);
  const neutralTrend = generateHistoricalData(30, 6);
</script>

<div class="stats-layout">
  <div class="card overview-stats">
    <h2 class="section-title">Overview</h2>
    <div class="stats-grid">
      <div class="stat-card town">
        <h3>Town</h3>
        <div class="value">{mockFactionStats[0].winRate * 100}%</div>
        <div class="label">Win Rate</div>
      </div>
      <div class="stat-card mafia">
        <h3>Mafia</h3>
        <div class="value">{mockFactionStats[1].winRate * 100}%</div>
        <div class="label">Win Rate</div>
      </div>
      <div class="stat-card neutral">
        <h3>Neutral</h3>
        <div class="value">{mockFactionStats[2].winRate * 100}%</div>
        <div class="label">Win Rate</div>
      </div>
    </div>
  </div>

  <div class="card">
    <h2 class="section-title">Win Rate Trends</h2>
    <div class="trends-grid">
      <TrendChart title="Town Win Rate" data={townTrend} color="var(--success)" />
      <TrendChart title="Mafia Win Rate" data={mafiaTrend} color="var(--danger)" />
      <TrendChart title="Neutral Win Rate" data={neutralTrend} color="var(--neutral)" />
    </div>
  </div>
</div>

<style>
  .stats-layout {
    display: grid;
    gap: 2rem;
  }

  .overview-stats {
    background-color: var(--bg-secondary);
  }

  .stats-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1.5rem;
  }

  .stat-card {
    padding: 1.5rem;
    border-radius: 8px;
    text-align: center;
    background-color: var(--bg-tertiary);
  }

  .stat-card h3 {
    font-size: 1.2rem;
    margin-bottom: 0.5rem;
  }

  .stat-card .value {
    font-size: 2.5rem;
    font-weight: 700;
    font-family: 'Poppins', sans-serif;
    margin: 0.5rem 0;
  }

  .stat-card .label {
    color: var(--text-secondary);
    font-size: 0.9rem;
  }

  .town { border-left: 4px solid var(--success); }
  .mafia { border-left: 4px solid var(--danger); }
  .neutral { border-left: 4px solid var(--neutral); }

  .trends-grid {
    display: grid;
    gap: 2rem;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  }

  @media (max-width: 768px) {
    .stats-grid {
      grid-template-columns: 1fr;
    }
  }
</style>