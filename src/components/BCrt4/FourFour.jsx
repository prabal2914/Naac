import React from 'react'
class FourFour extends React.Component{

  constructor(){
    super();
    this.state={
      description:'',
	add_info:'',
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
  fetch('http://127.0.0.1:8000/api/bfourfour/',{
      method:'POST',
      body:JSON.stringify(this.state),
      headers:{
          'Content-type': 'application/json; charset=UTF-8',
      },
  })
  .then(response=>response.json())
  .then((data)=>console.log(data));

  this.setState({
    description:'',
    add_info:'',
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
               Part B Criteria 4 Table 4.3.1
            </h1>
    <h3 className="text-3xl mb-10 bg-gradient-to-r from-slate-100 to-slate-300 rounded-md shadow-xl  shadow-slate-900 ring-2 ring-slate-600">Describe IT facilities including Wi-Fi with date and nature of
updation, available internet bandwidth within a maximum of 500
words.</h3>
    <div classNmae="overflow-hidden">
    <textarea className="textarea textarea-bordered w-full" placeholder="Write description here" value={this.state.description} name="description" onChange={this.changeHandler}></textarea>
        <table>
            <thead>
                <tr>
                    <th>
                    <textarea className="textarea textarea-bordered w-full" placeholder="Add Additional Information" value={this.state.add_info} name="add_info" onChange={this.changeHandler}></textarea>
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

export default FourFour
