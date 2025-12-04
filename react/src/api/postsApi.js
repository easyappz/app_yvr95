import { instance } from './axios';

export const postsApi = {
  list: async (params = {}) => {
    const response = await instance.get('/api/posts/', { params });
    return response.data;
  },

  create: async (data) => {
    const response = await instance.post('/api/posts/', data);
    return response.data;
  },

  retrieve: async (id) => {
    const response = await instance.get(`/api/posts/${id}/`);
    return response.data;
  },

  update: async (id, data) => {
    const response = await instance.put(`/api/posts/${id}/`, data);
    return response.data;
  },

  delete: async (id) => {
    const response = await instance.delete(`/api/posts/${id}/`);
    return response.data;
  },

  like: async (id) => {
    const response = await instance.post(`/api/posts/${id}/like/`);
    return response.data;
  },

  unlike: async (id) => {
    const response = await instance.delete(`/api/posts/${id}/like/`);
    return response.data;
  }
};