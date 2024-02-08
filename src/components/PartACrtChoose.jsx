import React from 'react'

const PartACrtChoose = () => {
  return (
    <div>
      <div className="relative flex flex-col justify-center min-h-screen overflow-hidden bg-gradient-to-r from-slate-500 to-slate-800">
        <div className="w-full p-6 m-auto bg-gradient-to-r from-slate-300 to-slate-500 rounded-md shadow-xl shadow-slate-900 ring-2 ring-slate-600 lg:max-w-xl">
            <h1 className="text-3xl font-semibold text-center text-slate-800 underline uppercase decoration-bold">
               CHOOSE Criteria From Part A to Fill Up
            </h1>
            <form className="mt-6">
                < div className='mb-2'>
                <div className="mt-6">
                    <button className="w-full px-4 py-2 tracking-wide text-white transition-colors duration-200 transform bg-emerald-700 rounded-md-emerald-900 rounded-md hover:bg-emerald-500 focus:outline-none focus:bg-emerald-900">
                        Criteria 1
                    </button>
                </div>
                </div>
                <div className='mb-2 mt-6'>
                <div className="mt-6">
                    <button className="w-full px-4 py-2 tracking-wide text-white transition-colors duration-200 transform bg-emerald-700 rounded-md-emerald-900 rounded-md hover:bg-emerald-500 focus:outline-none focus:bg-emerald-900">
                        Criteria 2
                    </button>
                </div>
                </div>
                <div className='mb-2 mt-6'>
                <div className="mt-6">
                    <button className="w-full px-4 py-2 tracking-wide text-white transition-colors duration-200 transform bg-emerald-700 rounded-md-emerald-900 rounded-md hover:bg-emerald-500 focus:outline-none focus:bg-emerald-900">
                        Criteria 3
                    </button>
                </div>
                </div>
                <div className='mb-2 mt-6'>
                <div className="mt-6">
                    <button className="w-full px-4 py-2 tracking-wide text-white transition-colors duration-200 transform bg-emerald-700 rounded-md-emerald-900 rounded-md hover:bg-emerald-500 focus:outline-none focus:bg-emerald-900">
                        Criteria 4
                    </button>
                </div>
                </div> 
                <div className='mb-2 mt-6'>
                <div className="mt-6">
                    <button className="w-full px-4 py-2 tracking-wide text-white transition-colors duration-200 transform bg-emerald-700 rounded-md-emerald-900 rounded-md hover:bg-emerald-500 focus:outline-none focus:bg-emerald-900">
                        Back
                    </button>
                </div>
                </div>
            </form>
        </div>
    </div>
    </div>
  )
}

export default PartACrtChoose
