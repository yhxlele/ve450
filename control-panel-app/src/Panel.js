import React, { Component } from 'react';
import './App.css';
import Button from '@material-ui/core/Button';
import Paper from '@material-ui/core/Paper';

import TextField from '@material-ui/core/TextField'

// import Card from "./components/Card/Card.jsx";

import GridItem from "components/Grid/GridItem.jsx";
import Card from "components/Card/Card.jsx";
import CardBody from "components/Card/CardBody.jsx";
import CardHeader from "components/Card/CardHeader.jsx";

import dashboardStyle from "assets/jss/material-dashboard-react/views/dashboardStyle";
import CustomInput from "components/CustomInput/CustomInput.jsx";

import withStyles from "@material-ui/core/styles/withStyles";

var styles = {
  ...dashboardStyle,
  cardTitle: {
    marginTop: "0",
    minHeight: "auto",
    fontWeight: "1000",
    fontFamily: "'Roboto', 'Helvetica', 'Arial', sans-serif",
    marginBottom: "0px",
    textDecoration: "none",
    fontSize: "24px"
  }
};


class Panel extends Component {


  constructor(props) {
    // Initialize the state
    super(props);
    this.state = { input_dir: '', output_dir: '', params: '' };
    this.handleChangeInput = this.handleChangeInput.bind(this);
    this.handleChangeOutput = this.handleChangeOutput.bind(this);
    this.handleChangeParams = this.handleChangeParams.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  render() {

    const { classes } = this.props

    return (
      <GridItem xs={12} sm={12} md={4} className="Node-panel">
          <Card>
            <CardHeader color={this.props.color}>
              <h4 className={classes.cardTitle}>{this.props.panelname}</h4>
              <p> {this.props.description} </p>
            </CardHeader>
            <CardBody>
            <form id="comment-form" onSubmit={this.handleSubmit}>
              <div className="row">
                <TextField
                  className="fullwidth"
                  id="name full-width"
                  label="Python Script Path"
                  margin="normal"
                  fullWidth
                  value={this.state.input_dir}
                  onChange={this.handleChangeInput}
                />
              </div>
              <div className="row">
              <TextField
                className="fullwidth"
                id="name full-width"
                label="Output Path"
                margin="normal"
                fullWidth
                value={this.state.output_dir}
                onChange={this.handleChangeOutput}
              />
              </div>
              <div className="row">
              <TextField
                className="fullwidth"
                id="name"
                label="Parameter Lists"
                margin="normal"
                fullWidth
                value={this.state.params}
                onChange={this.handleChangeParams}
              />
              </div>
              <div className="submitbutton row">
                <Button type="submit" variant="contained" color="primary">
                  Submit
                </Button>
              </div>
           </form>

            </CardBody>
          </Card>
      </GridItem>
    );
  }


  handleChangeInput(event) {
    event.preventDefault();
    this.setState({
      input_dir: event.target.value,
    });
  };

  handleChangeOutput(event) {
    event.preventDefault();
    this.setState({
      output_dir: event.target.value,
    });
  };
  
  handleChangeParams(event) {
    event.preventDefault();
    this.setState({
      params: event.target.value,
    });
  }''
  
  handleSubmit(event) {
    event.preventDefault();
    console.log(this.props.url)
    fetch(this.props.url, {
      credentials: 'include',
      method: 'POST',
      body: JSON.stringify({
        job: this.props.panelname,
        input_dir: this.state.input_dir,
        output_dir: this.state.output_dir,
        params: this.state.params,
        ip: this.props.ip
      }),
    })
      .then((response) => {
        if (!response.ok) {
          window.alert("Bad Request!");
          throw Error(response.statusText);
        } else {
          window.alert("Success!");
        }
        return response.json();
      })
      .then((data) => {
        console.log(data)
        this.setState({
          input_dir: "",
          output_dir: "",
          params: ""
        });
      })
      .catch(error => console.log(error)); // eslint-disable-line no-console
  }
}

export default withStyles(styles)(Panel);
