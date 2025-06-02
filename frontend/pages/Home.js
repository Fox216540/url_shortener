// pages/Home.js
import React, { useState } from 'react';
import { Link } from 'react-router-dom';

const Home = () => {
  const [url, setUrl] = useState('');
  const [shortUrl, setShortUrl] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!url) {
      setError('Please enter a URL');
      return;
    }

    setLoading(true);
    // Simulate API call
    setTimeout(() => {
      setShortUrl(`https://short.ly/${Math.random().toString(36).substring(7)}`);
      setLoading(false);
      setError('');
    }, 1000);
  };

  return (
    <div className="max-w-2xl mx-auto">
      <div className="bg-white p-8 rounded-xl shadow-md">
        <h1 className="text-3xl font-bold text-center mb-6">Shorten Your URL</h1>

        <form onSubmit={handleSubmit} className="mb-6">
          <div className="flex flex-col sm:flex-row gap-3">
            <input
              type="url"
              value={url}
              onChange={(e) => setUrl(e.target.value)}
              placeholder="https://example.com"
              className="flex-grow px-4 py-3 border rounded-lg focus:ring-2 focus:ring-indigo-500 focus:outline-none"
            />
            <button
              type="submit"
              disabled={loading}
              className="px-6 py-3 bg-indigo-600 text-white font-medium rounded-lg hover:bg-indigo-700 transition disabled:opacity-50"
            >
              {loading ? 'Shortening...' : 'Shorten'}
            </button>
          </div>
          {error && <p className="mt-2 text-red-500 text-sm">{error}</p>}
        </form>

        {shortUrl && (
          <div className="border border-green-200 bg-green-50 rounded-lg p-4">
            <div className="flex flex-col sm:flex-row justify-between items-center gap-3">
              <div className="flex-grow">
                <a
                  href={shortUrl}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-indigo-600 hover:underline break-all"
                >
                  {shortUrl}
                </a>
              </div>
              <Link
                to="/chat/123"
                className="px-4 py-2 bg-emerald-500 text-white rounded-lg hover:bg-emerald-600 transition"
              >
                Discuss
              </Link>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default Home;