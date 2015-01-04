Title: A Laymans Guide to the "Big Data" Ecosystem
Date: 2014-11-06 12:11
Tags: juju, planet, hadoop, big-data-2
Slug: a-laymans-guide-to-the-big-data-ecosystem
Category: BigData
image: /images/2014/Nov/BigData_2267x1146_white.png

"Big Data" is now synonymous with marketing, and buzzword bingo. As a layman getting started in the ecosystem I found it truly difficult to really grasp what it was, and where I should be looking to get started. This will be the first post in a multi-post series breaking down the big-data stack, leveraging examples with Juju.

## Disambiguation of the term 'Hadoop'

I dont know about you but when I think "Big Data" - I think of one thing. The 800lb Gorilla in the room and that's **Hadoop**. It's become synonymous with crunching petabytes of data in the name of everything from medical research, market analysis, to crunching website results powering your favorite search engine and computing trends over long periods of time. But that's kind of a misnomer, as there is an entire ecosystem around this software; and I think Wikipedia has defined this better than I ever could:

> `Apache Hadoop` is an open-source software framework for distributed storage and distributed processing of Big Data on clusters of commodity hardware. Its Hadoop Distributed File System (HDFS) splits files into large blocks (default 64MB or 128MB) and distributes the blocks amongst the nodes in the cluster. For processing the data, the Hadoop Map/Reduce ships code (specifically Jar files) to the nodes that have the required data, and the nodes then process the data in parallel. This approach leverages data locality, in contrast to conventional HPC architecture which usually relies on a parallel file system (compute and data separated, but connected with high-speed networking).

Source: [Wikipedia](http://en.wikipedia.org/wiki/Apache_Hadoop)


So, in summation - Hadoop is really an ecosystem of applications and utilities (despite the core map-reduce engine being titled 'hadoop'). To further confuse and complicate things there are several vendors creating Hadoop application stacks.


- **Apache** - [Open Source Vanilla Hadoop](http://hadoop.apache.org/)
- **Cloudera** - [Cloudera Hadoop](http://www.cloudera.com/content/cloudera/en/home.html)
- **Hortonworks** - [Hortonworks Hadoop](http://hortonworks.com)
- **MapR** - [MapR Hadoop](https://www.mapr.com/)
- **Pivotal** - [Pivotal HD](http://www.pivotal.io/big-data/pivotal-hd)

How do you know which one to pick? "Which one makes **my** job easier?" you might ask. At the end of the day each vendor mixes in their own patches and special flavor of management on top of the Vanilla Apache Hadoop. Some give the patches back, some keep them proprietary to their distribution. It's all about preference, which approach appeals to you, and how much time you want to spend getting started. For the sake of brevity, and attention - I'll pick a middle of the road candidate and take a look at just the major applications in the stack and give illustrations using the Hortonworks flavor.


## Map Reduce Engines

### Hadoop
#### The core component(s)

![Dancing hadoop elephants](/images/2014/Nov/Hadoop_elephants.jpg)

The base Apache Hadoop framework (as of v2) is composed of the following modules:

`Hadoop Common` – contains libraries and utilities needed by other Hadoop modules.

`Hadoop Distributed File System (HDFS)` – a distributed file-system that stores data on commodity machines, providing very high aggregate bandwidth across the cluster.

`Hadoop YARN` – a resource-management platform responsible for managing compute resources in clusters and using them for scheduling of users' applications.

`Hadoop MapReduce` – a programming model for large scale data processing.

#### How to deploy Hadoop Core quickly with juju as a reference architecture

    juju quickstart bundle:hdp-core-batch-processing


![Hadoop Core Bundle Depiction from Juju](/images/2014/Nov/Selection_171-1.png)

### Tez
#### High Preformance Bach Processing Engine

![](/images/2014/Nov/ApacheTezLogo_lowres.png)

`Tez` generalizes the MapReduce paradigm to a more powerful framework based on expressing computations as a dataflow graph. Tez is not meant directly for end-users – in fact it enables developers to build end-user applications with much better performance and flexibility. Hadoop has traditionally been a batch-processing platform for large amounts of data. However, there are a lot of use cases for near-real-time performance of query processing. There are also several workloads, such as Machine Learning, which do not fit will into the MapReduce paradigm. Tez helps Hadoop address these use cases.

#### How to deploy Tez quickly with juju as a reference architecture

    juju quickstart bundle:high-performance-batch-processing

![Tez Bundle Depiction from Juju](/images/2014/Nov/Selection_172.png)

## Distributed Stream Processing

### Storm
#### Real Time Processing of Data Streams

![](/images/2014/Nov/storm_logo1.png)

Storm is a distributed computation framework written predominantly in the Clojure programming language. It uses custom created "spouts" and "bolts" to define information sources and manipulations to allow batch, distributed processing of streaming data.

A Storm application is designed as a topology in the shape of a [directed acyclic graph (DAG)](http://en.wikipedia.org/wiki/Directed_acyclic_graph) with spouts and bolts acting as the graph vertices. Edges on the graph are named streams, and direct data from one node to another. Together, the topology acts as a data transformation pipeline. At a superficial level the general topology structure is similar to a MapReduce job, with the main difference being that data is processed in real-time as opposed to in individual batches. Additionally, Storm topologies run indefinitely until killed, while a MapReduce job DAG must eventually end.


#### How to deploy Storm quickly with juju as a reference architecture

    juju quickstart bundle:realtime-analytics-with-storm


![Storm Bundle Depiction from Juju](/images/2014/Nov/Selection_170-1.png)

## Client Libraries and Supporting Applications for writing Map/Reduce

### Hive
#### Write Map/Reduce applications with a variant of SQL

![Hadoop Hive Logo](/images/2014/Nov/hive_logo.png)

Apache Hive is a data warehouse infrastructure built on top of Hadoop for providing data summarization, query, and analysis. Hive supports analysis of large datasets stored in Hadoop's HDFS and compatible file systems such as Amazon S3 filesystem. It provides an SQL-like language called HiveQL with schema on read and transparently converts queries to map/reduce, Apache Tez and in the future Spark jobs. All three execution engines can run in Hadoop YARN. To accelerate queries, it provides indexes, including bitmap indexes.


#### How to deploy Hive quickly with juju as a reference architecture

    juju quickstart bundle:data-analytics-with-sql-like


![Hive Bundle Depiction from Juju](/images/2014/Nov/Selection_169-1.png)

### Pig
#### The Rapid Latin Language of Big Data

![Pig the rapid map reduce writer](/images/2014/Nov/pig-on-elephant.png)

Pig is a high-level platform for creating MapReduce programs used with Hadoop. The language for this platform is called Pig Latin.Pig Latin abstracts the programming from the Java MapReduce idiom into a notation which makes MapReduce programming high level, similar to that of SQL for RDBMS systems. Pig Latin can be extended using User Defined Functions which the user can write in Java, Python, JavaScript, Ruby or Groovy and then call directly from the language.

#### How to deploy Pig quickly with juju as a reference architecture

    juju quickstart bundle:data-analytics-with-pig-latin


![Pig Bundle Depiction from Juju](/images/2014/Nov/Selection_168-2.png)

### Breaking down comprehension on Pig and Hive - and how they work in the ecosystem

![Diagram of Pig vs Hive - credit: http://www.bigdatatrendz.com/2013/10/introduction-to-apache-hive-and-pig.html](/images/2014/Nov/PigVsHive.png)


`Pig` and `Hive` both bundle client side application libraries, and deployed daemon components that bolt on additional functionality for the data scientist working with the data in HDFS or SQL tables. This allows a powerful combination for end-users to write map/reduce applications rapidly.

While they are not stand-alone entities in the hadoop bundle, they do provide a lower barrier to entry for end-users looking to get into the ecosystem without learning all the intricacies of learning Map/Reduce programming with just the core Hadoop stack.

Both of these applications communicate with the yarn-master to load a JIT compiled map/reduce application. `Hive` and `Pig` both have their own syntax, and translate the queries to a respective Map/Reduce jar that is then distributed to do the queries.


With the core components broken down - we're ready to take a look at the new kid on the block in the next post in the series:  **Spark for the layman**.
