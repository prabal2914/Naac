import React from 'react'
class CriteriaTwoNine extends React.Component{

  constructor(){
    super();
    this.state={
        const:'',
        aff:'',
        clg_2F:'',
        clg_2F_12B:'',
        naac:'',
        ugc:'',
        auto:'',
        postgrd:'',
        clg_res:'',
        uni_res:'',
    }
    this.changeHandler=this.changeHandler.bind(this);
    this.submitForm=this.submitForm.bind(this);
}

// Input Change Handler
changeHandler(event){
    this.setState({
        [event.target.name]:event.target.value
    });
}

submitForm(){
  fetch('http://127.0.0.1:8000/api/atwonine/',{
      method:'POST',
      body:JSON.stringify(this.state),
      headers:{
          'Content-type': 'application/json; charset=UTF-8',
      },
  })
  .then(response=>response.json())
  .then((data)=>console.log(data));

  this.setState({
    const:'',
    aff:'',
    clg_2F:'',
    clg_2F_12B:'',
    naac:'',
    ugc:'',
    auto:'',
    postgrd:'',
    clg_res:'',
    uni_res:'',
  });
}

render(){
  return (
        <div className="relative flex flex-col justify-center min-h-screen overflow-hidden bg-gradient-to-r from-slate-500 to-slate-800">
            <div className="w-full p-6 m-auto bg-gradient-to-r from-slate-300 to-slate-500 rounded-md shadow-xl shadow-slate-900 ring-2 ring-slate-600 lg:max-w-5xl">
    <div className="inline-block min-w-full py-2 sm:px-6 lg:px-8">
      <div className="overflow-hidden">
      <h1 className="text-3xl m-4 font-semibold text-center text-slate-800 underline uppercase decoration-bold">
            2.2 ACADEMIC INFORMATION
        </h1>
        <table className="min-w- text-left text-sm font-light ">
          <thead className="border-b font-medium dark:border-neutral-500">
          
              <h1 className="text-3xl w-full font-semibold text-left text-slate-800 uppercase decoration-bold ">Furnish the Details of Colleges of University</h1>
          </thead>
          <tbody>
            <tr
              className="border-b transition duration-300 ease-in-out hover:bg-neutral-100 dark:border-neutral-500 dark:hover:bg-neutral-600">
              <td className="whitespace-nowrap px-6 py-4 w-1/3 uppercase font-medium text-slate-800 font-bold decoration-bold">Type Of Colleges</td>
              <td className="whitespace-nowrap px-6 py-4 w-1/3 uppercase font-medium text-slate-800 font-bold decoration-bold">Numbers</td>
            </tr>

            <tr
              className="border-b transition duration-300 ease-in-out hover:bg-neutral-100 dark:border-neutral-500 dark:hover:bg-neutral-600">
              <td className="whitespace-nowrap px-6 py-4 w-1/3 uppercase font-medium text-slate-800 font-semibold decoration-bold">Constituent Colleges</td>
              <td className="whitespace-nowrap px-6 py-4 w-2/3 max-w-4xl font-medium">
              <input type="text" placeholder="Type here" className="input-md w-2/3 max-w-4xl" value={this.state.const} name="const" onChange={this.changeHandler} />
              </td> 
            </tr>

            <tr
              className="border-b transition duration-300 ease-in-out hover:bg-neutral-100 dark:border-neutral-500 dark:hover:bg-neutral-600">
              <td className="whitespace-nowrap px-6 py-4 w-1/3 uppercase font-medium text-slate-800 font-semibold decoration-bold">Affiliated Colleges</td>
              <td className="whitespace-nowrap px-6 py-4 w-2/3 max-w-4xl font-medium">
              <input type="text" placeholder="Type here" className="input-md w-2/3 max-w-4xl" value={this.state.aff} name="aff" onChange={this.changeHandler}/>
              </td> 
            </tr>

            <tr
              className="border-b transition duration-300 ease-in-out hover:bg-neutral-100 dark:border-neutral-500 dark:hover:bg-neutral-600">
              <td className="whitespace-nowrap px-6 py-4 w-1/3 uppercase font-medium text-slate-800 font-semibold decoration-bold">Colleges Under 2(f)</td>
              <td className="whitespace-nowrap px-6 py-4 w-2/3 max-w-4xl font-medium">
              <input type="text" placeholder="Type here" className="input-md w-2/3 max-w-4xl" value={this.state.clg_2F} name="clg_2F" onChange={this.changeHandler} />
              </td> 
            </tr>

            <tr
              className="border-b transition duration-300 ease-in-out hover:bg-neutral-100 dark:border-neutral-500 dark:hover:bg-neutral-600">
              <td className="whitespace-nowrap px-6 py-4 w-1/3 uppercase font-medium text-slate-800 font-semibold decoration-bold">Colleges Under 2(f) and 12B</td>
              <td className="whitespace-nowrap px-6 py-4 w-2/3 max-w-4xl font-medium">
              <input type="text" placeholder="Type here" className="input-md w-2/3 max-w-4xl" value={this.state.clg_2F_12B} name="clg_2F_12B" onChange={this.changeHandler}/>
              </td> 
            </tr>

            <tr
              className="border-b transition duration-300 ease-in-out hover:bg-neutral-100 dark:border-neutral-500 dark:hover:bg-neutral-600">
              <td className="whitespace-nowrap px-6 py-4 w-1/3 uppercase font-medium text-slate-800 font-semibold decoration-bold">NAAC Accredited Colleges</td>
              <td className="whitespace-nowrap px-6 py-4 w-2/3 max-w-4xl font-medium">
              <input type="text" placeholder="Type here" className="input-md w-2/3 max-w-4xl " value={this.state.naac} name="naac" onChange={this.changeHandler}/>
              </td> 
            </tr>

            <tr
              className="border-b transition duration-300 ease-in-out hover:bg-neutral-100 dark:border-neutral-500 dark:hover:bg-neutral-600">
              <td className="whitespace-nowrap px-6 py-4 w-1/3 uppercase font-medium text-slate-800 font-semibold decoration-bold">Colleges with Potential for Excellence(UGC)</td>
              <td className="whitespace-nowrap px-6 py-4 w-2/3 max-w-4xl font-medium">
              <input type="text" placeholder="Type here" className="input-md w-2/3 max-w-4xl " value={this.state.ugc} name="ugc" onChange={this.changeHandler}/>
              </td> 
            </tr>

            <tr
              className="border-b transition duration-300 ease-in-out hover:bg-neutral-100 dark:border-neutral-500 dark:hover:bg-neutral-600">
              <td className="whitespace-nowrap px-6 py-4 w-1/3 uppercase font-medium text-slate-800 font-semibold decoration-bold">Autonomous Colleges</td>
              <td className="whitespace-nowrap px-6 py-4 w-2/3 max-w-4xl font-medium">
              <input type="text" placeholder="Type here" className="input-md w-2/3 max-w-4xl " value={this.state.auto} name="auto" onChange={this.changeHandler}/>
              </td> 
            </tr>

            <tr
              className="border-b transition duration-300 ease-in-out hover:bg-neutral-100 dark:border-neutral-500 dark:hover:bg-neutral-600">
              <td className="whitespace-nowrap px-6 py-4 w-1/3 uppercase font-medium text-slate-800 font-semibold decoration-bold">Colleges with Postgraduate Departments</td>
              <td className="whitespace-nowrap px-6 py-4 w-2/3 max-w-4xl font-medium">
              <input type="text" placeholder="Type here" className="input-md w-2/3 max-w-4xl " value={this.state.postgrd} name="postgrd" onChange={this.changeHandler}/>
              </td> 
            </tr>
            
            <tr
              className="border-b transition duration-300 ease-in-out hover:bg-neutral-100 dark:border-neutral-500 dark:hover:bg-neutral-600">
              <td className="whitespace-nowrap px-6 py-4 w-1/3 uppercase font-medium text-slate-800 font-semibold decoration-bold">Colleges with Research Departments</td>
              <td className="whitespace-nowrap px-6 py-4 w-2/3 max-w-4xl font-medium">
              <input type="text" placeholder="Type here" className="input-md w-2/3 max-w-4xl " value={this.state.clg_res} name="clg_res" onChange={this.changeHandler}/>
              </td> 
            </tr>

            <tr
              className="border-b transition duration-300 ease-in-out hover:bg-neutral-100 dark:border-neutral-500 dark:hover:bg-neutral-600">
              <td className="whitespace-nowrap px-6 py-4 w-1/3 uppercase font-medium text-slate-800 font-semibold decoration-bold">University Recognized Research Institutes/Centers</td>
              <td className="whitespace-nowrap px-6 py-4 w-2/3 max-w-4xl font-medium">
              <input type="text" placeholder="Type here" className="input-md w-2/3 max-w-4xl " value={this.state.uni_res} name="uni_res" onChange={this.changeHandler}/>
              </td> 
            </tr>

          </tbody>
          <div class="flex w-1/2 ">
          <button className="w-1/2 px-4 py-2 m-4 tracking-wide text-white transition-colors duration-200 transform bg-emerald-700 rounded-md-emerald-900 rounded-md hover:bg-emerald-500 focus:outline-none focus:bg-emerald-900">
                      Add More
            </button>
            
          <button className="w-1/2 px-4 py-2 m-4 tracking-wide text-white transition-colors duration-200 transform bg-emerald-700 rounded-md-emerald-900 rounded-md hover:bg-emerald-500 focus:outline-none focus:bg-emerald-900">
                      Done 
            </button>

            <button className="w-1/2 px-4 py-2 m-4 tracking-wide text-white transition-colors duration-200 transform bg-emerald-700 rounded-md-emerald-900 rounded-md hover:bg-emerald-500 focus:outline-none focus:bg-emerald-900">
                      Back
            </button>
            </div>
        </table>
      </div>
    </div>
  </div>
</div>

)
}
}
export default CriteriaTwoNine