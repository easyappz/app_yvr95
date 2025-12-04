import { instance } from './axios';

export const authApi = {
  // Register new user
  register: async (data) => {
    const response = await instance.post('/api/auth/register/', data);
    return response.data;
  },

  // Login user
  login: async (data) => {
    const response = await instance.post('/api/auth/login/', data);
    return response.data;
  },

  // Logout user
  logout: async () => {
    const response = await instance.post('/api/auth/logout/');
    return response.data;
  }
};