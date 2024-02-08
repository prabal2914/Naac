import React from 'react'
class SevenTwo extends React.Component{

  constructor(){
    super();
    this.state={
        alt_source:'',
        option:'',
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
  fetch('http://127.0.0.1:8000/api/bseventwo/',{
      method:'POST',
      body:JSON.stringify(this.state),
      headers:{
          'Content-type': 'application/json; charset=UTF-8',
      },
  })
  .then(response=>response.json())
  .then((data)=>console.log(data));

  this.setState({
    alt_source:'',
        option:'',
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
               Part B Criteria 7 Table 7.1.2
            </h1>
    <h3 className="text-3xl mb-10 bg-gradient-to-r from-slate-100 to-slate-300 rounded-md shadow-xl  shadow-slate-900 ring-2 ring-slate-600">The Institution has facilities for alternate sources of energy and energy conservation measures:</h3>
    <div classNmae="overflow-hidden">
      <table>
            <thead>
                <tr>
<th scope="col" classNmae="px-6 py-4">
<select className="select-lg select-bordered w-full " value={this.state.alt_source} name="alt_source" onChange={this.changeHandler}>
<option disabled selected>Alternate sources of energy</option>
<option>Solar energy</option>
<option>Bio gas plant </option>
<option>Wheeling to the Grid</option>
<option>Sensor-based energy conservation</option>
<option>Use of LED bulbs/ power efficient equipment</option>
<option>Wind mill or any other clean green energy</option>
</select>
</th>
<th scope="col" classNmae="px-6 py-4">
<select className="select-lg select-bordered w-full " value={this.state.option} name="option" onChange={this.changeHandler}>
<option disabled selected>Options</option>
<option>YES</option>
<option>NO</option>
</select>
</th>
                    <th>
                    <input type="text" placeholder="Link for additional information" className="input-lg" value={this.state.link} name="link" onChange={this.changeHandler}/>
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

export default SevenTwo
