import React from 'react'
class TwoSeven extends React.Component{

  constructor(){
    super();
    this.state={
      year: '',
	prof: '',
	associate_prof: '',
	assisstant_prof: '',
	total: '',
	authority: '',
	name: '',
	designation: '',
	year_app: '',
	nature: '',
	dept_name: ''
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
  fetch('http://127.0.0.1:8000/api/btwoseven/',{
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
    prof: '',
    associate_prof: '',
    assisstant_prof: '',
    total: '',
    authority: '',
    name: '',
    designation: '',
    year_app: '',
    nature: '',
    dept_name: ''
  });
}

render(){
  return (
    <div className="relative flex flex-col justify-center min-h-screen overflow-hidden bg-gradient-to-r from-slate-500 to-slate-800">
          <div className="w-full p-6 m-auto bg-gradient-to-r from-slate-300 to-slate-500 rounded-md shadow-xl shadow-slate-900 ring-2 ring-slate-600 lg:max-w-6xl">
  <div classNmae="inline-block min-w-full py-2 sm:px-6 lg:px-8">
  <h1 className="text-3xl font-semibold text-center text-slate-800 underline uppercase decoration-bold mb-5">
               Part B Criteria 2 Table 2.4.1
            </h1>
    <h3 className="text-xl mb-3 bg-gradient-to-r from-slate-100 to-slate-300 rounded-md shadow-xl  shadow-slate-900 ring-2 ring-slate-600">Percentage of full time teachers appointed against the number of sanctioned posts year wise during the last five years</h3>
    
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
            <input type="text" placeholder="Total Professor" className="input-lg" value={this.state.total} name="total" onChange={this.changeHandler}/>
            </th>
          </tr> 

          <tr>
            <th scope="col" classNmae="px-6 py-4">
            <input type="text" placeholder="Sanctioned Professor" className="input-lg" value={this.state.prof} name="prof" onChange={this.changeHandler}/>
            </th>
            <th scope="col" classNmae="px-6 py-4">
            <input type="text" placeholder="Sanctioned Associate Professor" className="input-lg" value={this.state.associate_prof} name="associate_prof" onChange={this.changeHandler}/>
            </th>
            <th scope="col" classNmae="px-6 py-4">
            <input type="text" placeholder="Sanctioned Assistant Professor" className="input-lg" value={this.state.assisstant_prof} name="assisstant_prof" onChange={this.changeHandler}/>
            </th>
          </tr>
          <tr>
          <th scope="col" classNmae="px-6 py-4">
            <input type="text" placeholder="Sanctioning authority" className="input-lg" value={this.state.authority} name="authority" onChange={this.changeHandler}/>
            </th>
            <th scope="col" classNmae="px-6 py-4">
            <input type="text" placeholder="Name of the Full-time teacher" className="input-lg" value={this.state.name} name="name" onChange={this.changeHandler}/>
            </th>
            <th scope="col" classNmae="px-6 py-4">
            <input type="text" placeholder="Designation" className="input-lg" value={this.state.designation} name="designation" onChange={this.changeHandler}/>
            </th>
          </tr>
          <tr>
          <th scope="col" classNmae="px-6 py-4">
            <input type="text" placeholder="Year of  appointment" className="input-lg" value={this.state.year_app} name="year_app" onChange={this.changeHandler}/>
            </th>
            <th scope="col" classNmae="px-6 py-4">
            <input type="text" placeholder="Nature of appointment" className="input-lg" value={this.state.nature} name="nature" onChange={this.changeHandler}/>
            </th>
            <th scope="col" classNmae="px-6 py-4">
            <input type="text" placeholder="Name of the Department/Subject" className="input-lg" value={this.state.dept_name} name="dept_name" onChange={this.changeHandler}/>
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

export default TwoSeven


