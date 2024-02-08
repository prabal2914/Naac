import React from 'react'
class FiveSeven extends React.Component{

  constructor(){
    super();
    this.state={
      year:'',
	name_st:'',
	year_qual:'',
	name_exam:'',
  level_exam:'',
	link:''
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
  fetch('http://127.0.0.1:8000/api/bfiveseven/',{
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
    name_st:'',
    year_qual:'',
    name_exam:'',
    level_exam:'',
    link:''
  });
}

render(){
  return (
    <div className="relative flex flex-col justify-center min-h-screen overflow-hidden bg-gradient-to-r from-slate-500 to-slate-800">
    <div className="w-full p-6 m-auto bg-gradient-to-r from-slate-300 to-slate-500 rounded-md shadow-xl shadow-slate-900 ring-2 ring-slate-600 lg:max-w-6xl">
<div classNmae="inline-block min-w-full py-2 sm:px-6 lg:px-8">
<h1 className="text-3xl font-semibold text-center text-slate-800 underline uppercase decoration-bold mb-5">
         Part B Criteria 5 Table 5.2.3
      </h1>
<h3 className="text-xl mb-3 bg-gradient-to-r from-slate-100 to-slate-300 rounded-md shadow-xl  shadow-slate-900 ring-2 ring-slate-600">Percentage of students qualifying in state/National/International level Examinations out of the graduated students during the last five years.</h3>

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
      <th scope="col" classNmae="px-6 py-4">
      <input type="text" placeholder="Name of the qualifying student" className="input-lg" value={this.state.name_st} name="name_st" onChange={this.changeHandler}/>
      </th>
    </tr> 
    <tr>
    <th scope="col" classNmae="px-6 py-4">
      <input type="text" placeholder="Name of comptetetive examination" className="input-lg" value={this.state.name_exam} name="name_exam" onChange={this.changeHandler}/>
      </th>
      <th scope="col" classNmae="px-6 py-4">
      <input type="text" placeholder="Level of exam" className="input-lg" value={this.state.level_exam} name="level_exam" onChange={this.changeHandler}/>
      </th>
      <th scope="col" classNmae="px-6 py-4">
      <input type="text" placeholder="Link to relevant documents" className="input-lg" value={this.state.link} name="link" onChange={this.changeHandler}/>
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

export default FiveSeven
