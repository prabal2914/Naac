import React from 'react'
class ThreeThirteen extends React.Component{

  constructor(){
    super();
    this.state={
        name: '',
	org:'',
	duration:'',
	amount:''
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
  fetch('http://127.0.0.1:8000/api/bthreethirteen/',{
      method:'POST',
      body:JSON.stringify(this.state),
      headers:{
          'Content-type': 'application/json; charset=UTF-8',
      },
  })
  .then(response=>response.json())
  .then((data)=>console.log(data));

  this.setState({
    name_awardee:'',
    name: '',
	org:'',
	duration:'',
	amount:''
  });
}

render(){
return (
<div className="relative flex flex-col justify-center min-h-screen overflow-hidden bg-gradient-to-r from-slate-500 to-slate-800">
<div className="w-full p-6 m-auto bg-gradient-to-r from-slate-300 to-slate-500 rounded-md shadow-xl shadow-slate-900 ring-2 ring-slate-600 lg:max-w-6xl">
<div classNmae="inline-block min-w-full py-2 sm:px-6 lg:px-8">
<h1 className="text-3xl font-semibold text-center text-slate-800 underline uppercase decoration-bold mb-5">
Part B Criteria 3 Table 3.5.1
</h1>
<h3 className="text-xl mb-3 bg-gradient-to-r from-slate-100 to-slate-300 rounded-md shadow-xl shadow-slate-900 ring-2 ring-slate-600">Revenue generated from consultancy and corporate training during the last five years</h3>
<table classNmae="min-w- text-left text-sm font-light ">
<thead classNmae="border-b font-medium dark:border-neutral-500">
<tr>
<th scope="col" classNmae="px-6 py-4">
<input type="text" placeholder="Name of faculty consultant" className="input-lg" value={this.state.name} name="name" onChange={this.changeHandler}/>
</th>
<th scope="col" classNmae="px-6 py-4">
<input type="text" placeholder="Organization name" className="input-lg" value={this.state.org} name="org" onChange={this.changeHandler}/>
</th>
<th scope="col" classNmae="px-6 py-4">
<input type="text" placeholder="Duration of Consultancy" className="input-lg" value={this.state.duration} name="duration" onChange={this.changeHandler}/>
</th>
</tr> 

<tr>
<th scope="col" classNmae="px-6 py-4">
<input type="text" placeholder="Amount Generated" className="input-lg" value={this.state.amount} name="amount" onChange={this.changeHandler}/>
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
export default ThreeThirteen