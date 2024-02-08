import React from 'react'
import HeroImage from "../assets/NAAC.png"

const Hero = () => {
  return (
    <div>
    <div className="hero min-h-screen bg-gradient-to-r from-slate-500 to-slate-600 ">
  <div className="hero-content flex-col lg:flex-row">
    <img src={HeroImage} className="max-w-sm rounded-lg shadow-2xl" />
    <div>
      <h1 className="text-5xl mt-5 font-bold">Check Your NAAC Score Now !</h1>
      <p className="py-6 mt-3">Enter the values in our system , we will thoroughly analyse the inputs and check for any potential mistakes in the entries and after carefully checking we will display whether the college will 
      get the NAAC accredition or not, using AI to calculate the expected marks which can be achieved by the given inputs according to the given trends of the marking system.</p>
      <button class="bg-emerald-500 hover:bg-emerald-700 text-white font-bold py-2 px-4 border border-emerald-700 rounded">
  Get Started
</button>
    </div>
  </div>
</div>
    </div>
  )
}

export default Hero
