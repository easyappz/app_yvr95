import { instance } from './axios';

export const profileApi = {
  // Get current user profile
  getMe: async () => {
    const response = await instance.get('/api/profile/me/');
    return response.data;
  },

  // Update current user profile
  updateMe: async (data) => {
    const response = await instance.patch('/api/profile/me/', data);
    return response.data;
  }
};