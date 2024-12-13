export interface LoginCredentials {
  username: string;
  password: string;
}

export interface LoginResponse {
  userSessionToken: string;
}

export interface ValidationError {
  field: string;
  message: string;
}