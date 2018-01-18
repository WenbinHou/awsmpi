
# awsmpi

## Overview

`awsmpi` allows you to create/start/stop/terminate an MPI cluster on AWS.

### Installation

Use `pip`. Python2 and Python3 are both OK.

````bash
pip install awsmpi
````

### Before you use it:

Before using awsmpi, you must login AWS with `aws configure` and set your account information properly:
- AWS Access Key ID
- AWS Secret Access Key
- Region (e.g. `cn-north-1`)

### Node information

As you create a cluster named `<name>` with `N` nodes, their hostnames will be: `<name>-1` `<name>-2` ... `<name>-N` respectively.

`<name>-1` is the master node and will be assigned an immutable public IP (AWS elastic IP). You are supported to SSH into this node.

As for MPI, `/etc/hostfile` stores all nodes' hostnames. Detailed information about MPI *hostfile* could be found in [OpenMPI documentation](https://www.open-mpi.org/faq/?category=running#mpirun-hostfile).

## Commands

### 1. Create an MPI cluster

````bash
awsmpi create <name> <node-count> <vm-type> <shared-volume-size>
````

- *\<name\>*: name of your cluster
- *\<node-count\>*: number of nodes
- *\<vm-type\>*: type of instance, like `c3.xlarge`
- *\<shared-volume-size\>*: size of shared volume in GB. At least 4 GB.

When creating a cluster, all nodes will be put to one placement-group if supported.
<br>**(Some types of instances do not support placement-group!)**

### 2. SSH to the cluster

After you create a cluster with *\<name\>*, you may login the first node (also the master node).

````bash
# The password is "ubuntu" (without quotes)
# You may change the password if you desire.

ssh ubuntu@<master-node-ip>
````

### 3. Start/Stop the cluster

Have you created the cluster, you could start/stop it by:

````bash
awsmpi start <name>
awsmpi stop <name>
````

Freshly created cluster will be started automatically.

**Remember to stop your cluster in time!**

### 4. Show cluster information

Use the following command to show the cluster information.

The information contains number of nodes, master node IP, current status (started/stopped), and so on.

````bash
# They are identical
awsmpi show <name>
awsmpi describe <name>
````

### 5. Terminate the cluster

If you don't need the cluster any more, you should terminate it:

````bash
awsmpi terminate <name>
````

This will delete the cluster permanently.

## Data Persistence

### 1. Cluster-shared data: **/share**

Cluster-shared data is mounted at `/share` (GlusterFS).

These data are persistent across cluster's stop & (re)start.

**However, when terminating a cluster, these data are permanently lost.**

### 2. Permanent data: **/permanent**

Permanent data is mounted at `/permanent` (GlusterFS).

Data in this directory will be persisted even if a cluster terminates.

**HOW TO USE IT: Before you terminate a cluster, you may copy your data into `/permanent`. After creating a new cluster, copy your data out from `/permanent`. This is extremely slow, just for data persistence across clusters! Do not directly read from or write to this directory in normal use!**

**NOTE: This directory is shared by everyone. Don't touch others' data!**
