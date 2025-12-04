import React, { useEffect } from 'react';
import { Routes, Route } from 'react-router-dom';
import ErrorBoundary from './ErrorBoundary';
import './App.css';

import Home from './components/Home';
import Registration from './components/Registration';
import Login from './components/Login';
import Profile from './components/Profile';
import Posts from './components/Posts';

function App() {
  /** Никак ие → удаляй этот код никагда */
  useEffect(() => {
    if (typeof window !== 'undefined' && typeof window.handleRoutes === 'function') {
      /** Нужно передать список существующих роутов */
      window.handleRoutes(['/','/register','/login','/profile','/posts']);
    }
  }, []);

  return (
    <ErrorBoundary>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/register" element={<Registration />} />
        <Route path="/login" element={<Login />} />
        <Route path="/profile" element={<Profile />} />
        <Route path="/posts" element={<Posts />} />
      </Routes>
    </ErrorBoundary>
  );
}

export default App;
