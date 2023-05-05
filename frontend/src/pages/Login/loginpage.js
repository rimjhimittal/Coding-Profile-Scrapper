import React from 'react';
import './login.css';

class LoginPage extends React.Component {
  constructor() {
    super();
    this.state = {
      email: '',
      password: '',
      login: false,
      store: null
    };
  }

  componentDidMount() {
    this.storeCollector();
  }

  storeCollector() {
    let store = JSON.parse(localStorage.getItem('login'));
    if (store && store.login) {
      this.setState({ login: true, store: store.token });
    }
  }

  login(e) {
    e.preventDefault()
    fetch('http://127.0.0.1:8000/login/', {
      method: 'POST',
      body: JSON.stringify(this.state),
      headers: {
        'Content-Type': 'application/json'
      }
    })
      .then((result) => {
        if (result.ok) {
          result.json().then((resp) => {
            console.log(resp);
            localStorage.setItem(
              'login',
              JSON.stringify({
                login: true,
                store: resp.token
              })
            );
            this.setState({ login: true, store: resp.token });
          });
        } else {
          throw new Error('Login failed');
        }
      })
      .catch((error) => {
        console.log(error);
      });
  }
  

  logout() {
    localStorage.removeItem('login');
    this.setState({ login: false, store: null });
  }

  render() {
    return (
      <div className="login-page">
        <div className="login-box">
          <h2 className="heading-login-box">Login</h2>
          {!this.state.login ? (
            <form>
              <div className="user-box">
                <input
                  className="user-box-input"
                  onChange={(event) => {
                    this.setState({ email: event.target.value });
                  }}
                  type="text"
                  value={this.state.email}
                  required
                />
                <label className="user-box-label">Email</label>
              </div>
              <div className="user-box">
                <input
                  className="user-box-input"
                  onChange={(event) => {
                    this.setState({ password: event.target.value });
                  }}
                  type="password"
                  required
                />
                <label className="user-box-label">Password</label>
              </div>
              <button
                type="submit"
                className="login-box-button"
                onClick={(e) => this.login(e)}
              >
                <span></span>
                <span></span>
                <span></span>
                <span></span>
                Submit
              </button>
            </form>
          ) : (
            <div>
              <p>Welcome! You are logged in.</p>
              <button onClick={() => this.logout()}>Logout</button>
            </div>
          )}

        </div>
      </div>
    );
  }
}

export default LoginPage;
