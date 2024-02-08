import React from 'react'
class CriteriaTwoOne extends React.Component{

  constructor(){
    super();
    this.state={
      name:'',
	address:'',
	city:'',
	state:'',
	pin:'',
	website:'',
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
  fetch('http://127.0.0.1:8000/api/atwoone/',{
      method:'POST',
      body:JSON.stringify(this.state),
      headers:{
          'Content-type': 'application/json; charset=UTF-8',
      },
  })
  .then(response=>response.json())
  .then((data)=>console.log(data));

  this.setState({
    name:'',
	address:'',
	city:'',
	state:'',
	pin:'',
	website:'',
  });
}

render(){
  return (
    <div className="m-4">
      <div className=" relative flex flex-col justify-center m-4 min-h-screen overflow-hidden bg-gradient-to-r from-slate-500 to-slate-800">
            <div className="w-full p-6 m-auto bg-gradient-to-r from-slate-300 to-slate-500 rounded-md shadow-xl shadow-slate-900 ring-2 ring-slate-600 lg:max-w-5xl">
    <div className="inline-block min-w-full py-2 sm:px-6 lg:px-8">
      <div className="overflow-hidden">
      <h1 className="text-3xl  font-semibold text-center text-slate-800 underline uppercase decoration-bold">
               2.1 BASIC INFORMATION
            </h1>
        <table className="min-w- text-left m-4 text-sm font-light ">
          <thead className="border-b font-medium dark:border-neutral-500">
              <h1 className="text-3xl w-full font-semibold text-left text-slate-800 uppercase decoration-bold ">Name and Address of the University</h1>
          </thead>
          <tbody>
            <tr
              className="border-b transition duration-300 ease-in-out hover:bg-neutral-100 dark:border-neutral-500 dark:hover:bg-neutral-600">
              <td className="whitespace-nowrap px-6 py-4 w-1/3 uppercase font-medium text-slate-800 font-semibold decoration-bold">Name</td>
              <td className="whitespace-nowrap px-6 py-4 w-2/3 max-w-4xl font-medium">
              <input type="text" placeholder="Type here" className="input-md w-2/3 max-w-4xl" value={this.state.name} name="name" onChange={this.changeHandler}/>
              </td> 
            </tr>

            <tr
              className="border-b transition duration-300 ease-in-out hover:bg-neutral-100 dark:border-neutral-500 dark:hover:bg-neutral-600">
              <td className="whitespace-nowrap px-6 py-4 w-1/3 uppercase font-medium text-slate-800 font-semibold decoration-bold">Address</td>
              <td className="whitespace-nowrap px-6 py-4 w-2/3 max-w-4xl font-medium">
              <input type="text" placeholder="Type here" className="input-md w-2/3 max-w-4xl" value={this.state.address} name="address" onChange={this.changeHandler}/>
              </td> 
            </tr>

            <tr
              className="border-b transition duration-300 ease-in-out hover:bg-neutral-100 dark:border-neutral-500 dark:hover:bg-neutral-600">
              <td className="whitespace-nowrap px-6 py-4 w-1/3 uppercase font-medium text-slate-800 font-semibold decoration-bold">City</td>
              <td className="whitespace-nowrap px-6 py-4 w-2/3 max-w-4xl font-medium">
              <input type="text" placeholder="Type here" className="input-md w-2/3 max-w-4xl" value={this.state.city} name="city" onChange={this.changeHandler}/>
              </td> 
            </tr>

            <tr
              className="border-b transition duration-300 ease-in-out hover:bg-neutral-100 dark:border-neutral-500 dark:hover:bg-neutral-600">
              <td className="whitespace-nowrap px-6 py-4 w-1/3 uppercase font-medium text-slate-800 font-semibold decoration-bold">State</td>
              <td className="whitespace-nowrap px-6 py-4 w-2/3 max-w-4xl font-medium">
              <input type="text" placeholder="Type here" className="input-md w-2/3 max-w-4xl" value={this.state.state} name="state" onChange={this.changeHandler}/>
              </td> 
            </tr>

            <tr
              className="border-b transition duration-300 ease-in-out hover:bg-neutral-100 dark:border-neutral-500 dark:hover:bg-neutral-600">
              <td className="whitespace-nowrap px-6 py-4 w-1/3 uppercase font-medium text-slate-800 font-semibold decoration-bold">Pin</td>
              <td className="whitespace-nowrap px-6 py-4 w-2/3 max-w-4xl font-medium">
              <input type="text" placeholder="Type here" className="input-md w-2/3 max-w-4xl" value={this.state.pin} name="pin" onChange={this.changeHandler}/>
              </td> 
            </tr>

            <tr
              className="border-b transition duration-300 ease-in-out hover:bg-neutral-100 dark:border-neutral-500 dark:hover:bg-neutral-600">
              <td className="whitespace-nowrap px-6 py-4 w-1/3 uppercase font-medium text-slate-800 font-semibold decoration-bold">Website</td>
              <td className="whitespace-nowrap px-6 py-4 w-2/3 max-w-4xl font-medium">
              <input type="text" placeholder="Type here" className="input-md w-2/3 max-w-4xl " value={this.state.website} name="website" onChange={this.changeHandler}/>
              </td> 
            </tr>
           
          </tbody>
          <div class="flex w-1/2 ">
          <button onClick={this.submitForm} className="w-1/2 px-4 py-2 m-4 tracking-wide text-white transition-colors duration-200 transform bg-emerald-700 rounded-md-emerald-900 rounded-md hover:bg-emerald-500 focus:outline-none focus:bg-emerald-900">
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
</div>
  
)
}
}
export default CriteriaTwoOne