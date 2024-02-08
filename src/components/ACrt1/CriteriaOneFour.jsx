import React from 'react'
class CriteriaOneFour extends React.Component{

  constructor(){
    super();
    this.state={
      	add_info:'',
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
  fetch('http://127.0.0.1:8000/api/aonefour/',{
      method:'POST',
      body:JSON.stringify(this.state),
      headers:{
          'Content-type': 'application/json; charset=UTF-8',
      },
  })
  .then(response=>response.json())
  .then((data)=>console.log(data));

  this.setState({
    	add_info:'',
  });
}

render(){
  return (
    <div>
    <div className="relative flex flex-col justify-center min-h-screen overflow-hidden bg-gradient-to-r from-slate-500 to-slate-800">
        <div className="w-full p-6 m-auto bg-gradient-to-r from-slate-300 to-slate-500 rounded-md shadow-xl shadow-slate-900 ring-2 ring-slate-600 lg:max-w-5xl">
        <h1 className="text-3xl font-semibold text-center text-slate-800 underline uppercase decoration-bold">
               1.4 Any Additional Information
            </h1>
            <br></br>
            <textarea placeholder="About the Institution other than the ones already stated." className="textarea textarea-bordered textarea-lg w-full p-6 max-w-5xl" value={this.state.add_info} name="add_info" onChange={this.changeHandler}></textarea>
            <div class="flex w-1/2 ">
          <button onClick={this.submitForm} className="w-1/2 px-4 py-2 m-4 tracking-wide text-white transition-colors duration-200 transform bg-emerald-700 rounded-md-emerald-900 rounded-md hover:bg-emerald-500 focus:outline-none focus:bg-emerald-900">
                      Done 
            </button>

            <button className="w-1/2 px-4 py-2 m-4 tracking-wide text-white transition-colors duration-200 transform bg-emerald-700 rounded-md-emerald-900 rounded-md hover:bg-emerald-500 focus:outline-none focus:bg-emerald-900">
                      Back
            </button>
            </div>
            </div>
      
    </div>
    </div>
  )
}
}
export default CriteriaOneFour