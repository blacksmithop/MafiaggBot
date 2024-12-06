<script lang="ts">
  import TimerSettings from './sections/settings/TimerSettings.svelte';
  import MechanicsSettings from './sections/settings/MechanicsSettings.svelte';
  
  export let roomSettings = {
    timer: {
      dayLength: 3,
      nightLength: 9,
      scaleTimer: false,
      gameStart: 'off',
      disableVoteLock: false
    },
    mechanics: {
      revealRoles: 'allReveal',
      forceVote: false,
      majorityVote: -1,
      mafiaKillPower: 0,
      deadlockPrevention: -1,
      hostRoleSelection: false,
      hideSetup: false,
      preventNightDiscussion: false,
      mafiaLosesAfter: 0,
      townLosesAfter: 20
    }
  };

  export let onChange: (settings: any) => void;
</script>

<div class="room-settings">
  <TimerSettings settings={roomSettings.timer} />
  <MechanicsSettings settings={roomSettings.mechanics} />
</div>

<style>
  .room-settings {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
  }
</style>