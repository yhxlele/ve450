import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import Panel from './Panel';
import Grid from '@material-ui/core/Grid';

class App extends Component {

  constructor(props) {
    // Initialize mutable state
    super(props);
    this.state = { "container_list": [] };
  }

  componentWillMount() {
    fetch("/api/getInstanceData", { credentials: 'same-origin' })
      .then((response) => {
        if (!response.ok) throw Error(response.statusText);
        return response.json();
      })
      .then((data) => {
        console.log(data)
        this.setState({
          container_list: data["data"]
        });
      })
      .catch(error => console.log(error)); // eslint-disable-line no-console
  }


  render() {
    const container_list = this.state["container_list"];
    const color_list = ["danger", "primary", "info", "success"];
    console.log(container_list)
    return (
      <div className="App">
        <Grid container spacing={50}>
          {
            container_list.map((container, i) =>
              (<Panel 
                key={i} 
                color={color_list[i % color_list.length]} 
                panelname={container["container_name"]} 
                description={container["description"]} 
                url="/api/sendtask"
                ip={container["ip"]}/>))
          }
        </Grid>
      </div>
    ); 
  }
}

export default App;
