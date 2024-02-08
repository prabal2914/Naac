import React from 'react'
class OneFive extends React.Component{

  constructor(){
    super();
    this.state={
      name:'',
      mode_course:'',
      course_code:'',
      year:'',
      hours:'',
      st_enrolled:'',
      st_completed:'',
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
  fetch('http://127.0.0.1:8000/api/bonefive/',{
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
      mode_course:'',
      course_code:'',
      year:'',
      hours:'',
      st_enrolled:'',
      st_completed:'',
      link:''
  });
}

render(){
  return (
    <div>
    <div className="relative flex flex-col justify-center min-h-screen overflow-hidden bg-gradient-to-r from-slate-500 to-slate-800">
          <div className="w-full p-6 m-auto bg-gradient-to-r from-slate-300 to-slate-500 rounded-md shadow-xl shadow-slate-900 ring-2 ring-slate-600 lg:max-w-6xl">
  <div classNmae="inline-block min-w-full py-2 sm:px-6 lg:px-8">
  <h1 className="text-3xl font-semibold text-center text-slate-800 underline uppercase decoration-bold mb-5">
               Part B Criteria 1 Table 1.3.2
            </h1>
    <h3 className="text-3xl mb-10 bg-gradient-to-r from-slate-100 to-slate-300 rounded-md shadow-xl  shadow-slate-900 ring-2 ring-slate-600"> Number of certificate/ value added courses/ Diploma Programmes offered by the institutions and online courses of MOOCs, SWAYAM/e-PG Pathshala/ NPTEL and other recognized platforms where the students of the institution have enrolled and successfully completed during the last five years.</h3>
    <div classNmae="overflow-hidden">
        <table>
            <thead>
            <tr>
            <th scope="col" classNmae="px-6 py-4">
            <input type="text" placeholder="Name of the Course" className="input-lg" value={this.state.name} name="name" onChange={this.changeHandler}/>
            </th>
            <th scope="col" classNmae="px-6 py-4">
            <input type="text" placeholder="Course code" className="input-lg" value={this.state.course_code} name="course_code" onChange={this.changeHandler}/>
            </th>
            <th scope="col" classNmae="px-6 py-4">
            <input type="text" placeholder="Mode of Course offered by HEI" className="input-lg" value={this.state.mode_course} name="mode_course" onChange={this.changeHandler}/>
            </th>
          </tr> 
          <tr>
          <th scope="col" classNmae="px-6 py-4">
            <input type="text" placeholder="Year of Offering/Enrollment" className="input-lg" value={this.state.year} name="year" onChange={this.changeHandler}/>
            </th>
            <th scope="col" classNmae="px-6 py-4">
            <input type="text" placeholder="Contact hours of course" className="input-lg" value={this.state.hours} name="hours" onChange={this.changeHandler}/>
            </th>
            <th scope="col" classNmae="px-6 py-4">
            <input type="text" placeholder="Students enrolled in the year" className="input-lg" value={this.state.st_enrolled} name="st_enrolled" onChange={this.changeHandler}/>
            </th>
          </tr> 
          <tr>
          <th scope="col" classNmae="px-6 py-4">
            <input type="text" placeholder="Students completing the course" className="input-lg" value={this.state.st_completed} name="st_completed" onChange={this.changeHandler}/>
            </th>
            <th scope="col" classNmae="px-6 py-4">
            <input type="text" placeholder="Link to the relevant documents" className="input-lg" value={this.state.link} name="link" onChange={this.changeHandler}/>
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

export default OneFive


