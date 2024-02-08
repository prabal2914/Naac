import React from 'react'
class FiveSix extends React.Component{

  constructor(){
    super();
    this.state={
      year:'',
      sl_no:'',
      higher_placed:'',
      org:'',
      details:''
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
  fetch('http://127.0.0.1:8000/api/bfivesix/',{
      method:'POST',
      body:JSON.stringify(this.state),
      headers:{
          'Content-type': 'application/json; charset=UTF-8',
      },
  })
  .then(response=>response.json())
  .then((data)=>console.log(data));

  this.setState({
    year:'',
    sl_no:'',
    higher_placed:'',
    org:'',
    details:''
  });
}

render(){
  return (
    <div className="relative flex flex-col justify-center min-h-screen overflow-hidden bg-gradient-to-r from-slate-500 to-slate-800">
    <div className="w-full p-6 m-auto bg-gradient-to-r from-slate-300 to-slate-500 rounded-md shadow-xl shadow-slate-900 ring-2 ring-slate-600 lg:max-w-6xl">
<div classNmae="inline-block min-w-full py-2 sm:px-6 lg:px-8">
<h1 className="text-3xl font-semibold text-center text-slate-800 underline uppercase decoration-bold mb-5">
         Part B Criteria 5 Table 5.2.2
      </h1>
<h3 className="text-xl mb-3 bg-gradient-to-r from-slate-100 to-slate-300 rounded-md shadow-xl  shadow-slate-900 ring-2 ring-slate-600">Percentage of recently graduated students who have progressed to higher education (previous graduating batch).</h3>
<table classNmae="min-w- text-left text-sm font-light ">
  <thead classNmae="border-b font-medium dark:border-neutral-500">
  <tr>
      <th scope="col" classNmae="px-6 py-4">
      <h3 className="text-sm">Enter the year for which the data is being filled <br /> (Make sure to enter data for five distinct years).
        </h3>
      </th>
      <th scope="col" classNmae="px-6 py-4">
      <input type="text" placeholder="Year" className="input-lg" value={this.state.year} name="year" onChange={this.changeHandler}/>
      </th>
    </tr> 
    <tr>
    <th scope="col" classNmae="px-6 py-4">
      <input type="text" placeholder="Sl No." className="input-lg" value={this.state.sl_no} name="sl_no" onChange={this.changeHandler}/>
      </th>
      <th scope="col" classNmae="px-6 py-4">
      <h3 className="text-sm">Name of student enrolling into higher education
        </h3>
      </th>
      <th scope="col" classNmae="px-6 py-4">
      <input type="text" placeholder="Enter Name here" className="input-lg" value={this.state.higher_placed} name="higher_placed" onChange={this.changeHandler}/>
      </th>
    </tr> 
    <tr>
      <th scope="col" classNmae="px-6 py-4">
      <input type="text" placeholder="Name of institution admitted to" className="input-lg" value={this.state.org} name="org" onChange={this.changeHandler}/>
      </th>
      <th scope="col" classNmae="px-6 py-4">
      <input type="text" placeholder="Details of the program enrolled" className="input-lg" value={this.state.details} name="details" onChange={this.changeHandler}/>
      </th>
    </tr> 
  </thead>
</table>
< div className='mb-2'>
        <div className="mt-5">
        <button onClick={this.submitForm} className="w-1/2 px-4 py-2 tracking-wide text-white transition-colors duration-200 transform bg-emerald-700 rounded-md-emerald-900 rounded-md hover:bg-emerald-500 focus:outline-none focus:bg-emerald-900">
                ADD MORE
            </button>
            <button onClick={this.submitForm} className="w-1/2 px-4 py-2 tracking-wide text-white transition-colors duration-200 transform bg-emerald-700 rounded-md-emerald-900 rounded-md hover:bg-emerald-500 focus:outline-none focus:bg-emerald-900">
                DONE
            </button>
        </div>
        </div>

  </div>
</div>
</div>
  )
}
}
export default FiveSix
