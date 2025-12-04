import React, { useState, useEffect } from 'react';
import { postsApi } from '../../api/postsApi';

function Posts() {
  const [posts, setPosts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchPosts = async () => {
      try {
        const data = await postsApi.list();
        setPosts(data);
      } catch (err) {
        setError('Ошибка загрузки постов');
      } finally {
        setLoading(false);
      }
    };
    fetchPosts();
  }, []);

  const handleLike = async (id) => {
    try {
      await postsApi.like(id);
      // Refresh posts
      const data = await postsApi.list();
      setPosts(data);
    } catch (err) {
      setError('Ошибка лайка');
    }
  };

  if (loading) return <div>Загрузка...</div>;
  if (error) return <div className="alert alert-error">{error}</div>;

  return (
    <div data-easytag="id8-src/components/Posts/index.jsx" className="container mx-auto p-4">
      <h1 className="text-2xl mb-4">Лента постов</h1>
      <div className="space-y-4">
        {posts.map(post => (
          <div key={post.id} className="card bg-base-100 shadow-xl">
            <div className="card-body">
              <h2 className="card-title">{post.author.first_name} {post.author.last_name}</h2>
              <p>{post.text}</p>
              <div className="card-actions justify-between">
                <button onClick={() => handleLike(post.id)} className="btn btn-sm btn-ghost">
                  👍 {post.likes_count}
                </button>
                <details>
                  <summary>Комментарии ({post.comments_count})</summary>
                  <div className="mt-2 space-y-2">
                    {/* Comment list would go here */}
                  </div>
                </details>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Posts;
