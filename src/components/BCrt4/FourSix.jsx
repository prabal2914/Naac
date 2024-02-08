import React from 'react'
class Foursix extends React.Component{

  constructor(){
    super();
    this.state={
        add_mix_edit:'',
        lcs:'',
        central_inst:'',
        animal_house:'',
        museum:'',
        business_lab:'',
        reasearch:'',
        mootcourt:'',
        theatre:'',
        art:'',
        others:''
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
  fetch('http://127.0.0.1:8000/api/bfoursix/',{
      method:'POST',
      body:JSON.stringify(this.state),
      headers:{
          'Content-type': 'application/json; charset=UTF-8',
      },
  })
  .then(response=>response.json())
  .then((data)=>console.log(data));

  this.setState({
    add_mix_edit:'',
        lcs:'',
        central_inst:'',
        animal_house:'',
        museum:'',
        business_lab:'',
        reasearch:'',
        mootcourt:'',
        theatre:'',
        art:'',
        others:''
  });
}

render(){
  return (
    <div>
    <div className="relative flex flex-col justify-center min-h-screen overflow-hidden bg-gradient-to-r from-slate-500 to-slate-800">
          <div className="w-full p-6 m-auto bg-gradient-to-r from-slate-300 to-slate-500 rounded-md shadow-xl shadow-slate-900 ring-2 ring-slate-600 lg:max-w-6xl">
  <div classNmae="inline-block min-w-full py-2 sm:px-6 lg:px-8">
  <h1 className="text-3xl font-semibold text-center text-slate-800 underline uppercase decoration-bold mb-5">
               Part B Criteria 4 Table 4.3.3
            </h1>
    <h3 className="text-3xl mb-10 bg-gradient-to-r from-slate-100 to-slate-300 rounded-md shadow-xl  shadow-slate-900 ring-2 ring-slate-600">Institution has the following Facilities for e-content development  and other resource development.</h3>
    <div classNmae="overflow-hidden">
        <table>
            <thead>
                <tr>
                    <th>
                    <select className="select-lg select-bordered w-full " value={this.state.add_mix_edit} name="add_mix_edit" onChange={this.changeHandler}>
<option disabled selected>Audio visual center</option>
<option>YES</option>
<option>NO</option>
</select>
                    </th>
                    <th>
                    <select className="select-lg select-bordered w-full " value={this.state.lcs} name="lcs" onChange={this.changeHandler}>
<option disabled selected>Lecture Capturing System</option>
<option>YES</option>
<option>NO</option>
</select>
                    </th>
                    <th>
                    <select className="select-lg select-bordered w-full " value={this.state.central_inst} name="central_inst" onChange={this.changeHandler}>
<option disabled selected>Central Instrumentation Centre</option>
<option>YES</option>
<option>NO</option>
</select>
                    </th>
                </tr>

                <tr>
                    <th>
                    <select className="select-lg select-bordered w-full " value={this.state.animal_house} name="animal_house" onChange={this.changeHandler}>
<option disabled selected>Animal House</option>
<option>YES</option>
<option>NO</option>
</select>
                    </th>
                    <th>
                    <select className="select-lg select-bordered w-full " value={this.state.museum} name="museum" onChange={this.changeHandler}>
<option disabled selected>Museum</option>
<option>YES</option>
<option>NO</option>
</select>
                    </th>
                    <th>
                    <select className="select-lg select-bordered w-full " value={this.state.business_lab} name="business_lab" onChange={this.changeHandler}>
<option disabled selected>Business Lab</option>
<option>YES</option>
<option>NO</option>
</select>
                    </th>
                </tr>

                <tr>
                    <th>
                    <select className="select-lg select-bordered w-full " value={this.state.reasearch} name="reasearch" onChange={this.changeHandler}>
<option disabled selected>Research/statistical database</option>
<option>YES</option>
<option>NO</option>
</select>
                    </th>
                    <th>
                    <select className="select-lg select-bordered w-full " value={this.state.mootcourt} name="mootcourt" onChange={this.changeHandler}>
<option disabled selected>Mootcourt</option>
<option>YES</option>
<option>NO</option>
</select>
                    </th>
                    <th>
                    <select className="select-lg select-bordered w-full " value={this.state.theatre} name="theatre" onChange={this.changeHandler}>
<option disabled selected>Theatre</option>
<option>YES</option>
<option>NO</option>
</select>
                    </th>
                </tr>

                <tr>
                    <th>
                    <select className="select-lg select-bordered w-full " value={this.state.art} name="art" onChange={this.changeHandler}>
<option disabled selected>Art Gallery</option>
<option>YES</option>
<option>NO</option>
</select>
                    </th>
                    <th>
                    <select className="select-lg select-bordered w-full " value={this.state.others} name="others" onChange={this.changeHandler}>
<option disabled selected>Any other facultiy to support research</option>
<option>YES</option>
<option>NO</option>
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

export default Foursix
