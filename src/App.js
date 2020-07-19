import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import {Form, Button} from 'react-bootstrap';
import logo from './logo.svg';
import './App.css';
import 'katex/dist/katex.min.css'
import Latex from 'react-latex-next'
import axios from 'axios'

class App extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      latexStr: '',
      value: 'x squared plus two times x' };

    // This binding is necessary to make `this` work in the callback
    this.handleChange = this.handleChange.bind(this);
    this.handleClick = this.handleClick.bind(this);
  }

  handleChange(e) {
    this.setState({value: e.target.value});
  }

  handleClick(e) {
    e.preventDefault();
    const url = '/translate'

    let d = {
      prompt: this.state.value 
    }

    axios.post(url, d).then((res) => {
      let str = res.data.text;
      console.log(str)
      this.setState({latexStr: '$' + str.substring(6) + '$'});
    });
  }

  render() {
    return (
      <div>
        <head>
        </head>
        <body style={{'padding': '100px 400px'}}>
          <Form onSubmit={this.handleClick}>
            <Form.Group controlId="formBasicEmail">
              <Form.Label>Equation description</Form.Label>
              <Form.Control type="text" as='textarea' value={this.state.value} onChange={this.handleChange}/>
            </Form.Group>

            <Button variant="primary" type="submit">
              Translate
            </Button>
          </Form>
          <div style={{'margin': 'auto', 'textAlign': 'center', 'padding': '20px'}}>
          <Latex>{this.state.latexStr}</Latex>
          </div>
        </body>
      </div>
    );
  }
}

export default App;
