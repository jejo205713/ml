#!/bin/bash

# ==============================
# Hadoop Single Node Setup Script
# Automates Hadoop 3.3.6 installation & WordCount
# ==============================

# Exit on error
set -e

echo "=== Updating Ubuntu packages ==="
sudo apt update -y
sudo apt install -y openjdk-8-jdk wget nano ssh pdsh

echo "=== Setting JAVA_HOME ==="
JAVA_HOME_PATH=$(readlink -f /usr/bin/java | sed "s:bin/java::")
echo "JAVA_HOME=$JAVA_HOME_PATH"

# Add environment variables to ~/.bashrc
echo "=== Configuring environment variables ==="
cat >> ~/.bashrc <<EOL

# Hadoop Environment
export JAVA_HOME=$JAVA_HOME_PATH
export HADOOP_HOME=\$HOME/hadoop
export PATH=\$PATH:\$HADOOP_HOME/bin:\$HADOOP_HOME/sbin
EOL

source ~/.bashrc

echo "=== Downloading Hadoop 3.3.6 ==="
cd $HOME
wget https://downloads.apache.org/hadoop/common/hadoop-3.3.6/hadoop-3.3.6.tar.gz
tar -xvzf hadoop-3.3.6.tar.gz
mv hadoop-3.3.6 hadoop

echo "=== Configuring Hadoop XML files ==="

# core-site.xml
cat > $HADOOP_HOME/etc/hadoop/core-site.xml <<EOL
<configuration>
  <property>
    <name>fs.defaultFS</name>
    <value>hdfs://localhost:9000</value>
  </property>
</configuration>
EOL

# hdfs-site.xml
cat > $HADOOP_HOME/etc/hadoop/hdfs-site.xml <<EOL
<configuration>
  <property>
    <name>dfs.replication</name>
    <value>1</value>
  </property>
</configuration>
EOL

# mapred-site.xml
cp $HADOOP_HOME/etc/hadoop/mapred-site.xml.template $HADOOP_HOME/etc/hadoop/mapred-site.xml
cat > $HADOOP_HOME/etc/hadoop/mapred-site.xml <<EOL
<configuration>
  <property>
    <name>mapreduce.framework.name</name>
    <value>yarn</value>
  </property>
</configuration>
EOL

# yarn-site.xml
cat > $HADOOP_HOME/etc/hadoop/yarn-site.xml <<EOL
<configuration>
  <property>
    <name>yarn.nodemanager.aux-services</name>
    <value>mapreduce_shuffle</value>
  </property>
</configuration>
EOL

echo "=== Formatting HDFS NameNode ==="
hdfs namenode -format

echo "=== Starting Hadoop services ==="
$HADOOP_HOME/sbin/start-dfs.sh
$HADOOP_HOME/sbin/start-yarn.sh

echo "=== Creating HDFS input directory ==="
hdfs dfs -mkdir -p /input

echo "=== Creating sample input file ==="
echo "Hadoop 3 MapReduce 2 Word 5" > $HOME/sample.txt
hdfs dfs -put -f $HOME/sample.txt /input

echo "=== Running WordCount example ==="
hadoop jar $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-examples-3.3.6.jar \
wordcount /input /output

echo "=== WordCount output ==="
hdfs dfs -cat /output/part-r-00000

echo "=== Hadoop Single Node Setup Complete ==="
