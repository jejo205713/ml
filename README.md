# ml

## GAE Download Link : 
```
https://www.npackd.org/p/com.google.AppEnginePythonSDK/1.9.62
```
Download python 2.7.9


Experiment No 1 :Installation of VirtualBox/VMware Workstation with
Multiple OS Flavours on Windows 7/8
AIM:
To install VirtualBox or VMware Workstation on Windows 7/8 and set up virtual machines
with different flavours of Linux (e.g., Ubuntu, Fedora) or Windows OS.
BACKGROUND THEORY:
Virtualization allows multiple operating systems to run on a single physical machine by
sharing hardware resources. Two main software used for virtualization are:
 Oracle VirtualBox (Free, Open-source)
 VMware Workstation (Proprietary, Paid with a free version available - VMware
Workstation Player)
Benefits of Virtualization:
 Run multiple OSs simultaneously
 Ideal for testing, development, and educational use
 Isolation between guest and host OS
 No need for dual booting
Software Required:
S. No Software Version
1 Host OS (Windows 7/8) 64-bit
2 Oracle VirtualBox or VMware Latest
3 ISO File for Linux/Windows Ubuntu 22.04 / Fedora / Windows 10 ISO
Algorithm / Steps:
Step 1: Install Virtualization Software
1. Download VirtualBox from https://www.virtualbox.org
OR
Download VMware Workstation Player from https://www.vmware.com
2. Run the installer and follow the on-screen instructions to complete the installation.
Step 2: Create a New Virtual Machine
1. Open VirtualBox or VMware.
2. Click New VM.
3. Give a name (e.g., Ubuntu_VM), select type (Linux/Windows), and version.
4. Allocate RAM (Recommended: 2048 MB for Linux, 4096 MB for Windows).
5. Create a virtual hard disk (10–30 GB recommended).
6. Choose hard disk file type (VDI for VirtualBox or VMDK for VMware).
7. Proceed with a dynamically allocated or fixed size disk.
Step 3: Mount ISO and Start Installation
1. In VM settings, mount the downloaded ISO file under "Optical Drive".
2. Start the virtual machine.
3. Follow the OS installation steps (like a real PC).
Step 4: Post-Installation Setup
1. Install Guest Additions (VirtualBox) or VMware Tools for better performance and
shared clipboard.
2. Customize screen resolution, networking, and shared folders if needed.
Code
# Create VM
VBoxManage createvm --name "UbuntuVM" --ostype Ubuntu_64 --register
# Set memory and boot
VBoxManage modifyvm "UbuntuVM" --memory 2048 --boot1 dvd --nic1 nat
# Create virtual disk
VBoxManage createhd --filename "UbuntuVM.vdi" --size 20000
# Attach storage
VBoxManage storagectl "UbuntuVM" --name "SATA Controller" --add sata --controller
IntelAhci
VBoxManage storageattach "UbuntuVM" --storagectl "SATA Controller" --port 0 --device 0
--type hdd --medium "UbuntuVM.vdi"
VBoxManage storageattach "UbuntuVM" --storagectl "SATA Controller" --port 1 --device 0
--type dvddrive --medium "ubuntu-22.04.iso"
# Start VM
VBoxManage startvm "UbuntuVM"
Screenshots
1. VirtualBox/VMware installation screen
2. New VM creation steps
3. ISO mounting and OS installation
4. Running guest OS inside the VM
Result:
Successfully installed and configured VirtualBox/VMware Workstation on Windows 7/8 and
ran multiple virtual machines with different OS flavours like Ubuntu and Windows 10.
Pre-Viva Questions
1. State the purpose of using virtualization tools like VirtualBox or VMware.
2. Mention the advantages of installing multiple OS flavours on a single host system.
3. Describe the difference between a host OS and a guest OS.
4. List common OS flavours that can be installed on virtual machines.
5. Explain the basic system requirements for running a virtual machine efficiently.
6. Identify the steps involved in creating a new virtual machine.
Post-Viva Questions
1. Share your experience in installing and configuring a guest operating system.
2. Describe the settings you configured while creating the virtual machine (e.g., RAM,
disk).
3. Mention how you enabled networking in the guest OS.
4. Explain how multiple OSes can coexist without affecting the host machine.
5. Suggest use cases where virtual machines are better than dual boot.
6. Reflect on any difficulties you faced during installation and how you resolved them.
Experiment No 2:Installation of a C Compiler in a Virtual Machine Using
Virtual Box and Execution of Simple C Programs
AIM:
To install a C compiler (such as gcc) in a Linux virtual machine created using VirtualBox
and execute basic C programs.
BACKGROUND THEORY:
The C programming language is a foundational language for system and application
development. To compile and run C programs in a Linux environment, we use the GCC (GNU
Compiler Collection).
WHAT IS GCC?
 GCC is a compiler system produced by the GNU Project supporting various
programming languages.
 It is the standard compiler for most Unix-like systems.
VirtualBox + Linux + GCC = Portable Development Environment
Using a VM helps you test, code, and debug in a safe, isolated, and consistent environment.
SOFTWARE REQUIRED:
S. No Software Version
1 Oracle VirtualBox Latest
2 Ubuntu / Fedora ISO Ubuntu 22.04 LTS
3 GCC Compiler Preinstalled or installable via package manager
4 Terminal / Code Editor Gedit, nano, or VS Code (optional)
ALGORITHM / STEPS:
Step 1: Start Your Linux VM
 Open VirtualBox.
 Select your Linux virtual machine and click Start.
Step 2: Open Terminal
 Once the Linux desktop loads, press Ctrl + Alt + T to open the terminal.
Step 3: Update Package Repository
sudo apt update
For Fedora:
sudo dnf update
Step 4: Install GCC Compiler
For Ubuntu/Debian-based systems:
sudo apt install build-essential
For Fedora-based systems:
sudo dnf groupinstall "Development Tools"
Step 5: Verify GCC Installation
gcc --version
Output should show installed version like:
gcc (Ubuntu 11.4.0) 11.4.0
Step 6: Write and Execute a Simple C Program
Code: Hello World in C
1. Create a C file using any text editor:
nano hello.c
2. Paste the following code:
#include <stdio.h>
int main() {
 printf("Hello, Virtual Machine World!\n");
 return 0;
}
3. Save and Exit (Ctrl + O, Enter, then Ctrl + X)
Step 7: Compile the Program
gcc hello.c -o hello
This will create an output file hello.
Step 8: Run the Executable
./hello
Expected Output:
Hello, Virtual Machine World!
Output Screenshots :
1. Terminal showing gcc --version
2. Code written in editor (nano or gedit)
3. Output of the compiled C program
Result:
Successfully installed GCC in the Linux virtual machine, compiled, and executed a basic C
program.
Pre-Viva Questions
1. State the steps involved in setting up a virtual machine in VirtualBox.
2. Mention the importance of installing a C compiler inside a virtual environment.
3. Describe common C compilers available for Linux distributions.
4. List Linux commands used to install software packages from the terminal.
5. Identify basic components required to compile and run a C program.
6. Explain why VirtualBox is preferred for OS-level sandboxing.
Post-Viva Questions
1. Share the command used to install the C compiler in your virtual machine.
2. Describe the steps you followed to write, compile, and run a C program.
3. Mention any errors encountered during installation or compilation and how you
solved them.
4. Explain the purpose of using gcc or g++ in Linux environments.
5. Reflect on the advantages of testing programs inside a VM instead of the host OS.
6. Suggest how the setup can be extended to support other languages or tools.
Experiment No:3 Installing Google App Engine and Creating Hello World
Web Applications in Java and Python
AIM
To install Google App Engine and develop basic web applications such as "Hello World"
using both Java and Python, and deploy them using GAE's standard environment.
SOFTWARE REQUIRED
 Google Cloud SDK (includes App Engine deployment tools)
 Python 3.x
 Java JDK 11+
 Apache Maven (for Java)
 Text Editor: VS Code / Notepad++ / IntelliJ
 Web Browser (Chrome or Firefox)
 Internet Connection
 Operating System: Windows/Linux/Mac
BACKGROUND THEORY
Google App Engine (GAE) is a fully managed serverless platform by Google Cloud. It supports
various programming languages like Python, Java, Go, Node.js, etc., and allows you to build
scalable web apps and APIs without managing infrastructure.
 GAE Standard Environment: Predefined runtimes and sandbox environment
 GAE Flexible Environment: Custom runtimes with Docker container support
Both Python and Java web apps can be deployed using GAE by creating an app.yaml
configuration and using the gcloud app deploy command.
PART A: PYTHON – HELLO WORLD APP
ALGORITHM
1. Install Python and Google Cloud SDK
2. Create a GCP project and initialize SDK
3. Build a simple Flask web app
4. Create app.yaml file
5. Deploy using gcloud app deploy
LONG CODE (Python: main.py)
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
 return "Hello, World! This is a Python app on GAE."
if __name__ == '__main__':
 app.run()
app.yaml
runtime: python39
entrypoint: gunicorn -b :$PORT main:app
handlers:
 - url: /.*
 script: auto
requirements.txt
Flask==2.3.3
gunicorn==21.2.0
SAMPLE OUTPUT (Python)
When accessed via browser after deployment:
Hello, World! This is a Python app on GAE.
PART B: JAVA – HELLO WORLD APP
ALGORITHM
1. Install Java JDK and Apache Maven
2. Create a Maven project for GAE Java App
3. Add dependencies and servlet code
4. Create appengine-web.xml configuration
5. Deploy using gcloud app deploy
CODE (Java: Servlet-based App)
HelloServlet.java
import java.io.IOException;
import javax.servlet.http.*;
public class HelloServlet extends HttpServlet {
 @Override
 public void doGet(HttpServletRequest req, HttpServletResponse resp)
 throws IOException {
 resp.setContentType("text/plain");
 resp.getWriter().println("Hello, World! This is a Java app on GAE.");
 }
}
web.xml
<web-app>
 <servlet>
 <servlet-name>HelloServlet</servlet-name>
 <servlet-class>HelloServlet</servlet-class>
 </servlet>
 <servlet-mapping>
 <servlet-name>HelloServlet</servlet-name>
 <url-pattern>/</url-pattern>
 </servlet-mapping>
</web-app>
appengine-web.xml
<appengine-web-app xmlns="http://appengine.google.com/ns/1.0">
 <runtime>java11</runtime>
</appengine-web-app>
SAMPLE OUTPUT (Java)
Hello, World! This is a Java app on GAE.
RESULT
Python and Java-based web applications were successfully created and deployed on Google
App Engine. The experiment demonstrated deploying scalable cloud applications using
standard GAE tools and configurations.
PRE VIVA QUESTIONS
1. State the purpose of using Google App Engine in cloud platforms.
2. Mention supported languages in GAE Standard Environment.
3. Describe the role of the app.yaml or appengine-web.xml file.
4. List tools required to deploy Python and Java apps in GAE.
5. Explain the difference between runtime and entrypoint.
6. Identify the use of gcloud commands in deployment.
POST VIVA QUESTIONS
1. Describe the output observed after deployment.
2. Explain how GAE handles incoming web requests.
3. Share your experience using Python Flask vs Java Servlets on GAE.
4. Mention challenges faced during app deployment and how you resolved them.
5. Suggest extensions like form handling, database integration, or API creation.
6. Evaluate the performance and scalability benefits of serverless deployment.
Experiment 5: Simulate a Cloud Scenario Using CloudSim
with a Custom Scheduling Algorithm
AIM
To simulate a cloud environment using CloudSim and implement a custom VM scheduling
algorithm not present in the default library.
SOFTWARE REQUIRED
 CloudSim 3.0.3 or later
 Java JDK 8+
 Eclipse IDE
 Windows/Linux/Mac OS
BACKGROUND THEORY
CloudSim is a simulation toolkit for modeling cloud computing environments. It supports
modeling of data centers, hosts, VMs, and scheduling policies.
Custom scheduling allows you to override existing policies like TimeShared or SpaceShared
by implementing your own logic in VmScheduler.
ALGORITHM
1. Set up a datacenter and host.
2. Create a list of VMs.
3. Define a custom VM scheduler by extending VmScheduler.
4. Deploy cloudlets.
5. Observe performance under the custom policy.
CODE (Custom VmSchedulerRoundRobin.java)
public class VmSchedulerRoundRobin extends VmScheduler {
 private int currentIndex = 0;
 public VmSchedulerRoundRobin(List<? extends Pe> pelist) {
 super(pelist);
 }
 @Override
 public boolean allocatePesForVm(Vm vm, List<Double> mipsShare) {
 Map<String, List<Double>> peAllocationMap = getPeAllocationMap();
 List<Pe> peList = getPeList();

 if (currentIndex >= peList.size()) {
 currentIndex = 0;
 }
 List<Double> allocatedMips = new ArrayList<>();
 allocatedMips.add(mipsShare.get(0)); // Single MIPS value
 peAllocationMap.put(vm.getUid(), allocatedMips);

 currentIndex++;
 return true;
 }
 @Override
 public void deallocatePesForVm(Vm vm) {
 getPeAllocationMap().remove(vm.getUid());
 }
}
SAMPLE OUTPUT
Custom Round Robin VM Scheduling Simulation Started...
Datacenter created
VMs allocated in Round Robin manner
Simulation ended successfully.
RESULT
A custom Round-Robin VM scheduler was successfully implemented and tested using
CloudSim, simulating cloud workload management.
PRE VIVA QUESTIONS
1. State the role of CloudSim in cloud computing research.
2. Mention different types of schedulers in CloudSim.
3. Describe the difference between VM allocation and scheduling.
4. Identify components in a CloudSim simulation.
5. Explain the structure of a data center in CloudSim.
POST VIVA QUESTIONS
1. Explain how your custom algorithm improves over existing ones.
2. Suggest cases where Round-Robin may fail.
3. Share simulation results and observed performance.
4. Describe how cloudlets were assigned.
5. Propose future enhancements for your scheduler.
Experiment 6: Transfer Files from One Virtual Machine
to Another
AIM
To transfer files between two virtual machines within the same or different networks.
SOFTWARE REQUIRED
 Two Virtual Machines (e.g., VirtualBox or VMware)
 Ubuntu or CentOS
 OpenSSH or SCP utility
BACKGROUND THEORY
Transferring files between VMs is a common need in cloud environments. Tools like scp,
rsync, or shared folders can be used. SSH must be enabled on the target VM.
ALGORITHM (Using SCP)
1. Ensure both VMs are connected (via bridged/NAT network).
2. Enable SSH on the destination VM.
3. Use the scp command from the source VM:
4. scp /path/to/file user@destination_ip:/path/to/target/
CODE / COMMAND
# On Source VM
scp /home/user1/report.txt user2@192.168.1.15:/home/user2/
SAMPLE OUTPUT
report.txt 100% 10KB 2.0MB/s 00:00
RESULT
File was successfully transferred between virtual machines using the SCP protocol over SSH.
PRE VIVA QUESTIONS
1. State the need for file transfer between VMs.
2. Mention protocols used for secure file transfer.
3. Differentiate between shared folders and scp.
4. Explain the role of IP configuration in VM communication.
5. List tools used for file transfer in Linux.
POST VIVA QUESTIONS
1. Describe any issue faced during the file transfer.
2. Suggest alternative methods for large file transfers.
3. Share a real-world use of VM-to-VM transfer.
4. Describe how to make transfers permanent or automated.
5. Suggest improvements to your process.

Experiment 7: Launch a Virtual Machine Using TryStack
(OpenStack Demo)
AIM
To launch a virtual machine instance using the online OpenStack demo platform TryStack.
SOFTWARE REQUIRED
 Browser
 Internet access
 OpenStack TryStack credentials
BACKGROUND THEORY
TryStack is an OpenStack-powered sandbox environment that allows users to try OpenStack
without setup. It provides an easy GUI to launch virtual machines.
ALGORITHM
1. Login to https://trystack.org
2. Navigate to Instances > Launch Instance
3. Choose image (e.g., Ubuntu)
4. Configure flavor, security group, and key pair
5. Launch and access the instance
LONG STEPS
Step 1: Open TryStack
Step 2: Select Horizon > Compute > Instances
Step 3: Click “Launch Instance”
Step 4: Fill form:
 Name: MyVM
 Image: Ubuntu 20.04
 Flavor: m1.small
 Keypair: TryStackKey
 Network: public
Step 5: Click Launch
SAMPLE OUTPUT
Instance "MyVM" - ACTIVE
IP: 172.24.4.5
Status: Running













RESULT
A virtual machine instance was successfully launched on TryStack using OpenStack Horizon
Dashboard.
PRE VIVA QUESTIONS
1. Explain the purpose of using TryStack.
2. State the function of a keypair in OpenStack.
3. Mention types of OpenStack services.
4. Differentiate between flavor and image.
5. Define an instance in OpenStack.
POST VIVA QUESTIONS
1. Describe how the instance was configured.
2. Explain how to connect to the instance.
3. Share the role of networking in launching VMs.
4. Suggest improvements to OpenStack UI.
5. Mention security concerns in cloud VM creation.

Experiment 8: Install Hadoop Single Node Cluster and
Run Word Count
AIM
To install Hadoop on a single-node cluster and run a basic WordCount MapReduce
application.
SOFTWARE REQUIRED
 Ubuntu Linux
 Java JDK 8
 Hadoop 3.x
 Terminal / Bash
BACKGROUND THEORY
Hadoop is a framework for distributed storage and processing using MapReduce.
Single-node cluster setup allows standalone testing of HDFS and MapReduce.
ALGORITHM
1. Install Java
2. Download and configure Hadoop
3. Format HDFS namenode
4. Start Hadoop services
5. Run WordCount using input files in HDFS
LONG CODE / COMMANDS
# Install Java
sudo apt install openjdk-8-jdk
# Download Hadoop
wget https://downloads.apache.org/hadoop/common/hadoop-3.3.6/hadoop-3.3.6.tar.gz
tar -xvzf hadoop-3.3.6.tar.gz
mv hadoop-3.3.6 hadoop
# Configure environment
nano ~/.bashrc
# Add:
export HADOOP_HOME=~/hadoop
export PATH=$PATH:$HADOOP_HOME/bin
# Format namenode
hdfs namenode -format
# Start Hadoop (Standalone)
start-dfs.sh
start-yarn.sh
# Create input/output dirs
hdfs dfs -mkdir /input
hdfs dfs -put sample.txt /input
# Run Word Count
hadoop jar $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-examples-*.jar
wordcount /input /output
# Get result
hdfs dfs -cat /output/part-r-00000
SAMPLE OUTPUT
Hadoop 3
MapReduce 2
Word 5
RESULT
A Hadoop single-node cluster was successfully configured, and the Word Count application
ran and produced expected output using HDFS and MapReduce.
PRE VIVA QUESTIONS
1. State the purpose of HDFS in Hadoop.
2. Describe the role of NameNode and DataNode.
3. Mention the importance of Java in Hadoop.
4. Identify the output of Map and Reduce stages.
5. List directories used by Hadoop by default.
POST VIVA QUESTIONS
1. Explain the process of uploading input to HDFS.
2. Interpret the output of Word Count.
3. Share issues faced during Hadoop installation.
4. Suggest performance tuning ideas.
5. Describe the difference between standalone and cluster mode.
INNOVATIVE APPROACHES TO THE EXPERIMENT
1. AI-Powered Chatbot Web App on GAE (Python)
Innovation: Integrate a simple chatbot using rule-based logic or open-source AI models in
Python (Flask), hosted on GAE.
Features:
 User input through a web form
 Respond with predefined or dynamically generated answers
 Can be extended to use NLP libraries like NLTK or spaCy
Use Case:
 Educational bots for campus queries, FAQs, or mini health assistants.
2. Real-Time Feedback Collector with Firestore Backend (Python or Java)
Innovation: Extend the Flask or Java app to collect user feedback and store it in Google
Cloud Firestore.
Features:
 Feedback form
 Store responses in Firestore database
 Admin dashboard to view entries (optional)
Use Case:
 Collect feedback from students, faculty, or conference attendees in real time.
3. Weather Forecast App using REST API Integration
Innovation: Consume third-party weather APIs (like OpenWeatherMap) in your web app
and deploy it on GAE.
Features:
 Input: City name
 Output: Current temperature, humidity, condition
 Use: requests in Python or HttpURLConnection in Java
Use Case:
 Embed into campus dashboards or geography-related courses.
4. Resume Parser / Analyzer App (Python with NLP)
Innovation: A web app where users upload their resume, and the system extracts key details
(skills, education, etc.) using NLP and displays analysis.
Features:
 File upload
 Text extraction using pdfminer or docx
 NLP-based parsing and keyword extraction
 Hosted on GAE
Use Case:
 Placement offices or career support centers.
5. COVID-19 Safety Guidelines Checker (Multi-language Support)
Innovation: A simple app that displays current COVID-19 safety guidelines and supports
multilingual output using translation APIs.
Features:
 Select language dropdown
 Dynamic translation via Google Translate API
 GAE handles the backend and static hosting
Use Case:
 Public health awareness in multilingual regions.
6. AI-Based Text Sentiment Analyzer (Python)
Innovation: A GAE-deployed Flask app where users enter a sentence and get a sentiment
score (positive/negative/neutral) using NLP.
Features:
 Input box
 Backend using TextBlob or VADER
 Output sentiment classification
Use Case:
 Educational demo of AI or integration into feedback systems.
7. Expense Tracker App with Google Sheets API Integration
Innovation: Web app where users enter their daily expenses and the backend stores it in
Google Sheets via Sheets API.
Features:
 Expense form
 Authentication via OAuth (optional)
 Updates cloud-based sheet in real time
Use Case:
 Budget tracking for students, clubs, or teams.
8. Python + Java Hybrid App via REST API
Innovation: Deploy a Python Flask app on GAE that communicates with a Java-based
backend microservice via HTTP.
Features:
 Separation of UI (Python) and logic (Java)
 Demonstrates service-to-service communication on cloud
Use Case:
 Introduces students to microservice architecture on GCP.
Why These Are Innovative:
 🔗 Integration of APIs and cloud services
 🧠 Application of AI/ML/NLP in web apps
 🔐 Use of real-time databases and authentication
 📊 Enhancing user interactivity and analytics
