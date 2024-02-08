import React from 'react'
class CriteriaTwoEight extends React.Component{

  constructor(){
    super();
    this.state={
        type:'',
	address:'',
	loc:'',
	area:'',
	built_area:'',
	prog:'',
	date_est:'',
	date_rec:'',
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
  fetch('http://127.0.0.1:8000/api/atwoEight/',{
      method:'POST',
      body:JSON.stringify(this.state),
      headers:{
          'Content-type': 'application/json; charset=UTF-8',
      },
  })
  .then(response=>response.json())
  .then((data)=>console.log(data));

  this.setState({
    type:'',
	address:'',
	loc:'',
	area:'',
	built_area:'',
	prog:'',
	date_est:'',
	date_rec:'',
  });
}

render(){
  return (
    <div className="relative flex flex-col justify-center min-h-screen overflow-hidden bg-gradient-to-r from-slate-500 to-slate-800">
    <div className="w-full p-6 m-auto bg-gradient-to-r from-slate-300 to-slate-500 rounded-md shadow-xl shadow-slate-900 ring-2 ring-slate-600 lg:max-w-5xl">
    <div className="inline-block min-w-full py-2 sm:px-6 lg:px-8">
      <div className="overflow-hidden">
        <table className="min-w- text-left text-sm font-light ">
          <thead className="border-b font-medium dark:border-neutral-500">
              <h1 className="text-3xl w-full font-semibold text-left text-slate-800 uppercase decoration-bold ">University with Potential for Excellence</h1>
          </thead>
          <tbody>
            <tr
              className="border-b transition duration-300 ease-in-out hover:bg-neutral-100 dark:border-neutral-500 dark:hover:bg-neutral-600">
              <td className="whitespace-nowrap px-6 py-4 w-1/3 uppercase font-medium text-slate-800 font-semibold decoration-bold">Is the University Recognised as a University with
Potential for Excellence (UPE) by the UGC?</td>
              <td className="whitespace-nowrap px-6 py-4 w-2/3 max-w-4xl font-medium">
              <input type="text" placeholder="Type here" className="input-md w-2/3 max-w-4xl" value={this.state.UPE} name="UPE" onChange={this.changeHandler}/>
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
)
}
}
export default CriteriaTwoEight