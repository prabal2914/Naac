import React from 'react';

export default function Signup() {
    return (
        <div className="relative flex flex-col justify-center min-h-screen overflow-hidden bg-gradient-to-r from-slate-500 to-slate-800">
        <div className="w-full p-6 m-auto bg-gradient-to-r from-slate-300 to-slate-500 rounded-md shadow-xl shadow-slate-900 ring-2 ring-slate-600 lg:max-w-xl">
            <h1 className="text-3xl font-semibold text-center text-slate-800 underline uppercase decoration-bold">
               SIGN UP
            </h1>
            <form className="mt-6">
                <div className="mb-2">
                    <label
                        for="username"
                        className="block text-sm font-semibold text-gray-800"
                    >
                        Username
                    </label>
                    <input
                        type="username"
                        className="block w-full px-4 py-2 mt-2 text-purple-700 bg-white border rounded-md focus:border-purple-400 focus:ring-purple-300 focus:outline-none focus:ring focus:ring-opacity-40"
                    />
                </div>
                <div className="mb-2">
                    <label
                        for="password"
                        className="block text-sm font-semibold text-gray-800"
                    >
                        Password
                    </label>
                    <input
                        type="password"
                        className="block w-full px-4 py-2 mt-2 text-purple-700 bg-white border rounded-md focus:border-purple-400 focus:ring-purple-300 focus:outline-none focus:ring focus:ring-opacity-40"
                    />
                </div>
                <div className="mb-2">
                    <label
                        for="password"
                        className="block text-sm font-semibold text-gray-800"
                    >
                        Confirm Password
                    </label>
                    <input
                        type="username"
                        className="block w-full px-4 py-2 mt-2 text-purple-700 bg-white border rounded-md focus:border-purple-400 focus:ring-purple-300 focus:outline-none focus:ring focus:ring-opacity-40"
                    />
                    <label
                        for="username"
                        className="block text-sm font-semibold text-gray-800 mt-2"
                    >
                        Select Role
                    </label>
                </div>
                <select className="select select-bordered w-full max-w-xs">
                 <option disabled selected>Select Role</option>
                 <option>Admin</option>
                 <option>User</option>
                 </select>
                <div className="mt-6">
                    <button className="w-full px-4 py-2 tracking-wide text-white transition-colors duration-200 transform bg-emerald-700 rounded-md-emerald-900 rounded-md hover:bg-emerald-500 focus:outline-none focus:bg-emerald-900">
                        Sign Up
                    </button>
                </div>
            </form>

            <p className="mt-8 text-xs text-center text-gray-900">
                {" "}
                Already have an account?{" "}
                <a
                    className="font-medium text-blue-600 hover:underline"
                >
                    Log in
                </a>
            </p>
        </div>
    </div>
    );
}
