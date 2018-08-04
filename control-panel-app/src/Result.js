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
import Tabs from "components/CustomTabs/CustomTabs.jsx";
import Table from "components/Table/Table.jsx";

import withStyles from "@material-ui/core/styles/withStyles";
import Grid from '@material-ui/core/Grid';

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



class Result extends Component {

  componentWillMount() {
    fetch("/api/getfile", { credentials: 'same-origin' })
      .then((response) => {
        if (!response.ok) throw Error(response.statusText);
        return response.json();
      })
      .then((data) => {
        this.setState({
          file_list: data["file_list"]
        });
      })
      .catch(error => console.log(error)); // eslint-disable-line no-console
  }


  constructor(props) {
    // Initialize the state
    super(props);
    this.state = { "file_list": [] , "color_list": ["danger", "primary", "info", "success"]};
  }

  render() {

    const { classes } = this.props

    return (
      <Grid container spacing={50}>
        <Grid container spacing={50}>
          {
            this.state.file_list.map((file_content, i) =>
              (
                <GridItem xs={12} sm={12} md={8} className="Node-panel">
                <Card>
                  <CardHeader color={this.state.color_list[i%4]}>
                    <h4 className={classes.cardTitle}>{file_content["edge_ip"]}</h4>
                    <p> {file_content["container_id"]} </p>
                  </CardHeader>
                  <CardBody>
                  <pre>
                    {file_content["file_content"]}
                  </pre>
                  </CardBody>
                </Card>
            </GridItem>
              // <Panel 
              //   key={i} 
              //   color={color_list[i % color_list.length]} 
              //   panelname={container["container_name"]} 
              //   description={container["description"]} 
              //   url="/api/sendtask"
              //   container_id={container["container_id"]}
              //   ip={container["ip"]}/>
              
              )) 
          }
        </Grid>
      </Grid>
    );
  }
}



export default withStyles(styles)(Result);
