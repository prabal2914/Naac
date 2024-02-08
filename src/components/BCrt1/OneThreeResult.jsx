import React from 'react';

class OneThreeResult extends React.Component{
    constructor(){
        super();
        this.state={
            data:[]
        };
    }

    fetchData(){
        fetch('http://127.0.0.1:8000/api/bonethree/')
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

            </tr>
        );
        let sum=0;
        const keys = Object.keys(empData)
        keys.forEach(key=>{
            sum=sum+1;
        
        });
        let number = 10;
        let percentage = (sum/number)*50;
        
        return (
            <div>
            
            

           <h1>The marks received in this category is {percentage}</h1>
            </div>
        );
    }
    
}

export default OneThreeResult;