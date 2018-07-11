# Workload Autonamous Distribution System

This is the repo for the workload autonamous distribution system for an edge computing system. The system will take the upcoming request from the user or other machine end to distribute the task to the edge nodes. The nodes with the same functionability can form as a cluster of machine. 

## Getting Started

The system is computing of three parts:

- Distributor: Responsible for the distribution of tasks and monitor of the edge nodes' status
- Edge Clusters: The collection of machine and software replica that resides on the machine.
- Control Dashboard: A UI system to call the api on the distributor and distribute task and monitor the ndoes.

### Prerequisites

Before using our system, you need to install the ```docker```

### System Start

To start the whole system, we need to first start the Distributor through virtual environment:

```
# $PROJECT_ROOT is this repo folder
cd $PROJECT_ROOT
python3 -m venv env
source env/bin/activate
pip install --upgrade pip setuptools wheel
pip install nodeenv
nodeenv --python-virtualenv

# reactivate the environment
deactivate
source env/bin/activate
sh run_central.sh
```

You should see an app running on the port 8000. Then open another terminal for the UI system

```
# open another terminal
cd $PROJECT_ROOT
source env/bin/activate
cd control-panel-app
npm install .
cd ..

# run the control panel ui system
sh run_control_panel.sh
```

You should see another app pop out in your browser that running on the port 3000
Then, we want to run a simple testing version of the system

```
# create a config file that has your system ip
# you can see your ip by "ifconfig | grep inet"
# choose your local ip, "192.168.1.107" etc
touch ~/config.txt
echo "$your_local_ip" > ~/config.txt

# run the docker container on your own machine
docker run -p 4000:80  -v  /Users:/Users -v ~/config.txt:/config.txt gaole/deeplearning-containe
```
You should see in the UI system that a new machine (container) has show up in the table list, click to the ```dashboard``` and send a python running script to it


