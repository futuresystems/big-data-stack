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
- [ ] [Python](https://www.python.org/)
  * [ ] [Pandas](http://pandas.pydata.org/)
  * [ ] [Scikit-learn](http://scikit-learn.org/stable/)
- [ ] [Tensorflow](https://www.tensorflow.org/)


## Data Processing Layer

- [X] [Hadoop MapReduce](https://hadoop.apache.org/docs/r1.2.1/mapred_tutorial.html)
- [X] [Spark](http://spark.apache.org/)
- [ ] [Tez](https://tez.apache.org/)
- [ ] [Hama](https://hama.apache.org/)
- [ ] [Storm](http://storm.apache.org/)
- [X] [Hive](https://hive.apache.org/)
- [X] [Pig](https://pig.apache.org/)
- [ ] [Flink](https://flink.apache.org/)

## Database Layer

- [X] [Drill](https://drill.apache.org/)
- [ ] [MongoDB](https://www.mongodb.org/)
- [ ] [CouchDB](http://couchdb.apache.org/)
- [X] [HBase](https://hbase.apache.org/)
- [X] [MySQL](https://www.mysql.com/)
- [ ] [PostgreSQL](https://www.mysql.com/)
- [ ] [Memcached](http://memcached.org/)
- [ ] [Redis](http://redis.io/)

## Scheduling

  * [X] [Zookeeper](http://zookeeper.apache.org/)
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


1. Make sure your public key is added to [github.com](https://github.com/settings/keys) **IMPORTANT** check the fingerprint `ssh-keygen -lf ~/.ssh/id_rsa` and make sure it is in your [list of keys](https://github.com/settings/keys)!
1. Download this repository using `git clone --recursive`. **IMPORTANT**: make sure you specify the `--recursive` option otherwise you will get errors.

     ```
      git clone --recursive https://github.com/futuresystems/big-data-stack.git
     ```
     
1. Install the requirements using `pip install -r requirements.txt`
1. Launch a virtual cluster and obtain the SSH-able IP addresses
1. Generate the inventory and variable files using `./mk-inventory`
   For example:
   
   ```
   ./mk-inventory -n $USER-mycluster 192.168.10{1,2,3,4} >inventory.txt
   ```
   
   Will define the inventory for a four-node cluster which nodes names
   as `$USER-myclusterN` (with `N` from `0..3`)
1. Make sure that `ansible.cfg` reflects your environment. Look
   especially at `remote_user` if you are not using Ubuntu. You can
   alternatively override the user by passing `-u $NODE_USERNAME` to
   the ansible commands.
1. Ensure `ssh_config` is to your liking.
1. Run `ansible all -m ping` to make sure all nodes can be managed.
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


# Upgrading

Whenever a new release is made, you can get the changes by either cloning a fresh repository (as above), or pulling changes from the upstream master branch and updating the submodules:

```
$ git pull https://github.com/futuresystems/big-data-stack master
$ git submodule update
$ pip install -U -r requirements.txt
```


# Examples

See the `examples` directory:

- `nist_fingerprint`: fingerprint analysis using Spark with results pushed to HBase


# License

Please see the `LICENSE` file in the root directory of the repository.


# Contributing

1. Fork the repository
1. Add yourself to the `CONTRIBUTORS.yml` file
1. Submit a pull request to the `unstable` branch
