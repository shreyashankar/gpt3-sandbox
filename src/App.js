import React from "react";
import { Form, Button, Row, Col } from "react-bootstrap";
import axios from "axios";
import { debounce } from "lodash";

import "bootstrap/dist/css/bootstrap.min.css";

const UI_PARAMS_API_URL = "/params";
const TRANSLATE_API_URL = "/translate";
const EXAMPLE_API_URL = "/examples";

const DEBOUNCE_INPUT = 250;

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      output: "",
      input: "",
      buttonText: "Submit",
      description: "Description",
      showExampleForm: false,
      examples: {}
    };
    // Bind the event handlers
    this.handleInputChange = this.handleInputChange.bind(this);
    this.handleClick = this.handleClick.bind(this);
  }

  componentDidMount() {
    // Call API for the UI params
    axios
      .get(UI_PARAMS_API_URL)
      .then(
        ({
          data: { placeholder, button_text, description, show_example_form }
        }) => {
          this.setState({
            input: placeholder,
            buttonText: button_text,
            description: description,
            showExampleForm: show_example_form
          });
          if (this.state.showExampleForm) {
            axios.get(EXAMPLE_API_URL).then(({ data: examples }) => {
              this.setState({ examples });
            });
          }
        }
      );
  }

  updateExample(id, body) {
    axios.put(`${EXAMPLE_API_URL}/${id}`, body);
  }

  debouncedUpdateExample = debounce(this.updateExample, DEBOUNCE_INPUT);

  handleExampleChange = (id, field) => e => {
    const text = e.target.value;

    let body = { [field]: text };
    let examples = { ...this.state.examples };
    examples[id][field] = text;

    this.setState({ examples });
    this.debouncedUpdateExample(id, body);
  };

  handleExampleDelete = id => e => {
    e.preventDefault();
    axios.delete(`${EXAMPLE_API_URL}/${id}`).then(({ data: examples }) => {
      this.setState({ examples });
    });
  };

  handleExampleAdd = e => {
    e.preventDefault();
    axios.post(EXAMPLE_API_URL).then(({ data: examples }) => {
      this.setState({ examples });
    });
  };

  handleInputChange(e) {
    this.setState({ input: e.target.value });
  }

  handleClick(e) {
    e.preventDefault();
    let body = {
      prompt: this.state.input
    };
    axios.post(TRANSLATE_API_URL, body).then(({ data: { text } }) => {
      this.setState({ output: text });
    });
  }

  render() {
    const showExampleForm = this.state.showExampleForm;
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
                {showExampleForm && (
                  <div>
                    <h4 style={{ marginBottom: "25px" }}>Examples</h4>
                    {Object.values(this.state.examples).map(example => (
                      <span key={example.id}>
                        <Form.Group
                          as={Row}
                          controlId={"formExampleInput" + example.id}
                        >
                          <Form.Label column="sm" lg={2}>
                            Example Input
                          </Form.Label>
                          <Col sm={10}>
                            <Form.Control
                              type="text"
                              as="input"
                              placeholder="Enter text"
                              value={example.input}
                              onChange={this.handleExampleChange(
                                example.id,
                                "input"
                              )}
                            />
                          </Col>
                        </Form.Group>
                        <Form.Group
                          as={Row}
                          controlId={"formExampleOutput" + example.id}
                        >
                          <Form.Label column="sm" lg={2}>
                            Example Output
                          </Form.Label>
                          <Col sm={10}>
                            <Form.Control
                              type="text"
                              as="textarea"
                              placeholder="Enter text"
                              value={example.output}
                              onChange={this.handleExampleChange(
                                example.id,
                                "output"
                              )}
                            />
                          </Col>
                        </Form.Group>
                        <Form.Group as={Row}>
                          <Col sm={{ span: 10, offset: 2 }}>
                            <Button
                              type="button"
                              size="sm"
                              variant="danger"
                              onClick={this.handleExampleDelete(example.id)}
                            >
                              Delete example
                            </Button>
                          </Col>
                        </Form.Group>
                      </span>
                    ))}
                    <Form.Group as={Row}>
                      <Col sm={{ span: 10 }}>
                        <Button
                          type="button"
                          variant="primary"
                          onClick={this.handleExampleAdd}
                        >
                          Add example
                        </Button>
                      </Col>
                    </Form.Group>
                  </div>
                )}
                <Form.Label>{this.state.description}</Form.Label>
                <Form.Control
                  type="text"
                  as="textarea"
                  placeholder="Enter text"
                  value={this.state.input}
                  onChange={this.handleInputChange}
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
