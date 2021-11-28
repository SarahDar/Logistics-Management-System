import logo from './logo.svg';
import './App.css';
//import Login from '/Users/sarahdar/lms-app/src/login.js';
import {Switch, Router, Routes, Route} from 'react-router-dom';
import React from 'react';


/*const App = () =>{
  return(
    <div>
      <Switch>
      <Route exact path = '/' component = {Login}/>
      </Switch>
    </div>
    )
}*/

class App extends React.component
{
  state={
    ID:'',
    username: '',
    pwd:''
  }
  handlechange= (e) =>{
     this.setState({[name]:value})
  }

  handleSubmit = (e) =>{
    e.preventDefault
  } 
  render(){ 
    return( 
      <div> 
        <div> 
          <form onSubmit = {this.handleSubmit}> 
            <input type = 'ID' name ='email' placeholder = 'email...' required onChange = {this.handleChange}/> 
            <input type = 'username' name ='username' placeholder = 'username...' required onChange = {this.handleChange}/>
            <input type = 'password' name ='pwd' placeholder = 'password...' required onChange = {this.handleChange}/>  
            <button onSubmit = {this.handleSubmit  }> Log In </button>
          </form>
        </div> 
      </div>

      );
  }
} 




export default App;

