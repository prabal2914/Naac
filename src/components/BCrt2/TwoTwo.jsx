import React from 'react'
class TwoTwo extends React.Component{

  constructor(){
    super();
    this.state={
      year : '',
      res_sc: '',
      res_st: '',
      res_obc: '',
      res_general: '',
      res_others: '',
      adm_sc: '',
      adm_st: '',
      adm_obc: '',
      adm_general: '',
      adm_others: ''
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
  fetch('http://127.0.0.1:8000/api/btwotwo/',{
      method:'POST',
      body:JSON.stringify(this.state),
      headers:{
          'Content-type': 'application/json; charset=UTF-8',
      },
  })
  .then(response=>response.json())
  .then((data)=>console.log(data));

  this.setState({
    year : '',
    res_sc: '',
    res_st: '',
    res_obc: '',
    res_general: '',
    res_others: '',
    adm_sc: '',
    adm_st: '',
    adm_obc: '',
    adm_general: '',
    adm_others: ''
  });
}

render(){
  return (
    <div className="relative flex flex-col justify-center min-h-screen overflow-hidden bg-gradient-to-r from-slate-500 to-slate-800">
          <div className="w-full p-6 m-auto bg-gradient-to-r from-slate-300 to-slate-500 rounded-md shadow-xl shadow-slate-900 ring-2 ring-slate-600 lg:max-w-6xl">
  <div classNmae="inline-block min-w-full py-2 sm:px-6 lg:px-8">
  <h1 className="text-2xl font-semibold text-center mt-2 text-slate-800 underline uppercase decoration-bold mb-3">
               Part B Criteria 2 Table 2.1.2
            </h1>
    <h3 className="text-lg mb-2 bg-gradient-to-r from-slate-100 to-slate-300 rounded-md shadow-xl  shadow-slate-900 ring-2 ring-slate-600"> Percentage of seats filled against reserved categories (SC, ST, OBC etc.) as per applicable reservation policy for the first year admission year wise during the last five years.</h3>
    
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
        </thead>
      </table>
      <h3 className="text-xl mb-3 mt-3 bg-gradient-to-r from-slate-100 to-slate-300 rounded-md shadow-xl  shadow-slate-900 ring-2 ring-slate-600 w-full">Number of  seats earmarked for reserved category as per GOI or State Government rule</h3>
      <div className="join">
  <input className="input-lg input-bordered join-item" placeholder="SC"value={this.state.res_sc} name="res_sc" onChange={this.changeHandler}/>
  <input className="input-lg input-bordered join-item" placeholder="ST" value={this.state.res_st} name="res_st" onChange={this.changeHandler}/>
  <input className="input-lg input-bordered join-item" placeholder="OBC" value={this.state.res_obc} name="res_obc" onChange={this.changeHandler}/>
</div>
<div className="join">
  <input className="input-lg input-bordered join-item" placeholder="GENERAL" value={this.state.res_general} name="res_general" onChange={this.changeHandler}/>
  <input className="input-lg input-bordered join-item" placeholder="OTHERS" value={this.state.res_others} name="res_others" onChange={this.changeHandler}/>
</div>

<h3 className="text-xl mb-3 mt-3 bg-gradient-to-r from-slate-100 to-slate-300 rounded-md shadow-xl  shadow-slate-900 ring-2 ring-slate-600 w-full">Number of students admitted from the reserved category</h3>
      <div className="join">
  <input className="input-lg input-bordered join-item" placeholder="SC" value={this.state.adm_sc} name="adm_sc" onChange={this.changeHandler}/>
  <input className="input-lg input-bordered join-item" placeholder="ST" value={this.state.adm_st} name="adm_st" onChange={this.changeHandler}/>
  <input className="input-lg input-bordered join-item" placeholder="OBC" value={this.state.adm_obc} name="adm_obc" onChange={this.changeHandler}/>
</div>
<div className="join">
  <input className="input-lg input-bordered join-item" placeholder="GENERAL" value={this.state.adm_general} name="adm_general" onChange={this.changeHandler}/>
  <input className="input-lg input-bordered join-item" placeholder="OTHERS"value={this.state.adm_others} name="adm_others" onChange={this.changeHandler}/>
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

export default TwoTwo
