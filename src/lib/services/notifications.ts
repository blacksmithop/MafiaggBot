import { fetchWithAuth } from './api';
import { API_ENDPOINTS } from './config';
import type { Notification } from '../types/Notification';

export async function getNotifications(params: {
  page?: number;
  limit?: number;
  type?: string;
}) {
  const queryParams = new URLSearchParams();
  Object.entries(params).forEach(([key, value]) => {
    if (value) queryParams.append(key, value.toString());
  });

  return fetchWithAuth<Notification[]>(
    `${API_ENDPOINTS.notifications}?${queryParams.toString()}`
  );
}

export async function markAsRead(notificationId: string) {
  return fetchWithAuth(`${API_ENDPOINTS.notifications}/${notificationId}/read`, {
    method: 'POST'
  });
}

export async function markAllAsRead() {
  return fetchWithAuth(`${API_ENDPOINTS.notifications}/read-all`, {
    method: 'POST'
  });
}