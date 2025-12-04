import { instance } from './axios';

export const postsApi = {
  // List all posts
  list: async (params = {}) => {
    const response = await instance.get('/api/posts/', { params });
    return response.data;
  },

  // Create new post
  create: async (data) => {
    const response = await instance.post('/api/posts/', data);
    return response.data;
  },

  // Retrieve single post
  retrieve: async (id) => {
    const response = await instance.get(`/api/posts/${id}/`);
    return response.data;
  },

  // Update post
  update: async (id, data) => {
    const response = await instance.put(`/api/posts/${id}/`, data);
    return response.data;
  },

  // Delete post
  delete: async (id) => {
    const response = await instance.delete(`/api/posts/${id}/`);
    return response.data;
  },

  // Like post
  like: async (id) => {
    const response = await instance.post(`/api/posts/${id}/like/`);
    return response.data;
  },

  // Remove like from post
  unlike: async (id) => {
    const response = await instance.delete(`/api/posts/${id}/like/`);
    return response.data;
  }
};