# Big Data Analytics Stack

Provides a set of Ansible playbooks to deploy a Big Data analytics
stack on top of Hadoop/Yarn.

The `play-hadoop.yml` deploys the base system. Addons, such as Pig,
Spark, etc, are deployed using the playbooks in the `addons`
directory. A playbook for deploying all the addons is given in
`play-alladdons.yml`.


# Stack

- Analytics Layer
   * [ ] BLAS
   * [ ] LAPACK
   * [ ] Mahout
   * [ ] **_MLlib_**
   * [ ] MLbase
   * [X] Java
   * [ ] R+libraries
   * [ ] **_Python_**
      * [ ] Pandas
      * [ ] Scikit-learn
- Data Processing Layer
   * [X] Hadoop MapReduce
   * [X] Spark
   * [ ] Tez
   * [ ] Hama
   * [ ] **_Storm_**
   * [ ] Hive
   * [X] Pig
   * [ ] **_Flink_**
- Database Layer
    * [ ] **_MongoDB_**
    * [ ] CouchDB
    * [X] HBase
    * [ ] **_MySQL_**
    * [ ] PostgreSQL
    * [ ] Memcached
    * [ ] Redis
- Scheduling:
  * [X] YARN
  * [ ] Mesos
- Storage
  * [X] HDFS
- Monitoring
  * [X] Ganglia


# Usage

1. Download this repository using `git clone --recursive`.
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
1. Define `zookeeper_id` for each zookeeper node. Adapt the following:

    ```
    mkdir host_vars
    for i in 0 1 2; do
      echo "zookeeper_id: $(( i+1 ))" >host_vars/zk$i`
    done
    ```

1. Run `ansible-playbook plays-hadoop.yml` to install the base system
1. Run `ansible-playbook addons/{pig,spark}.yml # etc` to install the
   Pig and Spark addons.


# License

Please see the `LICENSE` file in the root directory of the repository.


# Contributing

1. Fork the repository
1. Add yourself to the `CONTRIBUTORS.yml` file
1. Submit a pull request to the `unstable` branch


# Stack Components

<!-- This is a list of the components with the associated information: -->
<!-- - description of purpose -->
<!-- - summary of general usage -->
<!-- - references (with links) to any scientific publications by the authors -->
<!-- - official documentation -->
<!-- - links to third party tutorials and demonstrations -->

<!-- The name of the technology should link to the project webpage -->
