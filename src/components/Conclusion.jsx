import React from 'react'

const Conclusion = () => {
  return (
    <div className="relative flex flex-col justify-center min-h-screen overflow-hidden bg-gradient-to-r from-slate-500 to-slate-800">
        <div className="w-full p-6 m-auto bg-gradient-to-r from-slate-300 to-slate-500 rounded-md shadow-xl shadow-slate-900 ring-2 ring-slate-600 lg:max-w-xl">
        <h1 className="text-3xl font-semibold text-center text-slate-800 underline uppercase decoration-bold">
               CONCLUSION
            </h1>
            <h1 className="text-xl font-semibold text-left text-slate-800 underline uppercase decoration-bold">
               Additional Information
            </h1>
            <textarea placeholder="Additional Information" className="textarea textarea-bordered textarea-lg w-full max-w-lg" ></textarea>

            <h1 className="text-xl font-semibold text-left text-slate-800 underline uppercase decoration-bold">
               Concluding Remarks
            </h1>
            <textarea placeholder="Concluding Remarks" className="textarea textarea-bordered textarea-lg w-full max-w-lg" ></textarea>
      </div>
    </div>
  )
}

export default Conclusion
