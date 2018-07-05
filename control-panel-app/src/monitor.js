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



class Monitor extends Component {

  componentWillMount() {
    fetch("/api/getInstanceData", { credentials: 'same-origin' })
      .then((response) => {
        if (!response.ok) throw Error(response.statusText);
        return response.json();
      })
      .then((data) => {
        var Num = data["data"].length
        for (var i = 0; i < Num; i++){
          var dic = data["data"][i]
          var containers = []
          Object.keys(dic).forEach(function(key){
            var container = dic[key]
            containers.push([container["ip"], container["container_id"], container["container_num"], container["container_name"]])
          });
          this.setState({
            container_list: containers
          });
        }
        
      })
      .catch(error => console.log(error)); // eslint-disable-line no-console
  }


  constructor(props) {
    // Initialize the state
    super(props);
    this.state = { "container_list": [] };
  }

  render() {

    const { classes } = this.props

    return (
      <Grid container spacing={50}>

        <GridItem xs={12} sm={12} md={8} className="Node-panel">
        <Table
            tableHeaderColor="primary"
            tableHead={['Machine IP','Container ID','Replica Num','Name']}
            tableData={
              this.state["container_list"]
            }
        />
        </GridItem>
      </Grid>
    );
  }
}



export default withStyles(styles)(Monitor);
