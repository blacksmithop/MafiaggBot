<script lang="ts">
  import { onMount } from 'svelte';
  import Chart from 'chart.js/auto';
  import { format } from 'date-fns';

  export let title: string;
  export let data: { date: Date; value: number }[];
  export let color: string = '#4CAF50';
  
  let canvas: HTMLCanvasElement;

  onMount(() => {
    new Chart(canvas, {
      type: 'line',
      data: {
        labels: data.map(d => format(d.date, 'MMM d')),
        datasets: [{
          label: title,
          data: data.map(d => d.value),
          borderColor: color,
          backgroundColor: `${color}33`,
          fill: true,
          tension: 0.4
        }]
      },
      options: {
        responsive: true,
        plugins: {
          title: {
            display: true,
            text: title,
            color: '#ffffff',
            font: {
              family: 'Poppins',
              size: 16,
              weight: '600'
            }
          },
          legend: {
            display: false
          }
        },
        scales: {
          y: {
            beginAtZero: true,
            grid: {
              color: '#2c2a31'
            },
            ticks: {
              color: '#8b8a8e'
            }
          },
          x: {
            grid: {
              color: '#2c2a31'
            },
            ticks: {
              color: '#8b8a8e'
            }
          }
        }
      }
    });
  });
</script>

<canvas bind:this={canvas}></canvas>