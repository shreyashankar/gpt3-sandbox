import React from "react";
import { Form, Button } from "react-bootstrap";
import axios from "axios";

import "bootstrap/dist/css/bootstrap.min.css";

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      output: "",
      input: "",
      buttonText: "Submit",
      description: "Description"
    };

    // Bind the event handlers
    this.handleChange = this.handleChange.bind(this);
    this.handleClick = this.handleClick.bind(this);
  }

  componentDidMount() {
    // Call API for the UI params
    const url = "/params";
    axios
      .get(url)
      .then(({ data: { placeholder, button_text, description } }) => {
        this.setState({
          input: placeholder,
          buttonText: button_text,
          description: description
        });
      });
  }

  handleChange(e) {
    this.setState({ input: e.target.value });
  }

  handleClick(e) {
    e.preventDefault();
    const url = "/translate";
    let data = {
      prompt: this.state.input
    };

    axios.post(url, data).then(({ data: { text } }) => {
      this.setState({ output: text });
    });
  }

  render() {
    return (
      <div>
        <head />
        <body style={{ alignItems: "center", justifyContent: "center" }}>
          <div
            style={{
              margin: "auto",
              marginTop: "80px",
              display: "block",
              maxWidth: "500px",
              minWidth: "200px",
              width: "50%"
            }}
          >
            <Form onSubmit={this.handleClick}>
              <Form.Group controlId="formBasicEmail">
                <Form.Label>{this.state.description}</Form.Label>
                <Form.Control
                  type="text"
                  as="textarea"
                  placeholder="Enter text"
                  value={this.state.input}
                  onChange={this.handleChange}
                />
              </Form.Group>

              <Button variant="primary" type="submit">
                {this.state.buttonText}
              </Button>
            </Form>
            <div
              style={{
                textAlign: "center",
                margin: "20px",
                fontSize: "18pt"
              }}
            >
              {this.state.output}
            </div>
          </div>
        </body>
      </div>
    );
  }
}

export default App;
