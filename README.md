# Big Data Analytics Stack

Provides a set of Ansible playbooks to deploy a Big Data analytics
stack on top of Hadoop/Yarn.

The `play-hadoop.yml` deploys the base system. Addons, such as Pig,
Spark, etc, are deployed using the playbooks in the `addons`
directory. A playbook for deploying all the addons is given in
`play-alladdons.yml`.


# Stack

- Analytics Layer
   * [ ] [BLAS](http://www.netlib.org/blas/)
   * [ ] [LAPACK](http://www.netlib.org/lapack/)
   * [ ] [LAPACKE](http://www.netlib.org/lapack/lapacke.html)
   * [ ] [Mahout](http://mahout.apache.org/)
   * [X] [MLlib](http://spark.apache.org/docs/latest/mllib-guide.html)
   * [ ] [MLbase](http://www.mlbase.org/)
   * [X] [Java](https://www.java.com/en/)
   * [ ] [R+libraries](https://cran.r-project.org/web/packages/available_packages_by_date.html)
   * [ ] [**_Python_**](https://www.python.org/)
      * [ ] [Pandas](http://pandas.pydata.org/)
      * [ ] [Scikit-learn](http://scikit-learn.org/stable/)
- Data Processing Layer
   * [X] [Hadoop MapReduce](https://hadoop.apache.org/docs/r1.2.1/mapred_tutorial.html)
   * [X] [Spark](http://spark.apache.org/)
   * [ ] [Tez](https://tez.apache.org/)
   * [ ] [Hama](https://hama.apache.org/)
   * [ ] [**_Storm_**](http://storm.apache.org/)
   * [ ] [Hive](https://hive.apache.org/)
   * [X] [Pig](https://pig.apache.org/)
   * [ ] [**_Flink_**](https://flink.apache.org/)
- Database Layer
    * [ ] [**_MongoDB_**](https://www.mongodb.org/)
    * [ ] [CouchDB](http://couchdb.apache.org/)
    * [ ] [HBase](https://hbase.apache.org/)
    * [ ] [**_MySQL_**](https://www.mysql.com/)
    * [ ] [PostgreSQL](https://www.mysql.com/)
    * [ ] [Memcached](http://memcached.org/)
    * [ ] [Redis](http://redis.io/)
- Scheduling:
  * [X] [YARN](https://hadoop.apache.org/docs/r2.7.1/hadoop-yarn/hadoop-yarn-site/FairScheduler.html)
  * [ ] [Mesos](http://mesos.apache.org/)
- Storage
  * [X] [HDFS](https://hadoop.apache.org/docs/r1.2.1/hdfs_design.html)
- Monitoring
  * [X] [Ganglia](http://ganglia.info/?p=88)


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


Sidenote: you may want to pass the `-f <N>` flag to `ansible-playbook` to use `N` parallel connections.
This will make the deployment go faster.
For example:

```
$ ansible-playbook -f $(egrep '^[a-zA-Z]' inventory.txt | sort | uniq | wc -l) # etc ...
```


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
