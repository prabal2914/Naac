import React from 'react';

class OneSevenResult extends React.Component{
    constructor(){
        super();
        this.state={
            data:[]
        };
    }

    fetchData(){
        fetch('http://127.0.0.1:8000/api/boneseven/')
        .then(response=>response.json())
        .then((data)=>{
            this.setState({
                data:data
            });
        });
    }

    componentDidMount(){
        this.fetchData();
    }



    render(){
        const empData=this.state.data;
        const rows=empData.map((emp)=>
            <tr key={emp.id}>
                <td>{emp.year}</td>
                <td>{emp.choice}</td>
                <td>{emp.link}</td>
            </tr>
        );
        let sum=0;
        const keys = Object.keys(empData)
        keys.forEach(key=>{
            if(empData[key].choice==='A')
            sum=sum+4;
            else if(empData[key].choice==='B')
            sum=sum+3;
            else if(empData[key].choice==='C')
            sum=sum+2;
            else if(empData[key].choice==='D')
            sum=sum+1;
            else if(empData[key].choice==='E')
            sum=sum+0;
        
        });


        return (
            <div>
            <table className="table table-bordered">
                <thead>
                    <tr>
                        <th>Year</th>
                        <th>Choice</th>
                        <th>Link</th>
                    </tr>
                </thead>
                <tbody>
                    {rows}
                </tbody>
            </table>

           <h1>The marks received in this category is {sum}</h1>
            </div>
        );
    }
    
}

export default OneSevenResult;