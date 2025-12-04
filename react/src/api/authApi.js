import { instance } from './axios';

export const authApi = {
  register: async (data) => {
    const response = await instance.post('/api/auth/register/', data);
    return response.data;
  },

  login: async (data) => {
    const response = await instance.post('/api/auth/login/', data);
    return response.data;
  },

  logout: async () => {
    const response = await instance.post('/api/auth/logout/');
    return response.data;
  },

  getProfile: async () => {
    const response = await instance.get('/api/profile/me/');
    return response.data;
  },

  updateProfile: async (data) => {
    const response = await instance.patch('/api/profile/me/', data);
    return response.data;
  }
};