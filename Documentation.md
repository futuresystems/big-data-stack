JAVA

What is JAVA and its purpose:

Java is a programming language and computing platform first released by Sun Microsystems in 1995. There are lots of applications and websites that will not work unless you have Java installed, and more are created every day. Java is fast, secure, and reliable. From laptops to datacenters, game consoles to scientific supercomputers, cell phones to the Internet, Java is everywhere!

Downloading and Installing JAVA on our local machines:

Always download the latest version of Java. The latest Java version contains important enhancements to improve performance, stability and security of the Java applications that run on your machine. Installing this free update will ensure that your Java applications continue to run safely and efficiently.

The Java Runtime Environment (JRE) is what you get when you download Java software. The JRE consists of the Java Virtual Machine (JVM), Java platform core classes, and supporting Java platform libraries. The JRE is the runtime portion of Java software, which is all you need to run it in your Web browser. The Java Virtual Machine is only one aspect of Java software that is involved in web interaction. The Java Virtual Machine is built right into your Java software download, and helps run Java applications. The Java Plug-in software is a component of the Java Runtime Environment (JRE). The JRE allows applets written in the Java programming language to run inside various browsers. The Java Plug-in software is not a standalone program and cannot be installed separately.

Java can be downloaded from the following link (depending on the type of operating system):
https://java.com/en/download/manual.jsp

•	Click on the appropriate operating system (32 or 64 bit) to start with the Java download
•	The File Download dialog box appears prompting you to run or save the download file 
•	To run the installer, click Run.
•	To save the file for later installation, click Save. 
•	Double-click on the saved file to start the installation process.
•	The installation process starts. Click the Install button to accept the license terms and to continue with the installation. 
•	Oracle has partnered with companies that offer various products. The installer may present you with option to install various other programs when you install Java. After ensuring that the desired programs are selected, click the Next button to continue the installation.
•	A few brief dialogs confirm the last steps of the installation process; click Close on the last dialog. This will complete Java installation process.  

Setting Environmental Variables:
On Windows:

Windows uses two flavors of Environment Variables (EVs): System EVs and User EVs. 
Assuming you have installed Java in c:\Program Files\java\jdk directory:

•	Right-click on 'My Computer' and select 'Properties'.
•	Click on the 'Environment variables' button under the 'Advanced' tab.
•	Now, alter the 'Path' variable so that it also contains the path to the Java executable. Example, if the path is currently set to 'C:\WINDOWS\SYSTEM32', then change your path to read 'C:\WINDOWS\SYSTEM32;c:\Program Files\java\jdk\bin'.

On Linux, Unix, Solaris and FreeBSD:
Environment variable PATH should be set to point to where the Java binaries have been installed. Refer to your shell documentation if you have trouble doing this.
Example, if you use bash as your shell, then you would add the following line to the end of your '.bashrc: export PATH=/path/to/java:$PATH'

General tutorial of Java is available at:
http://www.tutorialspoint.com/java/


References:

[1]. https://java.com/en/download/faq/whatis_java.xml
[2]. https://java.com/en/download/help/windows_manual_download.xml
[3]. http://www.tutorialspoint.com/java/java_environment_setup.htm

HADOOP MAPREDUCE

Hadoop MapReduce (Hadoop Map/Reduce) is a software framework for distributed processing of large data sets on compute clusters of commodity hardware. It is a sub-project of the Apache Hadoop project. The framework takes care of scheduling tasks, monitoring them and re-executing any failed tasks. 
According to The Apache Software Foundation, the primary objective of Map/Reduce is to split the input data set into independent chunks that are processed in a completely parallel manner.
The Hadoop MapReduce framework sorts the outputs of the maps, which are then input to the reduce tasks. Typically, both the input and the output of the job are stored in a file system.

HADOOP INSTALLATION:

Prerequisites: JAVA should be installed in the system

(On Ubuntu system)
Adding a dedicated Hadoop system user:
sudo addgroup hadoop_group
sudo adduser --ingroup hadoop_group hduser1
sudo adduser hduser1 sudo

Configuring SSH:
su – hduser1
ssh-keygen -t rsa -P ""
cat $HOME/.ssh/id_rsa.pub >> $HOME/.ssh/authorized_keys
ssh localhost

Installation:
su - hduser1
# Set Hadoop-related environment variables
export HADOOP_HOME=/usr/local/hadoop
# Add Hadoop bin/ directory to PATH
export PATH= $PATH:$HADOOP_HOME/bin

To understand the basics more clearly, and to play around with Hadoop, please goto the tutorial:
http://www.tutorialspoint.com/hadoop/hadoop_enviornment_setup.htm
http://www.alexjf.net/blog/distributed-systems/hadoop-yarn-installation-definitive-guide/

References:
[1]. http://doctuts.readthedocs.org/en/latest/hadoop.html
[2]. http://hadoop.apache.org/

HBase:

HBase  is a NoSQL database that runs on top of Hadoop as a distributed and scalable big data store. This means that HBase can leverage the distributed processing paradigm of the Hadoop Distributed File System (HDFS) and benefit from Hadoop’s MapReduce programming model. It is meant to host large tables with billions of rows with potentially millions of columns and run across a cluster of commodity hardware. But beyond its Hadoop roots, HBase is a powerful database in its own right that blends real-time query capabilities with the speed of a key/value store and offline or batch processing via MapReduce. In short, HBase allows you to query for individual records as well as derive aggregate analytic reports across a massive amount of data. 

HBase Installation:

Prerequisites: Java and Hadoop should be installed in the system

HBase Installation:
Choose a download site from this list of Apache Download Mirrors. Click on the suggested top link. This will take you to a mirror of HBase Releases. Click on the folder named stable and then download the file that ends in .tar.gz to your local filesystem; e.g. hbase-0.94.2.tar.gz.
$ tar xfz hbase-0.94.27.tar.gz
$cd hbase-0.94.27

At this point, you are ready to start HBase. But before starting it, edit conf/hbase-site.xml, the file you write your site-specific configurations into. Set hbase.rootdir, the directory HBase writes data to, andhbase.zookeeper.property.dataDir, the director ZooKeeper writes its data too:
<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<configuration>
  <property>
    <name>hbase.rootdir</name>
    <value>file:///DIRECTORY/hbase</value>
  </property>
  <property>
    <name>hbase.zookeeper.property.dataDir</name>
    <value>/DIRECTORY/zookeeper</value>
  </property>
</configuration>
Start HBase:
$ ./bin/start-hbase.sh

You can  find good tutorial on Hbase here:
http://www.tutorialspoint.com/hbase/hbase_installation.htm

References:
[1]. http://www.informit.com/articles/article.aspx?p=2253412
[2].  http://hbase.apache.org/0.94/book/quickstart.html

HDFS:

HDFS is a distributed file system that provides high-performance access to data across Hadoop clusters. Like other Hadoop-related technologies, HDFS has become a key tool for managing pools of big data and supporting big data analytics applications. Because HDFS typically is deployed on low-cost commodity hardware, server failures are common.
The file system is designed to be highly fault-tolerant, however, by facilitating the rapid transfer of data between compute nodes and enabling Hadoop systems to continue running if a node fails. That decreases the risk of catastrophic failure, even in the event that numerous nodes fail.
When HDFS takes in data, it breaks the information down into separate pieces and distributes them to different nodes in a cluster, allowing for parallel processing. 
The file system also copies each piece of data multiple times and distributes the copies to individual nodes, placing at least one copy on a different server rack than the others. As a result, the data on nodes that crash can be found elsewhere within a cluster, which allows processing to continue while the failure is resolved.
HDFS is built to support applications with large data sets, including individual files that reach into the terabytes. It uses a master/slave architecture, with each cluster consisting of a single NameNode that manages file system operations and supporting DataNodes that manage data storage on individual compute nodes.

HDFS Configuration on Hadoop:

The main HDFS configuration file is located at $HADOOP_PREFIX/etc/hadoop/hdfs-site.xml. If you've been following since the beginning, this file should be empty so it will use the default configurations outlined in this page.
For a single-node installation of HDFS you'll want to change hdfs-site.xml to have, at the very least, the following:
<configuration>
    <property>
        <name>dfs.datanode.data.dir</name>
        <value>file:///home/alex/Programs/hadoop-2.2.0/hdfs/datanode</value>
        <description>Comma separated list of paths on the local filesystem of a DataNode where it should store its blocks.</description>
    </property>

    <property>
        <name>dfs.namenode.name.dir</name>
        <value>file:///home/alex/Programs/hadoop-2.2.0/hdfs/namenode</value>
        <description>Path on the local filesystem where the NameNode stores the namespace and transaction logs persistently.</description>
    </property>
</configuration>

Make sure to replace /home/alex/Programs/hadoop-2.2.0 with whatever you set $HADOOP_PREFIX to. In addition, add the following to $HADOOP_PREFIX/etc/hadoop/core-site.xml to let the Hadoop modules know where the HDFS NameNode is located.
<configuration>
    <property>
        <name>fs.defaultFS</name>
        <value>hdfs://localhost/</value>
        <description>NameNode URI</description>
    </property>
</configuration>

Deploying HDFS on cluster is presented well in this tutorial:
http://www.cloudera.com/documentation/archive/cdh/4-x/4-2-0/CDH4-Installation-Guide/cdh4ig_topic_11_2.html

References:
http://searchbusinessanalytics.techtarget.com/definition/Hadoop-Distributed-File-System-HDFS
http://www.alexjf.net/blog/distributed-systems/hadoop-yarn-installation-definitive-guide/

SPARK:

Spark is an Apache project advertised as “lightning fast cluster computing”. It has a thriving open-source community and is the most active Apache project at the moment.
Spark provides a faster and more general data processing platform. Spark lets you run programs up to 100x faster in memory, or 10x faster on disk, than Hadoop. 
Last year, Spark took over Hadoop by completing the 100 TB Daytona GraySort contest 3x faster on one tenth the number of machines and it also became thefastest open source engine for sorting a petabyte.
Spark also makes it possible to write code more quickly as you have over 80 high-level operators at your disposal.
INSTALLING SPARK:

Prerequisites: Should have Java and Scala downloaded and installed

Downloading Scala:
Download spark from:
http://www.scala-lang.org/download/
Installing Scala:
$ tar xvf scala-2.11.6.tgz
Move Scala software files
Use the following commands for moving the Scala software files, to respective directory (/usr/local/scala).
$ su – 
Password: 
# cd /home/Hadoop/Downloads/ 
# mv scala-2.11.6 /usr/local/scala 
# exit
$ export PATH = $PATH:/usr/local/scala/bin

Download Spark from:
https://spark.apache.org/downloads.html

Installing SPARK:
$ tar xvf spark-1.3.1-bin-hadoop2.6.tgz 
$ su – 
Password:  

# cd /home/Hadoop/Downloads/ 
# mv spark-1.3.1-bin-hadoop2.6 /usr/local/spark 
# exit 
export PATH = $PATH:/usr/local/spark/bin
$ source ~/.bashrc

Verifying SPARK Installation:
$spark-shell

A good tutorial for SPARK can be found here :
http://www.tutorialspoint.com/apache_spark/

References:
[1]. https://docs.hortonworks.com/HDPDocuments/HDP2/HDP-2.3.0/bk_installing_manually_book/content/ch_installing_spark_chapter.html
[2]. http://www.tutorialspoint.com/apache_spark/apache_spark_installation.htm
[3]. https://www.toptal.com/spark/introduction-to-apache-spark

YARN:

YARN is one of the key features in the second-generation Hadoop 2 version of the Apache Software Foundation's open source distributed processing framework. Originally described by Apache as a redesigned resource manager, YARN is now characterized as a large-scale, distributed operating system for big data applications.
In 2012, YARN became a sub-project of the larger Apache Hadoop project. Sometimes called MapReduce 2.0, YARN is a software rewrite that decouples MapReduce's resource management and scheduling capabilities from the data processing component, enablingHadoop to support more varied processing approaches and a broader array of applications.
YARN combines a central resource manager that reconciles the way applications use Hadoop system resources with node manageragents that monitor the processing operations of individual cluster nodes.

Prerequisites: YARN requires that Apache Hadoop is already installed in the system and HDFS Configuration is done:

YARN Configuration:

YARN is the component responsible for allocating containers to run tasks, coordinating the execution of said tasks, restart them in case of failure, among other housekeeping. Just like HDFS, it also has 2 main components: a ResourceManager which keeps track of the cluster resources and NodeManagers in each of the nodes which communicates with the ResourceManager and sets up containers for execution of tasks.
To configure YARN, the relevant file is $HADOOP_PREFIX/etc/hadoop/yarn-site.xml. The file should currently be empty which means it's using the default configurations you can find here. For a single-node installation of YARN you'll want to add the following to that file:


<configuration>
    <property>
        <name>yarn.scheduler.minimum-allocation-mb</name>
        <value>128</value>
        <description>Minimum limit of memory to allocate to each container request at the Resource Manager.</description>
    </property>
    <property>
        <name>yarn.scheduler.maximum-allocation-mb</name>
        <value>2048</value>
        <description>Maximum limit of memory to allocate to each container request at the Resource Manager.</description>
    </property>
    <property>
        <name>yarn.scheduler.minimum-allocation-vcores</name>
        <value>1</value>
        <description>The minimum allocation for every container request at the RM, in terms of virtual CPU cores. Requests lower than this won't take effect, and the specified value will get allocated the minimum.</description>
    </property>
    <property>
        <name>yarn.scheduler.maximum-allocation-vcores</name>
        <value>2</value>
        <description>The maximum allocation for every container request at the RM, in terms of virtual CPU cores. Requests higher than this won't take effect, and will get capped to this value.</description>
    </property>
    <property>
        <name>yarn.nodemanager.resource.memory-mb</name>
        <value>4096</value>
        <description>Physical memory, in MB, to be made available to running containers</description>
    </property>
    <property>
        <name>yarn.nodemanager.resource.cpu-vcores</name>
        <value>4</value>
        <description>Number of CPU cores that can be allocated for containers.</description>
    </property>
</configuration>

Staring YARN:

## Start HDFS daemons
# Format the namenode directory (DO THIS ONLY ONCE, THE FIRST TIME)
$HADOOP_PREFIX/bin/hdfs namenode -format
# Start the namenode daemon
$HADOOP_PREFIX/sbin/hadoop-daemon.sh start namenode
# Start the datanode daemon
$HADOOP_PREFIX/sbin/hadoop-daemon.sh start datanode

## Start YARN daemons
# Start the resourcemanager daemon
$HADOOP_PREFIX/sbin/yarn-daemon.sh start resourcemanager
# Start the nodemanager daemon
$HADOOP_PREFIX/sbin/yarn-daemon.sh start nodemanager

A good video tutorial for Hadoop and YARN can be found here:
http://www.edureka.co/blog/apache-hadoop-2-0-and-yarn/

References:
[1]. http://searchdatamanagement.techtarget.com/definition/Apache-Hadoop-YARN-Yet-Another-Resource-Negotiator
[2]. http://www.alexjf.net/blog/distributed-systems/hadoop-yarn-installation-definitive-guide/


Ganglia Monitoring System:

Ganglia is a scalable distributed monitoring system for high-performance computing systems such as clusters and Grids. It is based on a hierarchical design targeted at federations of clusters. It leverages widely used technologies such as XML for data representation, XDR for compact, portable data transport, and RRDtool for data storage and visualization. It uses carefully engineered data structures and algorithms to achieve very low per-node overheads and high concurrency. The implementation is robust, has been ported to an extensive set of operating systems and processor architectures, and is currently in use on thousands of clusters around the world. It has been used to link clusters across university campuses and around the world and can scale to handle clusters with 2000 nodes.

It has three main components: gmond, gmetad and ganglia web frontend.
Gmond: It is a monitoring daemon of Ganglia which collects the monitoring data from node and sends them to the configured host. It is configurable to send the monitoring data to as many hosts as you want. It also has the functionality to receive the monitoring data from the other gmond daemons.
Gmetad: The Ganglia Meta Daemon (gmetad) gathers the metrics from gmond nodes that sends the monitoring data and writes them in the round robin database. Ganglia uses the round robin database (rrd) to store the monitoring data. It is configurable to collect the monitoring data from any number of clusters.
Ganglia web interface: Web interface presents monitoring data in graphical form for cluster as well as node level. At cluster level it shows the aggregated graphs of CPU, Memory, Network and Disk. At node level it shows the aggregated graphs of standard system metrics. Additionally, it also shows the individual graphs for system as well as technology specific metrics.
Installing Ganglia:

sudo apt-get install ganglia-monitor rrdtool gmetad ganglia-webfrontend
sudo cp /etc/ganglia-webfrontend/apache.conf /etc/apache2/sites-enabled/ganglia.conf
sudo apt-get install ganglia-monitor

Configuring Ganglia:

Configuring Gmond:

Gmond can be configured by updating the cluster section, udp send section and udp recv section in gmond configuration file. Let’s understand the configuration process by taking an example of a cluster of two nodes; host1 as the head node and host2 as the gmond node only. Configure the gmond configuration file for host1 using the configuration as shown below.

globals {
   daemonize = yes
   setuid = yes
   user = nobody      /* Ganglia User */
   debug_level = 0
   max_udp_msg_len = 1472
   mute = no
   deaf = no
   allow_extra_data = yes
   host_dmax = 0 /*secs */
   cleanup_threshold = 300 /*secs */
   gexec = no
   send_metadata_interval = 30
}
cluster {
  name = "myCluster"
  owner = "clusterOwner"
  latlong = "unspecified"
  url = "unspecified"
}
udp_send_channel {
  host = host1
  port = 8649
  ttl = 1
}
udp_recv_channel {
  port = 8649
}
tcp_accept_channel {
  port = 8649
}

Configuring Gmetad:
The Gmetad file can be configured by providing the inputs in the data source code section. Provide the following inputs as shown in a sample code section below:
•	Cluster name
•	Poling interval
•	Host name of head node with gmond port
data_source "myCluster" 15 host1:8649
 setuid_username "nobody"

Step 3 - Running Ganglia:
There are two services called gmond and gmetad. Use the below commands to start the gmetad and gmond services.
Run the “sudo service gmetad start” command where gmetad is installed while run the “sudo service ganglia-monitor start” command where gmond is installed.
Starting Apache Server:
Run the below command to start the Apache server on the node where ganglia web frontend application is installed.
sudo service apache2 start

Once you are done with the above installation and configuration procedure, you can access the ganglia throughhttp://host1/ganglia URL.


A good tutorial for Ganglia is available at:
http://blogs.impetus.com/big_data/big_data_technologies/GangliaMonitoringTool.do
http://www.slideshare.net/Fastly/monitoring-with-ganglia

References:
[1]. http://blogs.impetus.com/big_data/big_data_technologies/GangliaMonitoringTool.do
[2]. http://ganglia.info/

PIG:

Apache Pig is a platform for analyzing large data sets that consists of a high-level language for expressing data analysis programs, coupled with infrastructure for evaluating these programs. The salient property of Pig programs is that their structure is amenable to substantial parallelization, which in turns enables them to handle very large data sets.
At the present time, Pig's infrastructure layer consists of a compiler that produces sequences of Map-Reduce programs, for which large-scale parallel implementations already exist (e.g., the Hadoop subproject). Pig's language layer currently consists of a textual language called Pig Latin, which has the following key properties:
•	Ease of programming. It is trivial to achieve parallel execution of simple, "embarrassingly parallel" data analysis tasks. Complex tasks comprised of multiple interrelated data transformations are explicitly encoded as data flow sequences, making them easy to write, understand, and maintain.
•	Optimization opportunities. The way in which tasks are encoded permits the system to optimize their execution automatically, allowing the user to focus on semantics rather than efficiency.
•	Extensibility. Users can create their own functions to do special-purpose processing

Requirements
Unix and Windows users need the following:
1.	Hadoop 0.20.2 - http://hadoop.apache.org/common/releases.html
2.	Java 1.6 - http://java.sun.com/javase/downloads/index.jsp (set JAVA_HOME to the root of your Java installation)
3.	Ant 1.7 - http://ant.apache.org/ (optional, for builds)
4.	JUnit 4.5 - http://junit.sourceforge.net/ (optional, for unit tests)
Windows users need to install Cygwin and the Perl package: http://www.cygwin.com/

Download Pig

To get a Pig distribution, download a recent stable release from one of the Apache Download Mirrors (see Pig Releases).
Unpack the downloaded Pig distribution. The Pig script is located in the bin directory (/pig-n.n.n/bin/pig).
Add /pig-n.n.n/bin to your path. Use export (bash,sh,ksh) or setenv (tcsh,csh). For example:
$ export PATH=/<my-path-to-pig>/pig-n.n.n/bin:$PATH
Try the following command, to get a list of Pig commands:
$ pig -help
Try the following command, to start the Grunt shell:
$ pig 

Run Modes
Pig has two run modes or exectypes:
•	Local Mode - To run Pig in local mode, you need access to a single machine.
•	Mapreduce Mode - To run Pig in mapreduce mode, you need access to a Hadoop cluster and HDFS installation. Pig will automatically allocate and deallocate a 15-node cluster.
You can run the Grunt shell, Pig scripts, or embedded programs using either mode.

Grunt Shell
Use Pig's interactive shell, Grunt, to enter pig commands manually. See the Sample Code for instructions about the passwd file used in the example.
You can also run or execute script files from the Grunt shell. See the run and exec commands.
Local Mode
$ pig -x local

Mapreduce Mode
$ pig
or
$ pig -x mapreduce

For either mode, the Grunt shell is invoked and you can enter commands at the prompt. The results are displayed to your terminal screen (if DUMP is used) or to a file (if STORE is used).
grunt> A = load 'passwd' using PigStorage(':'); 
grunt> B = foreach A generate $0 as id; 
grunt> dump B; 
grunt> store B; 

Script Files
Use script files to run Pig commands as batch jobs. See the Sample Code for instructions about the passwd file and the script file (id.pig) used in the example.

Local Mode
$ pig -x local id.pig

Mapreduce Mode
$ pig id.pig
or
$ pig -x mapreduce id.pig
For either mode, the Pig Latin statements are executed and the results are displayed to your terminal screen (if DUMP is used) or to a file (if STORE is used).

A good tutorial of PIG can be found at:
https://pig.apache.org/docs/r0.7.0/tutorial.html
http://www.tutorialspoint.com/apache_pig/index.htm

References:
[1]. https://pig.apache.org/docs/r0.7.0/setup.html
[2]. https://pig.apache.org/


