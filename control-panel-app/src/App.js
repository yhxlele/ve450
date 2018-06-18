import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import Panel from './Panel';

class App extends Component {
  render() {
    return (
      <div className="App">
        <Panel panelname="Deep Learning Container" description="Input python script path to train model" url="/api/sendtask"/>
      </div>
    ); 
  }
}

export default App;
