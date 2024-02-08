import React from 'react'
class TwoEight extends React.Component{

  constructor(){
    super();
    this.state={
      sl_no: '',
      name: '',
      year_join: '',
      qualification: '',
      year_qual: ''
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
  fetch('http://127.0.0.1:8000/api/btwoeight/',{
      method:'POST',
      body:JSON.stringify(this.state),
      headers:{
          'Content-type': 'application/json; charset=UTF-8',
      },
  })
  .then(response=>response.json())
  .then((data)=>console.log(data));

  this.setState({
    sl_no: '',
      name: '',
      year_join: '',
      qualification: '',
      year_qual: ''
  });
}

render(){
return (
<div>
<div className="relative flex flex-col justify-center min-h-screen overflow-hidden bg-gradient-to-r from-slate-500 to-slate-800">
<div className="w-full p-6 m-auto bg-gradient-to-r from-slate-300 to-slate-500 rounded-md shadow-xl shadow-slate-900 ring-2 ring-slate-600 lg:max-w-6xl">
<div classNmae="inline-block min-w-full py-2 sm:px-6 lg:px-8">
<h1 className="text-3xl font-semibold text-center text-slate-800 underline uppercase decoration-bold mb-5">
Part B Criteria 2 Table 2.4.2
</h1>
<h3 className="text-3xl mb-10 bg-gradient-to-r from-slate-100 to-slate-300 rounded-md shadow-xl shadow-slate-900 ring-2 ring-slate-600"> Average percentage of full time teachers with Ph.D./D.M/M.Ch./D.N.B Superspeciality/D.Sc./D.Lit. during the last five years</h3>
<div classNmae="overflow-hidden">
<table classNmae="min-w- text-left text-sm font-light ">
<thead classNmae="border-b font-medium dark:border-neutral-500">
<tr>
<th scope="col" classNmae="px-6 py-4">
<input type="text" placeholder="Serial Number" className="input-lg" value={this.state.sl_no} name="sl_no" onChange={this.changeHandler}/>
</th>
<th scope="col" classNmae="px-6 py-4">
<input type="text" placeholder="Name of the Full Time Teacher" className="input-lg" value={this.state.name} name="name" onChange={this.changeHandler}/>
</th>
<th scope="col" classNmae="px-6 py-4">
<select className="select-lg select-bordered w-full " value={this.state.qualification} name="qualification" onChange={this.changeHandler}>
<option disabled selected>Qualification</option>
<option>Ph.D</option>
<option>D.MM</option>
<option>M.Ch</option>
<option>D.N.B Super Speciality</option>
<option>D.Sc</option>
<option>D.Lit</option>
</select>
</th>
</tr>
<tr>
<th scope="col" classNmae="px-6 py-4">
<input type="text" placeholder="Year of joining the insitution" className="input-lg" value={this.state.year_join} name="year_join" onChange={this.changeHandler}/>
</th>
<th scope="col" classNmae="px-6 py-4">
<input type="text" placeholder="Year of Obtaining Qualification" className="input-lg" value={this.state.year_qual} name="year_qual" onChange={this.changeHandler}/>
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

export default TwoEight