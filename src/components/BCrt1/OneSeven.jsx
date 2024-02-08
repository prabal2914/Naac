import React from 'react'
class OneSeven extends React.Component{

  constructor(){
    super();
    this.state={
        year:'',
        choice:'',
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
  fetch('http://127.0.0.1:8000/api/boneseven/',{
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
        choice:'',
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
               Part B Criteria 1 Table 1.4.1
            </h1>
    <h3 className="text-3xl mb-10 bg-gradient-to-r from-slate-100 to-slate-300 rounded-md shadow-xl  shadow-slate-900 ring-2 ring-slate-600">
    Structured feedback for curriculum and its transactions is regularly obtained from stakeholders like Students, Teachers, Employers, Alumni, Academic peers etc., and Feedback processes of the institution may be classified as follows: 
<br /> A. Feedback collected, analysed, action taken and feedback
hosted on the institutional website
<br /> B. Feedback collected, analysed and action has been taken
<br /> C. Feedback collected and analysed
<br /> D. Feedback collected
<br /> E. Feedback not collected.
    </h3>
    <div classNmae="overflow-hidden">
        <table>
            <thead>
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
            <select className="select-lg select-bordered w-full" value={this.state.choice} name="choice" onChange={this.changeHandler}>
  <option disabled selected>Choose The Option.</option>
  <option>A. Feedback collected, analysed, action taken and feedback
hosted on the institutional website.</option>
  <option>B.Feedback collected, analysed and action has been taken</option>
  <option>C. Feedback collected and analysed</option>
  <option>D. Feedback collected</option>
  <option>E. Feedback not collected</option>
</select>
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

export default OneSeven