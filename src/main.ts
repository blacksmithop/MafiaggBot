import './app.css'
import App from './App.svelte'
import { navigate } from 'svelte-routing'

// Set up router base
let app = new App({
  target: document.getElementById('app')!,
  props: {
    url: window.location.pathname
  }
})

// Handle internal navigation
window.addEventListener('click', (event) => {
  const target = event.target as HTMLElement
  const anchor = target.closest('a')
  
  if (anchor && anchor.href && anchor.href.startsWith(window.location.origin) && !anchor.hasAttribute('target')) {
    event.preventDefault()
    const path = anchor.href.slice(window.location.origin.length)
    navigate(path)
  }
})

export default app