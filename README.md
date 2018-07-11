# Workload Autonamous Distribution System

This is the repo for the workload autonamous distribution system for an edge computing system. The system will take the upcoming request from the user or other machine end to distribute the task to the edge nodes. The nodes with the same functionability can form as a cluster of machine. 

## Getting Started

The system is computing of three parts:

- Distributor: Responsible for the distribution of tasks and monitor of the edge nodes' status
- Edge Clusters: The collection of machine and software replica that resides on the machine.
- Control Dashboard: A UI system to call the api on the distributor and distribute task and monitor the ndoes.

### Prerequisites

Before using our system, you need to install the ```docker```