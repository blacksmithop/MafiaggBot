<script>
  import { onMount } from "svelte";

  let username = "";
  let password = "";
  let isAuthenticated = false;

  function login() {
    // Dummy login logic
    if (username && password) {
      isAuthenticated = true;
      localStorage.setItem("isAuthenticated", "true");
      location.reload();
    } else {
      alert("Please enter valid credentials.");
    }
  }

  onMount(() => {
    if (localStorage.getItem("isAuthenticated") === "true") {
      isAuthenticated = true;
    }
  });
</script>

<style>
  .login-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100vh;
    background-color: var(--bg-color, #f9f9f9);
  }
  .login-form {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    padding: 2rem;
    border: 1px solid #ccc;
    border-radius: 8px;
    background: white;
  }
  .login-form input {
    padding: 0.5rem;
    font-size: 1rem;
  }
  .login-form button {
    padding: 0.5rem;
    font-size: 1rem;
    cursor: pointer;
  }
</style>

{#if !isAuthenticated}
  <div class="login-container">
    <form class="login-form" on:submit|preventDefault={login}>
      <h2>Login</h2>
      <input type="text" placeholder="Username" bind:value={username} required />
      <input type="password" placeholder="Password" bind:value={password} required />
      <button type="submit">Login</button>
    </form>
  </div>
{/if}
