// pages/ChatPage.js
import React, { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';

const ChatPage = () => {
  const { linkId } = useParams();
  const [messages, setMessages] = useState([]);
  const [newMessage, setNewMessage] = useState('');
  const [loading, setLoading] = useState(true);
  const [linkInfo, setLinkInfo] = useState(null);

  // Simulate loading chat messages
  useEffect(() => {
    setTimeout(() => {
      setMessages([
        { id: '1', user: 'John Doe', text: 'This link is super helpful! Thanks for sharing', timestamp: '2 hours ago' },
        { id: '2', user: 'You', text: 'Glad you found it useful!', timestamp: '1 hour ago' },
        { id: '3', user: 'Sarah Smith', text: 'Has anyone tried this with mobile apps?', timestamp: '30 minutes ago' },
      ]);
      setLinkInfo({
        shortUrl: 'https://short.ly/abc123',
        longUrl: 'https://example.com/very/long/url/that/needs/shortening'
      });
      setLoading(false);
    }, 1000);
  }, [linkId]);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!newMessage.trim()) return;

    const newMsg = {
      id: Date.now().toString(),
      user: 'You',
      text: newMessage,
      timestamp: 'Just now'
    };

    setMessages([...messages, newMsg]);
    setNewMessage('');
  };

  if (loading) {
    return (
      <div className="max-w-4xl mx-auto">
        <div className="bg-white p-6 rounded-xl shadow-md">
          <div className="flex justify-center py-10">
            <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-indigo-500"></div>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="max-w-4xl mx-auto">
      <div className="bg-white rounded-xl shadow-md overflow-hidden">
        <div className="p-4 bg-indigo-600 text-white">
          <Link to="/dashboard" className="text-indigo-200 hover:text-white inline-flex items-center mb-2">
            <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M10 19l-7-7m0 0l7-7m-7 7h18" />
            </svg>
            Back to Dashboard
          </Link>
          <h2 className="text-xl font-bold">Discussion for Link</h2>
          <a
            href={linkInfo.shortUrl}
            target="_blank"
            rel="noopener noreferrer"
            className="text-indigo-200 hover:text-white text-sm block truncate"
          >
            {linkInfo.longUrl}
          </a>
        </div>

        <div className="p-4 border-b">
          <div className="flex items-center">
            <div className="bg-indigo-100 text-indigo-800 text-xs px-2 py-1 rounded">
              {linkInfo.shortUrl}
            </div>
            <button className="ml-2 text-xs text-indigo-600 hover:text-indigo-800">
              Copy
            </button>
          </div>
        </div>

        <div className="h-96 overflow-y-auto p-4 bg-gray-50">
          {messages.map((message) => (
            <div
              key={message.id}
              className={`mb-4 ${message.user === 'You' ? 'text-right' : ''}`}
            >
              <div className={`inline-block p-3 rounded-lg max-w-xs md:max-w-md ${message.user === 'You' ? 'bg-indigo-100' : 'bg-white border'}`}>
                <div className="font-medium text-gray-900">
                  {message.user}
                </div>
                <p className="mt-1 text-gray-700">
                  {message.text}
                </p>
                <div className="mt-1 text-xs text-gray-500">
                  {message.timestamp}
                </div>
              </div>
            </div>
          ))}
        </div>

        <div className="p-4 border-t">
          <form onSubmit={handleSubmit} className="flex gap-2">
            <input
              type="text"
              value={newMessage}
              onChange={(e) => setNewMessage(e.target.value)}
              placeholder="Type your message..."
              className="flex-grow px-4 py-2 border rounded-lg focus:ring-2 focus:ring-indigo-500 focus:outline-none"
            />
            <button
              type="submit"
              className="px-4 py-2 bg-indigo-600 text-white rounded-lg hover:bg-indigo-700 transition"
            >
              Send
            </button>
          </form>
        </div>
      </div>
    </div>
  );
};

export default ChatPage;