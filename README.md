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

# build the container for deep learning locally
cd deep-learning-container
docker build -t gaole/deeplearning-container .
cd ..

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

This is a single edge node demo version, so we directly run a docker container on the same machine with the central server, to submit a job to this node, we can prepare a zip file of a python script with the file that this python file needs.

We have prepared this for you in the project folder

```
# the python script zip file is "./UnitTest/Archive.zip"
# This zip file include ["app.py", "run.sh"]
# app.py is a simple linear regression script
# run.sh is a bash script to run the python file
# open UI interface, write "sh ./run.sh" in the text field
# and submit the zip file
# After several seconds, the output should show up in "./centralServer/static/model/_stdout.txt"

# after task finish
cat ./centralServer/static/model/_stdout.txt
```

### TODO

List of things waiting to be done to the system

1. Verify and finish the user and system api format (specify what we can provide, and what the user need to provide in a programmatical way)
2. Change docker swarm to kubernetes, so the method of create cluster with docker-swarm is not listed here. (Or use both)
3. Create other container edge node for other usage, like media processing.
