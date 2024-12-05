import { writable } from 'svelte/store';

export const currentPath = writable<string>(window.location.pathname);

export function updateCurrentPath(path: string) {
  currentPath.set(path);
}