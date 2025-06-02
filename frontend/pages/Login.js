// pages/Login.js
import React, { useState } from 'react';
import { Link } from 'react-router-dom';

const Login = () => {
  const [credentials, setCredentials] = useState({
    emailOrUsername: '',
    password: ''
  });
  const [errors, setErrors] = useState({});
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setCredentials({ ...credentials, [name]: value });
  };

  const validate = () => {
    const newErrors = {};
    if (!credentials.emailOrUsername.trim()) newErrors.emailOrUsername = 'Email or username is required';
    if (!credentials.password) newErrors.password = 'Password is required';

    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (validate()) {
      setLoading(true);
      // Simulate login API call
      setTimeout(() => {
        setLoading(false);
        // Redirect to dashboard
      }, 1500);
    }
  };

  return (
    <div className="max-w-md mx-auto bg-white p-8 rounded-xl shadow-md">
      <h2 className="text-2xl font-bold text-center mb-6">Login to Your Account</h2>

      <form onSubmit={handleSubmit} className="space-y-4">
        <div>
          <label className="block text-gray-700 mb-1">Email or Username</label>
          <input
            type="text"
            name="emailOrUsername"
            value={credentials.emailOrUsername}
            onChange={handleChange}
            className={`w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-indigo-500 focus:outline-none ${errors.emailOrUsername ? 'border-red-500' : ''}`}
          />
          {errors.emailOrUsername && <p className="mt-1 text-red-500 text-sm">{errors.emailOrUsername}</p>}
        </div>

        <div>
          <label className="block text-gray-700 mb-1">Password</label>
          <input
            type="password"
            name="password"
            value={credentials.password}
            onChange={handleChange}
            className={`w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-indigo-500 focus:outline-none ${errors.password ? 'border-red-500' : ''}`}
          />
          {errors.password && <p className="mt-1 text-red-500 text-sm">{errors.password}</p>}
        </div>

        <div className="flex items-center justify-between">
          <div className="flex items-center">
            <input
              id="remember-me"
              name="remember-me"
              type="checkbox"
              className="h-4 w-4 text-indigo-600 focus:ring-indigo-500 border-gray-300 rounded"
            />
            <label htmlFor="remember-me" className="ml-2 block text-sm text-gray-700">
              Remember me
            </label>
          </div>

          <div className="text-sm">
            <a href="#" className="text-indigo-600 hover:text-indigo-500">
              Forgot password?
            </a>
          </div>
        </div>

        <button
          type="submit"
          disabled={loading}
          className="w-full py-3 bg-indigo-600 text-white font-medium rounded-lg hover:bg-indigo-700 transition disabled:opacity-50"
        >
          {loading ? 'Logging in...' : 'Login'}
        </button>
      </form>

      <p className="mt-6 text-center text-gray-600">
        Don't have an account?{' '}
        <Link to="/register" className="text-indigo-600 hover:underline">Register here</Link>
      </p>
    </div>
  );
};

export default Login;