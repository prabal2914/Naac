import React from 'react';
import { Link } from 'react-router-dom';

class List extends React.Component{
    constructor(){
        super();
        this.state={
            data:[]
        };
    }

    fetchData(){
        fetch('http://127.0.0.1:8000/api/boneone/')
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

    deleteData(id){
        fetch('http://127.0.0.1:8000/api/boneone/'+id+'/',{
            method:'DELETE',
            body:JSON.stringify(this.state),
        })
        .then(response=>response)
        .then((data)=>{
            if(data){
                this.fetchData();
            }
        });
    }

    render(){
        const empData=this.state.data;
        const rows=empData.map((emp)=>
            <tr key={emp.id}>
                <td>{emp.description}</td>
                <td>{emp.add_info}</td>
                <td>{emp.link}</td>
                <td>
                    <button onClick={()=>this.deleteData(emp.id)} className="btn btn-danger">Delete</button>
                </td>
            </tr>
        );
        return (
            <div>
            <table className="table table-bordered">
                <thead>
                    <tr>
                        <th>Description</th>
                        <th>Additional Info</th>
                        <th>LINK</th>
                    </tr>
                </thead>
                <tbody>
                    {rows}
                </tbody>
            </table>
            </div>
        );
    }
    
}

    export default List;