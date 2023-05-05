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

  login() {
    fetch('http://127.0.0.1:8000/login/', {
      method: 'POST',
      body: JSON.stringify(this.state)
    }).then((result) => {
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
              <a
                type="submit"
                className="login-box-button"
                href="/"
                onClick={() => this.login()}
              >
                <span></span>
                <span></span>
                <span></span>
                <span></span>
                Submit
              </a>
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
