import React from 'react';
import Loginbox from './loginbox';
import './login.css';
class LoginPage extends React.Component {

  constructor()
  {
    super();
    this.state={
      email:"",
      password:"",
      login: false,
      store: null
    }
  }

componentDidMount(){
  this.storeCollector()
}
storeCollector(){
  let store=JSON.parse(localStorage.getItem("login"));
  if(store && store.login){
    this.setState({login:true,store:store.token})
  }
}

  login(){
    fetch('', {
      method: 'POST',
      body:JSON.stringify(this.state)
    }).then((result)=>{
      result.json().then((resp)=>{
        console.warn(resp)
        localStorage.setItem("login",JSON.stringify({
          login: true,
          store: resp.token
        }))
        this.setState({login:true,store:resp.token})
      })
    })
  }
  // post(){
  //   let token= 'Bearer' + this.state.store.token
  //   fetch('', {
  //     method: 'POST',
  //     headers: {
  //       'Authorization': token,
  //     },
  //     body:JSON.stringify(this.state.post)
  //   }).then((result)=>{
  //     result.json().then((resp)=>{
  //       console.warn(resp)
  //     })
  //   })
  // }
  render(){
  return (
    <div>
      <body classNameName="login-page">
    <div className="login-box">
        <h2 className="heading-login-box">Login</h2>
        {!this.state.login?
        <form>
            <div className="user-box">
                <input className="user-box-input" onChange={(event)=>{this.setState({email:event.target.value})}} type="text" required />
                <label className="user-box-label">Email</label>
            </div>
            <div className="user-box">
                <input className="user-box-input" onChange={(event)=>{this.setState({password:event.target.value})}} type="password" required />
                <label className="user-box-label">Password</label>
            </div>
            <a type="submit" className="login-box-button" href="/" >
                <span></span>
                <span></span>
                <span></span>
                <span></span>
                Submit
            </a>
        </form>
        : 
        <div></div>
        }

        {/* <div>
          <textarea onChange={(event)=>this.setState({post:event.target.value})}>
          </textarea>
             <button onClick={()=>{this.post()}}>Post</button> 
          
        </div> */}
    </div>
</body>
    </div>
 
    );
      
}
}

export default LoginPage;
