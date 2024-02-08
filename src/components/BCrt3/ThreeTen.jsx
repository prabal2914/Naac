import React from 'react'
class ThreeTen extends React.Component{

  constructor(){
    super();
    this.state={
        title:'',
        name_author:'',
        teacher_dept:'',
        name_journal:'',
        year:'',
        issn:'',
        link_website:'',
        link_article:'',
        listed:''
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
  fetch('http://127.0.0.1:8000/api/bthreeten/',{
      method:'POST',
      body:JSON.stringify(this.state),
      headers:{
          'Content-type': 'application/json; charset=UTF-8',
      },
  })
  .then(response=>response.json())
  .then((data)=>console.log(data));

  this.setState({
    title:'',
    name_author:'',
    teacher_dept:'',
    name_journal:'',
    year:'',
    issn:'',
    link_website:'',
    link_article:'',
    listed:''
  });
}

render(){
return (
<div className="relative flex flex-col justify-center min-h-screen overflow-hidden bg-gradient-to-r from-slate-500 to-slate-800">
<div className="w-full p-6 m-auto bg-gradient-to-r from-slate-300 to-slate-500 rounded-md shadow-xl shadow-slate-900 ring-2 ring-slate-600 lg:max-w-6xl">
<div classNmae="inline-block min-w-full py-2 sm:px-6 lg:px-8">
<h1 className="text-3xl font-semibold text-center text-slate-800 underline uppercase decoration-bold mb-5">
Part B Criteria 3 Table 3.4.4
</h1>
<h3 className="text-xl mb-3 bg-gradient-to-r from-slate-100 to-slate-300 rounded-md shadow-xl shadow-slate-900 ring-2 ring-slate-600">Number of research papers published per teacher in the Journals as notified on UGC CARE list during the last five years.</h3>
<table classNmae="min-w- text-left text-sm font-light ">
<thead classNmae="border-b font-medium dark:border-neutral-500">
<tr>
<th scope="col" classNmae="px-6 py-4">
<input type="text" placeholder="Title of paper" className="input-lg" value={this.state.title} name="title" onChange={this.changeHandler}/>
</th>
<th scope="col" classNmae="px-6 py-4">
<input type="text" placeholder="Name of author" className="input-lg" value={this.state.name_author} name="name_author" onChange={this.changeHandler}/>
</th>
<th scope="col" classNmae="px-6 py-4">
<input type="text" placeholder="Department of teacher" className="input-lg" value={this.state.teacher_dept} name="teacher_dept" onChange={this.changeHandler}/>
</th>
</tr> 
<tr>
<th scope="col" classNmae="px-6 py-4">
<input type="text" placeholder="Name of journal" className="input-lg" value={this.state.name_journal} name="name_journal" onChange={this.changeHandler}/>
</th>
<th scope="col" classNmae="px-6 py-4">
<input type="text" placeholder="Year of publication" className="input-lg" value={this.state.year} name="year" onChange={this.changeHandler}/>
</th>
<th scope="col" classNmae="px-6 py-4">
<input type="text" placeholder="ISSN number" className="input-lg" value={this.state.issn} name="issn" onChange={this.changeHandler}/>
</th>
</tr> 
<tr>
<th scope="col" classNmae="px-6 py-4">
<input type="text" placeholder="Link to Journal website" className="input-lg" value={this.state.link_website} name="link_website" onChange={this.changeHandler}/>
</th>
<th scope="col" classNmae="px-6 py-4">
<input type="text" placeholder="Link to article/paper" className="input-lg" value={this.state.link_article} name="link_article" onChange={this.changeHandler}/>
</th>
<th scope="col" classNmae="px-6 py-4">
<select className="select-lg select-bordered w-full " value={this.state.listed} name="listed" onChange={this.changeHandler}>
<option disabled selected>Listed in UGC care</option>
<option>Yes</option>
<option>No</option>
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
)
}
}

export default ThreeTen