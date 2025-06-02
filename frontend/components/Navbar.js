// components/Navbar.js
import React from 'react';
import { Link, NavLink } from 'react-router-dom';

const Navbar = () => {
  const isLoggedIn = false; // Authentication state would go here

  return (
    <nav className="bg-white shadow-md">
      <div className="container mx-auto px-4">
        <div className="flex justify-between items-center h-16">
          <Link to="/" className="text-2xl font-bold text-indigo-600">Short.ly</Link>

          <div className="flex space-x-4">
            {isLoggedIn ? (
              <>
                <NavLink to="/dashboard" className="px-3 py-2 rounded-md text-gray-700 hover:bg-gray-100">Dashboard</NavLink>
                <button className="px-3 py-2 rounded-md text-gray-700 hover:bg-gray-100">Logout</button>
              </>
            ) : (
              <>
                <NavLink to="/login" className="px-3 py-2 rounded-md text-gray-700 hover:bg-gray-100">Login</NavLink>
                <NavLink to="/register" className="px-3 py-2 rounded-md bg-indigo-600 text-white hover:bg-indigo-700">Register</NavLink>
              </>
            )}
          </div>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;