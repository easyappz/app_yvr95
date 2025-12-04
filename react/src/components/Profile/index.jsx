import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { authApi } from '../../api/authApi';

function Profile() {
  const navigate = useNavigate();
  const [userData, setUserData] = useState(null);
  const [formData, setFormData] = useState({
    firstName: '',
    lastName: '',
    about: ''
  });
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchData = async () => {
      try {
        const data = await authApi.getProfile();
        setUserData(data);
        setFormData({
          firstName: data.first_name,
          lastName: data.last_name,
          about: data.about || ''
        });
      } catch (err) {
        setError('Ошибка загрузки профиля');
      }
    };
    fetchData();
  }, []);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await authApi.updateProfile(formData);
      setUserData({ ...userData, ...formData });
    } catch (err) {
      setError('Ошибка обновления профиля');
    }
  };

  if (!userData) return <div>Загрузка...</div>;

  return (
    <div data-easytag="id7-src/components/Profile/index.jsx" className="container mx-auto p-4">
      <h1 className="text-2xl mb-4">Профиль</h1>
      {error && <div className="alert alert-error">{error}</div>}
      <form onSubmit={handleSubmit} className="space-y-4">
        <div>
          <label className="block">Имя</label>
          <input 
            type="text" 
            name="firstName" 
            value={formData.firstName}
            onChange={handleChange}
            className="input input-bordered w-full" 
            required
          />
        </div>
        <div>
          <label className="block">Фамилия</label>
          <input 
            type="text" 
            name="lastName" 
            value={formData.lastName}
            onChange={handleChange}
            className="input input-bordered w-full" 
            required
          />
        </div>
        <div>
          <label className="block">О себе</label>
          <textarea 
            name="about" 
            value={formData.about}
            onChange={handleChange}
            className="textarea textarea-bordered w-full" 
          />
        </div>
        <button type="submit" className="btn btn-primary">Сохранить</button>
      </form>
    </div>
  );
}

export default Profile;
