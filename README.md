# Big Data Analytics Stack

Provides a set of Ansible playbooks to deploy a Big Data analytics
stack on top of Hadoop/Yarn.

The `play-hadoop.yml` deploys the base system. Addons, such as Pig,
Spark, etc, are deployed using the playbooks in the `addons`
directory. A playbook for deploying all the addons is given in
`play-alladdons.yml`.


# Stack

Legend:
  - [X] available
  - [ ] **_ItaliBold_**: work-in-progress
  - [ ] planned


## Analytics Layer

- [X] [BLAS](http://www.netlib.org/blas/)
- [X] [LAPACK](http://www.netlib.org/lapack/)
- [X] [LAPACKE](http://www.netlib.org/lapack/lapacke.html)
- [ ] [Mahout](http://mahout.apache.org/)
- [X] [MLlib](http://spark.apache.org/docs/latest/mllib-guide.html)
- [ ] [MLbase](http://www.mlbase.org/)
- [X] [Java](https://www.java.com/en/)
- [ ] [R+libraries](https://cran.r-project.org/web/packages/available_packages_by_date.html)
- [ ] [**_Python_**](https://www.python.org/)
  * [ ] [Pandas](http://pandas.pydata.org/)
  * [ ] [Scikit-learn](http://scikit-learn.org/stable/)


## Data Processing Layer

- [X] [Hadoop MapReduce](https://hadoop.apache.org/docs/r1.2.1/mapred_tutorial.html)
- [X] [Spark](http://spark.apache.org/)
- [ ] [Tez](https://tez.apache.org/)
- [ ] [Hama](https://hama.apache.org/)
- [ ] [**_Storm_**](http://storm.apache.org/)
- [ ] [Hive](https://hive.apache.org/)
- [X] [Pig](https://pig.apache.org/)
- [ ] [**_Flink_**](https://flink.apache.org/)

## Database Layer

- [ ] [**_MongoDB_**](https://www.mongodb.org/)
- [ ] [CouchDB](http://couchdb.apache.org/)
- [X] [HBase](https://hbase.apache.org/)
- [ ] [**_MySQL_**](https://www.mysql.com/)
- [ ] [PostgreSQL](https://www.mysql.com/)
- [ ] [Memcached](http://memcached.org/)
- [ ] [Redis](http://redis.io/)

## Scheduling

  * [X] [YARN](https://hadoop.apache.org/docs/r2.7.1/hadoop-yarn/hadoop-yarn-site/FairScheduler.html)
  * [ ] [Mesos](http://mesos.apache.org/)

## Storage

  * [X] [HDFS](https://hadoop.apache.org/docs/r1.2.1/hdfs_design.html)

## Monitoring

  * [X] [Ganglia](http://ganglia.info/?p=88)


# Usage

1. Make sure to start an ssh-agent so you don't need to retype you passphrase multiple times.
We've also noticied that if you are running on `india`, Ansible may be unable to access the node and complain with something like:

   ```
   master0 | UNREACHABLE! => {
       "changed": false,
       "msg": "ssh cc@129.114.110.126:22 : Private key file is encrypted\nTo connect as a different user, use -u <username>.",
       "unreachable": true
   }
   ```


   To start the agent:

   ```
   badi@i136 ~$ eval $(ssh-agent)
   badi@i136 ~$ ssh-add
   ```


1. Make sure your public key is added to [github.com](https://github.com/settings/keys)
1. Download this repository using `git clone --recursive`. **IMPORTANT**: make sure you specify the `--recursive` option otherwise you will get errors.::

      git clone --recursive https://github.com/futuresystems/big-data-stack.git

1. Install the requirements using `pip install -r requirements.txt`
1. Edit `.cluster.py` to define the machines in the cluster.
1. Launch the cluster using `vcl boot -p openstack -P $USER-` This
   will start the machines on whatever openstack environment is
   currently available (via the `$OS_PROJECT_NAME`, `$OS_AUTH_URL`,
   etc), prefixing `$USER-` to the name of each VM (eg. `zk0` becomes
   `badi-zk0`).
1. Make sure that `ansible.cfg` reflects your environment. Look
   especially at `remote_user` if you are not using Ubuntu.
1. Ensure `ssh_bastion_config` is to your liking (it assumes you are
   using the openstack cluster on FutureSystems).
1. Run `ansible all -m ping` to make sure all nodes can be managed.
1. ~~Define `zookeeper_id` for each zookeeper node. Adapt the following:~~ (**NO LONGER NEEDED as of v0.2.4**)

    ```
    mkdir host_vars
    for i in 0 1 2; do
      echo "zookeeper_id: $(( i+1 ))" > host_vars/master$i
    done
    ```

1. Run `ansible-playbook play-hadoop.yml` to install the base system
1. Run `ansible-playbook addons/{pig,spark}.yml # etc` to install the
   Pig and Spark addons.
1. Log into the frontend node (see the `[frontends]` group in the inventory) and use the `hadoop` user (`sudo su - hadoop`) to run jobs on the cluster.


Sidenote: you may want to pass the `-f <N>` flag to `ansible-playbook` to use `N` parallel connections.
This will make the deployment go faster.
For example:

```
$ ansible-playbook -f $(egrep '^[a-zA-Z]' inventory.txt | sort | uniq | wc -l) # etc ...
```

The `hadoop` user is present on all the nodes and is the hadoop administrator.
If you need to change anything on HDFS, it must be done as `hadoop`.


# Access

`vcl ssh` can be used as shorthand to access the nodes.
It looks up the ip address in the generated .machines.yml, using the floating ip if available.

# Monitoring

You can access the Ganglia display on the monitoring node.
The interface is kept local to the virtual cluster so you need log in with X forwarding enable and install a browser.
For example:

```
[badi@india]: ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no ubuntu@123.45.67.89 -X
[ubuntu@master2]: sudo apt-get -y install firefox
[ubuntu@master2]: firefox http://localhost/ganglia
```


# Upgrading

Whenever a new release is made, you can get the changes by either cloning a fresh repository (as above), or pulling changes from the upstream master branch and updating the submodules:

```
$ git pull https://github.com/futuresystems/big-data-stack master
$ git submodule update
$ pip install -U -r requirements.txt
```


# Examples

See the `examples` directory:

- `nist_finterprint`: fingerprint analysis using Spark with results pushed to HBase


# License

Please see the `LICENSE` file in the root directory of the repository.


# Contributing

1. Fork the repository
1. Add yourself to the `CONTRIBUTORS.yml` file
1. Submit a pull request to the `unstable` branch


<!-- # Stack Components -->

<!-- This is a list of the components with the associated information: -->
<!-- - description of purpose -->
<!-- - summary of general usage -->
<!-- - references (with links) to any scientific publications by the authors -->
<!-- - official documentation -->
<!-- - links to third party tutorials and demonstrations -->

<!-- The name of the technology should link to the project webpage -->
