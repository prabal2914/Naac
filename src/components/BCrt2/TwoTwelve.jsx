import React from 'react'
class TwoTwelve extends React.Component{

  constructor(){
    super();
    this.state={
       choice: ''

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
  fetch('http://127.0.0.1:8000/api/btwotwelve/',{
      method:'POST',
      body:JSON.stringify(this.state),
      headers:{
          'Content-type': 'application/json; charset=UTF-8',
      },
  })
  .then(response=>response.json())
  .then((data)=>console.log(data));

  this.setState({
    choice: ''
  });
}

render(){
return (
<div>
<div className="relative flex flex-col justify-center min-h-screen overflow-hidden bg-gradient-to-r from-slate-500 to-slate-800">
<div className="w-full p-6 m-auto bg-gradient-to-r from-slate-300 to-slate-500 rounded-md shadow-xl shadow-slate-900 ring-2 ring-slate-600 lg:max-w-6xl">
<div classNmae="inline-block min-w-full py-2 sm:px-6 lg:px-8">
<h1 className="text-3xl font-semibold text-center text-slate-800 underline uppercase decoration-bold mb-5">
Part B Criteria 2 Table 2.5.3
</h1>
<h3 className="text-3xl mb-10 bg-gradient-to-r from-slate-100 to-slate-300 rounded-md shadow-xl shadow-slate-900 ring-2 ring-slate-600">Status of automation of Examination division along with approved Examination Manual/ordinance</h3>
<h3 className="text-3xl mb-10 bg-gradient-to-r from-slate-100 to-slate-300 rounded-md shadow-xl shadow-slate-900 ring-2 ring-slate-600">A.100% automation of entire division & implementation of Examination Management  System (EMS)</h3>
<h3 className="text-3xl mb-10 bg-gradient-to-r from-slate-100 to-slate-300 rounded-md shadow-xl shadow-slate-900 ring-2 ring-slate-600">B.Only student registration, Hall ticket issue & Result Processing</h3>
<h3 className="text-3xl mb-10 bg-gradient-to-r from-slate-100 to-slate-300 rounded-md shadow-xl shadow-slate-900 ring-2 ring-slate-600">C.Only student registration and result processing</h3>
<h3 className="text-3xl mb-10 bg-gradient-to-r from-slate-100 to-slate-300 rounded-md shadow-xl shadow-slate-900 ring-2 ring-slate-600">D.Only result processing</h3>
<h3 className="text-3xl mb-10 bg-gradient-to-r from-slate-100 to-slate-300 rounded-md shadow-xl shadow-slate-900 ring-2 ring-slate-600">E.Only manual methodology </h3>

<div classNmae="overflow-hidden">
<table classNmae="min-w- text-left text-sm font-light ">
<thead classNmae="border-b font-medium dark:border-neutral-500">
<tr>
<th scope="col" classNmae="px-6 py-4">
<select className="select-lg select-bordered w-full " value={this.state.choice} name="choice" onChange={this.changeHandler}>
<option disabled selected>Qualification</option>
<option>A</option>
<option>B</option>
<option>C</option>
<option>D</option>
</select>
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
</div>
</div>
)
}
}

export default TwoTwelve
