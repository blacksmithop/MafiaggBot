import { writable } from 'svelte/store';
import type { Chat } from '../types/Chat';

export const chatOpen = writable(false);
export const selectedChat = writable<Chat | null>(null);