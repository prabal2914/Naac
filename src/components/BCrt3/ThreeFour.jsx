import React from 'react'
class ThreeFour extends React.Component{

  constructor(){
    super();
    this.state={
      name:'',
	grant:'',
	agency:'',
	year:'',
	period:''
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
  fetch('http://127.0.0.1:8000/api/bthreefour/',{
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
    grant:'',
    agency:'',
    year:'',
    period:''
  });
}

render(){
return (
<div className="relative flex flex-col justify-center min-h-screen overflow-hidden bg-gradient-to-r from-slate-500 to-slate-800">
<div className="w-full p-6 m-auto bg-gradient-to-r from-slate-300 to-slate-500 rounded-md shadow-xl shadow-slate-900 ring-2 ring-slate-600 lg:max-w-6xl">
<div classNmae="inline-block min-w-full py-2 sm:px-6 lg:px-8">
<h1 className="text-3xl font-semibold text-center text-slate-800 underline uppercase decoration-bold mb-5">
Part B Criteria 3 Table 3.1.4
</h1>
<h3 className="text-xl mb-3 bg-gradient-to-r from-slate-100 to-slate-300 rounded-md shadow-xl shadow-slate-900 ring-2 ring-slate-600"> Number of JRFs, SRFs, Post Doctoral Fellows, Research Associates and other research fellows enrolled in the institution during the last five years.</h3>

<table classNmae="min-w- text-left text-sm font-light ">
<thead classNmae="border-b font-medium dark:border-neutral-500">
<tr>
<th scope="col" classNmae="px-6 py-4">
<input type="text" placeholder="Name of the scholar" className="input-lg" value={this.state.name} name="name" onChange={this.changeHandler}/>
</th>
<th scope="col" classNmae="px-6 py-4">
<input type="text" placeholder="Specify the grants" className="input-lg" value={this.state.grant} name="grant" onChange={this.changeHandler}/>
</th>
<th scope="col" classNmae="px-6 py-4">
<input type="text" placeholder="Awarding Agency" className="input-lg" value={this.state.agency} name="agency" onChange={this.changeHandler}/>
</th>
</tr>
<tr>
<th scope="col" classNmae="px-6 py-4">
<input type="text" placeholder="Year of award" className="input-lg" value={this.state.year} name="year" onChange={this.changeHandler}/>
</th>
<th scope="col" classNmae="px-6 py-4">
<input type="text" placeholder="Period of award" className="input-lg" value={this.state.period} name="period" onChange={this.changeHandler}/>
</th>
</tr>
</thead>
</table>
< div className='mb-2'>
<div className="mt-5">
<button className="w-1/2 px-4 py-2 tracking-wide text-white transition-colors duration-200 transform bg-emerald-700 rounded-md-emerald-900 rounded-md hover:bg-emerald-500 focus:outline-none focus:bg-emerald-900">
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

export default ThreeFour