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

    this.primeText = `English: Two plus two equals four\nLaTeX: 2 + 2 = 4\n\nEnglish: The integral from zero to infinity\nLaTeX: \\int_0^{\\infty}\n\nEnglish: The gradient of x squared plus two times x with respect to x\nLaTeX: \\nabla_x x^2 + 2x\n\nEnglish: The log of two times x\nLaTeX: \\log{2x}\n\nEnglish: x squared plus y squared plus equals z squared\nLaTeX: x^2 + y^2 = z^2\n\nEnglish: The sum from zero to twelve of i squared\nLaTeX: \\sum_{i=0}^{12} i^2\n\nEnglish: E equals m times c squared\nLaTeX: E = mc^2\n\nEnglish: H naught of t\nLaTeX: H_0(t)\n\nEnglish: f of n equals 1 over (b-a) if n is 0 otherwise 5\nLaTeX: f(n) = \\begin{cases} 1/(b-a) &\\mbox{if } n \\equiv 0 \\\
    5 \\end{cases}\n\n`;

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
