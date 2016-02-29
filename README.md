# Big Data Analytics Stack

Provides a set of Ansible playbooks to deploy a Big Data analytics
stack on top of Hadoop/Yarn.

The `play-hadoop.yml` deploys the base system. Addons, such as Pig,
Spark, etc, are deployed using the playbooks in the `addons`
directory. A playbook for deploying all the addons is given in
`play-alladdons.yml`.


# Stack

1. Analytics Layer
   1. [ ] BLAS
   1. [ ] LAPACK
   1. [ ] Mahout
   1. [ ] MLlib
   1. [ ] MLbase
   1. [ ] R+libraries
   1. [ ] Python
      1. [ ] Pandas
      1. [ ] Scikit-learn
1. Data Processing Layer
   1. [X] Hadoop MapReduce
   1. [X] Spark
   1. [ ] Tez
   1. [ ] Hama
   1. [ ] Storm
   1. [ ] Hive
   1. [ ] Pig
   1. [ ] Flink
1. Database Layer
    1. [ ] MongoDB
    1. [ ] CouchDB
    1. [ ] HBase
    1. [ ] MySQL
    1. [ ] PostgreSQL
    1. [ ] Memcached
    1. [ ] Redis
1. [X] Scheduling: YARN
1. [X] Storage: HDFS
1. [X] Monitoring: Ganglia


# Usage

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
1. Run `ansible-playbook plays-hadoop.yml` to install the base system
1. Run `ansible-playbook addons/{pig,spark}.yml # etc` to install the
   Pig and Spark addons.


# License

Please see the `LICENSE` file in the root directory of the repository.


# Contributing

1. Fork the repository
1. Add yourself to the `CONTRIBUTORS.yml` file
1. Submit a pull request to the `unstable` branch
