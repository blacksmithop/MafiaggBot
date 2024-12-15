<script lang="ts">
  import { onMount } from "svelte";
  import { navigate } from "svelte-routing";
  import { AlertCircle } from 'lucide-svelte';
  import { login } from '../services/auth';
  import { loginSchema, type LoginFormData } from '../validation/auth';
  import type { ValidationError } from '../types/Auth';

  let username = "";
  let password = "";
  let isLoading = false;
  let errors: ValidationError[] = [];
  let generalError = "";

  onMount(() => {
    if (localStorage.getItem("isAuthenticated") === "true") {
      navigate("/");
    }
  });

  async function handleLogin() {
    try {
      errors = [];
      generalError = "";
      isLoading = true;

      // Validate form data
      const formData: LoginFormData = { username, password };
      const validationResult = loginSchema.safeParse(formData);

      if (!validationResult.success) {
        errors = validationResult.error.errors.map(err => ({
          field: err.path[0].toString(),
          message: err.message
        }));
        return;
      }

      // Attempt login
      await login(username, password);
      
      // Redirect to dashboard
      navigate("/");
    } catch (error) {
      generalError = error instanceof Error ? error.message : "Login failed";
    } finally {
      isLoading = false;
    }
  }

  function getFieldError(field: string): string {
    const error = errors.find(err => err.field === field);
    return error ? error.message : '';
  }
</script>

<div class="login-container">
  <div class="login-card">
    <div class="logo-section">
      <img src="/mafia-icon.svg" alt="Mafia.gg Logo" class="logo" />
      <h1>Welcome Back</h1>
      <p>Sign in to access your Mafia.gg stats</p>
    </div>

    <form class="login-form" on:submit|preventDefault={handleLogin}>
      {#if generalError}
        <div class="error-banner">
          <AlertCircle size={20} />
          <span>{generalError}</span>
        </div>
      {/if}

      <div class="form-group">
        <label for="username">Username</label>
        <input
          type="text"
          id="username"
          bind:value={username}
          class:error={getFieldError('username')}
          disabled={isLoading}
          autocomplete="username"
        />
        {#if getFieldError('username')}
          <span class="error-message">{getFieldError('username')}</span>
        {/if}
      </div>

      <div class="form-group">
        <label for="password">Password</label>
        <input
          type="password"
          id="password"
          bind:value={password}
          class:error={getFieldError('password')}
          disabled={isLoading}
          autocomplete="current-password"
        />
        {#if getFieldError('password')}
          <span class="error-message">{getFieldError('password')}</span>
        {/if}
      </div>

      <button type="submit" class="login-btn" disabled={isLoading}>
        {#if isLoading}
          <div class="loader"></div>
          <span>Signing in...</span>
        {:else}
          <span>Sign In</span>
        {/if}
      </button>
    </form>
  </div>
</div>

<style>
  .login-container {
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 1rem;
    background: linear-gradient(135deg, var(--bg-primary) 0%, var(--bg-secondary) 100%);
  }

  .login-card {
    background-color: var(--bg-secondary);
    border-radius: 12px;
    padding: 2rem;
    width: 100%;
    max-width: 400px;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2);
  }

  .logo-section {
    text-align: center;
    margin-bottom: 2rem;
  }

  .logo {
    width: 64px;
    height: 64px;
    margin-bottom: 1rem;
  }

  .logo-section h1 {
    font-size: 1.5rem;
    margin-bottom: 0.5rem;
    color: var(--text-primary);
  }

  .logo-section p {
    color: var(--text-secondary);
    font-size: 0.875rem;
  }

  .login-form {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
  }

  .form-group {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
  }

  label {
    color: var(--text-secondary);
    font-size: 0.875rem;
  }

  input {
    padding: 0.75rem;
    background-color: var(--bg-tertiary);
    border: 1px solid var(--bg-tertiary);
    border-radius: 6px;
    color: var(--text-primary);
    transition: all 0.2s ease;
  }

  input:focus {
    outline: none;
    border-color: var(--accent);
    box-shadow: 0 0 0 2px var(--accent-alpha);
  }

  input.error {
    border-color: var(--danger);
  }

  .error-message {
    color: var(--danger);
    font-size: 0.75rem;
  }

  .error-banner {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.75rem;
    background-color: color-mix(in srgb, var(--danger) 10%, transparent);
    border: 1px solid var(--danger);
    border-radius: 6px;
    color: var(--danger);
    font-size: 0.875rem;
  }

  .login-btn {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
    padding: 0.75rem;
    background-color: var(--accent);
    color: white;
    border: none;
    border-radius: 6px;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.2s ease;
  }

  .login-btn:hover:not(:disabled) {
    opacity: 0.9;
  }

  .login-btn:disabled {
    opacity: 0.7;
    cursor: not-allowed;
  }

  .loader {
    width: 16px;
    height: 16px;
    border: 2px solid white;
    border-top-color: transparent;
    border-radius: 50%;
    animation: spin 0.8s linear infinite;
  }

  @keyframes spin {
    to {
      transform: rotate(360deg);
    }
  }
</style>