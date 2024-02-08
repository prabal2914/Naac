import React from 'react'
class TwoFifteen extends React.Component{

  constructor(){
    super();
    this.state={
        year: '',
	name_student: '',
	gender: '',
	category: '',	
	domicile_state: '',
	nationality: '',
	email: '',
	name_program: '',
	st_UID: '',
	mobile: '',
	year_join: '',
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
  fetch('http://127.0.0.1:8000/api/btwofifteen/',{
      method:'POST',
      body:JSON.stringify(this.state),
      headers:{
          'Content-type': 'application/json; charset=UTF-8',
      },
  })
  .then(response=>response.json())
  .then((data)=>console.log(data));

  this.setState({
    year: '',
	name_student: '',
	gender: '',
	category: '',	
	domicile_state: '',
	nationality: '',
	email: '',
	name_program: '',
	st_UID: '',
	mobile: '',
	year_join: '',
  });
}

render(){
return (
<div className="relative flex flex-col justify-center min-h-screen overflow-hidden bg-gradient-to-r from-slate-500 to-slate-800">
<div className="w-full p-6 m-auto bg-gradient-to-r from-slate-300 to-slate-500 rounded-md shadow-xl shadow-slate-900 ring-2 ring-slate-600 lg:max-w-6xl">
<div classNmae="inline-block min-w-full py-2 sm:px-6 lg:px-8">
<h1 className="text-3xl font-semibold text-center text-slate-800 underline uppercase decoration-bold mb-5">
Part B Criteria 2 Table 2.7.1
</h1>
<h3 className="text-xl mb-3 bg-gradient-to-r from-slate-100 to-slate-300 rounded-md shadow-xl shadow-slate-900 ring-2 ring-slate-600">Student Satisfaction Survey.</h3>
<h3 className="text-xl mb-3 bg-gradient-to-r from-slate-100 to-slate-300 rounded-md shadow-xl shadow-slate-900 ring-2 ring-slate-600"> Online student satisfaction survey regarding teaching learning process.</h3>

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
<input type="text" placeholder="Name of the Student" className="input-lg" value={this.state.name_student} name="name_student" onChange={this.changeHandler}/>
</th>
<th scope="col" classNmae="px-6 py-4">
<select className="select-lg select-bordered w-full " value={this.state.gender} name="gender" onChange={this.changeHandler}>
<option disabled selected>Gender</option>
<option>Male</option>
<option>Female</option>
<option>Others</option>
</select>
</th>
<th scope="col" classNmae="px-6 py-4">
<input type="text" placeholder="Category" className="input-lg" value={this.state.category} name="category" onChange={this.changeHandler}/>
</th>
</tr>
<tr>
<th scope="col" classNmae="px-6 py-4">
<input type="text" placeholder="State of Domicile" className="input-lg" value={this.state.domicile_state} name="domicile_state" onChange={this.changeHandler}/>
</th>
<th scope="col" classNmae="px-6 py-4">
<input type="text" placeholder="Nationality if other than Indian" className="input-lg" value={this.state.nationality} name="nationality" onChange={this.changeHandler}/>
</th>
<th scope="col" classNmae="px-6 py-4">
<input type="text" placeholder="Email ID" className="input-lg" value={this.state.email} name="email" onChange={this.changeHandler}/>
</th>
</tr>
</thead>
</table>
<div>
<input type="text" placeholder="Programme Name" className="input-md" value={this.state.name_program} name="name_program" onChange={this.changeHandler}/>
<input type="text" placeholder="Student Unique Enrolment ID" className="input-md" value={this.state.st_UID} name="st_UID" onChange={this.changeHandler}/>
<input type="text" placeholder="Mobile Number" className="input-md" value={this.state.mobile} name="mobile" onChange={this.changeHandler} />
<input type="text" placeholder="Year of Joining" className="input-md" value={this.state.year_join} name="year_join" onChange={this.changeHandler}/>
</div>
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

export default TwoFifteen
