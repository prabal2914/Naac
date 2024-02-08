import React from 'react'

const Choose = () => {
  return (
    <div className="relative flex flex-col justify-center min-h-screen overflow-hidden bg-gradient-to-r from-slate-500 to-slate-800">
        <div className="w-full p-6 m-auto bg-gradient-to-r from-slate-300 to-slate-500 rounded-md shadow-xl shadow-slate-900 ring-2 ring-slate-600 lg:max-w-xl">
            <h1 className="text-3xl font-semibold text-center text-slate-800 underline uppercase decoration-bold">
               CHOOSE AQAR/SSR
            </h1>
            <form className="mt-6">
                < div className='mb-2'>
                <label
                        for="password"
                        className="block text-sm font-semibold text-gray-800"
                    >
                        Annual Quality Assurance Report
                    </label>
                <div className="mt-6">
                    <button className="w-full px-4 py-2 tracking-wide text-white transition-colors duration-200 transform bg-emerald-700 rounded-md-emerald-900 rounded-md hover:bg-emerald-500 focus:outline-none focus:bg-emerald-900">
                        Proceed to AQAR
                    </button>
                </div>
                </div>
                <div className='mb-2 mt-6'>
                <label
                        for="password"
                        className="block text-sm font-semibold text-gray-800"
                    >
                        Self Study Report
                    </label>
                <div className="mt-6">
                    <button className="w-full px-4 py-2 tracking-wide text-white transition-colors duration-200 transform bg-emerald-700 rounded-md-emerald-900 rounded-md hover:bg-emerald-500 focus:outline-none focus:bg-emerald-900">
                        Proceed to SSR
                    </button>
                </div>
                </div>
            </form>
        </div>
    </div>
  )
}

export default Choose
