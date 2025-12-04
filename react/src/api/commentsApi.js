import { instance } from './axios';

export const commentsApi = {
  // List comments for a post
  list: async (postId) => {
    const response = await instance.get(`/api/posts/${postId}/comments/`);
    return response.data;
  },

  // Create comment
  create: async (postId, data) => {
    const response = await instance.post(`/api/posts/${postId}/comments/`, data);
    return response.data;
  },

  // Retrieve comment
  retrieve: async (id) => {
    const response = await instance.get(`/api/comments/${id}/`);
    return response.data;
  },

  // Update comment
  update: async (id, data) => {
    const response = await instance.put(`/api/comments/${id}/`, data);
    return response.data;
  },

  // Delete comment
  delete: async (id) => {
    const response = await instance.delete(`/api/comments/${id}/`);
    return response.data;
  }
};