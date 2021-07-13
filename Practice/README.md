> # ROS_Projects
All ROS Python Related Projects

# ROS Documentation

## Initialising ROS:
Ros core has to be initialised/run on a terminal before starting any other process.
command : roscore

## Topics:
Nodes communicate on a topic in ros.

> rostopic bw     display bandwidth used by topic <br>
> rostopic delay display delay for topic which has header <br>
> rostopic echo   print messages to screen <br>
> rostopic find   find topics by type<br>
> rostopic hz     display publishing rate of topic <br>
> rostopic info   print information about active topic <br>
> rostopic list   print information about active topics <br>
> rostopic pub    publish data to topic <br>
> rostopic type   print topic type <br>

Resource: http://wiki.ros.org/rostopic

### Rqt Graph:
Rqt graphs can be used to visualise the nodes, subscribers etc on a given topic.

## Nodes:
They can be considered as the basic building block of any ROS based application. they can contain publishers, subscribers , services and clients.

Initialising a node: 
> rospy.init_node(‘node_name’, anonymous=True)<br>

*anonymous command creates a randomised name for the node to keep its name  unique.
### Publisher: 
A publisher publishes the required data on a rostopic.

Initialising a publisher: 
> publisher = rospy.Publisher(‘topic_name’, data_type, queue_size=10).<br>


Publishing data using a publisher:
> publisher.publish(message)<br>

Data can be published at a particular rate using the rate function in rospy as follows:
> Rate = rospy.rate(Hz)<br>
> Rate.sleep()     //Creates a delay of desired time in the loop.<br>

### Subscriber: 
It subscribes to a particular topic and receives the data (Messages) published on it.

Initialising a subscriber: 
> rospy.Subscriber('topic_name', data_type, callback_function)

A subscriber requires a predefined callback function for processing the received data.

Node Activation:
A node can be activated in the terminal using the following command:
> rosrun /topic_name node_name

Spin functionality:
It runs the subscriber/receiver node until its terminated by the used (it makes the node persistent).

Command: rospy.spin()
Messages:
Notes communicated on a topic using messages, they can be considered as the data packets used for communication within ROS.Standard message types: string, float, boolean, array, char, time etc.

Resource: http://wiki.ros.org/std_msgs

Publishing a message on a topic:
A message can be published on a running topic without the need of initialising the node (Given the data types of the message and topic are the same).

> rostopic pub -r rate /topic_name  message/type message

The publishing of data through a messages depends on the parameters accepted by it.
Eg: A String message can only transfer string data type.<br>
> Message = String() <br>
> Message.data = ‘It’s a string.’<br>

For creating a message data type, an object of the required datatype has to be instantiated.
## Service:
Services are used for bi-directional data flow on a topic. eg: Suppose a weather service is created and a client makes a request, the server can receive the request as well as transmit the desired data back to the client.

Resource: http://wiki.ros.org/Services

### Server:
A ROS server accepts the client’s request and transmits the data accordingly.

Initialisation:
> service = rospy.Service('/Service_Name',Service_Type,handler)

Handler function is required to handle the service request and transmit/return the desired data. It receives the client request as the parameter and returns the appropriate data.

There are predefined services in ROS like Addition of the input numbers, but can also be customised.
### Client:
A client transmits data/request to the server and waits until it gets a response from it.

Hence the services in ROS are used for quick communication purposes, as it suspends the client activity until it gets a response from the server.

Initialisation:
> client_name = rospy.ServiceProxy("/",Service_Type) <br>
> response = Service_Name (requested_data) <br>

## Log:
Logging functionality can be used to print/log a message/command on the running terminal.

### Logging info:
> rospy.loginfo(data)

## Custom Messages:
Custom message definitions can be created in ROS in the .msg format.

Example:

> float64 temprature <br>
> bool motor_status <br>
> string debug_msg <br>


The message parameters can be set using the variable names specified in the .msg file.
*The message file has to be created in the msg folder of a package.
Eg: message.temprature = 102.04

### Custom Message Compilation:
Custom message definitons need to be compiled in the CMakeLists.txt and package.xml file.

Changes to be made in CMakeLists.txt:

1: Adding message generation in find_package

> find_package(catkin REQUIRED COMPONENTS <br>
>   roscpp<br>
>   rospy<br>
>   std_msgs<br>
>   message_generation     # Adding message generation in find_package<br>
> )<br>

2. Adding message file name in add_message_file (The message file should be in msg folder of the package)

> add_message_files(<br>
>   FILES<br>
>   HardwareStatus.msg  # Adding message file name in add_message_file<br>
> )

3. Uncommenting generate_messages 

> generate_messages(<br>
>   DEPENDENCIES<br>
>   std_msgs <br>
> )

4. Adding message_runtime to catkin_depend

> catkin_package(<br>
>   #INCLUDE_DIRS include<br>
>   #LIBRARIES Robot_Messages<br>
>   CATKIN_DEPENDS roscpp rospy std_msgs message_runtime<br>
>   #DEPENDS system_lib<br>
> )<br>


### Changes to be made in Package.xml:

1. Adding message_generation and message_runtime:

> <build_depend>message_generation</build_depend> <br>
> <exec_depend>message_runtime</exec_depend> <br>

## Custom Service File:
Custom service files definitions can be created in ROS in the .srv format.
*The message file has to be created in the srv folder of a package.

Example: <br>
> float64 temprature<br>
> '---'<br>
> string debug_msg<br>

The datatype declared above the ‘---’ is the input data the service is expecting and the datatype declared below ‘---’ is the output data of the service.

Custom Service Compilation:

### Changes to be made in CMakeLists.txt:
1. Adding srv file name in add_service_file:

> add_service_files( <br>
>    FILES<br>
>    CircleArea.srv	# Adding srv file name in add_service_file<br>
>    BatterySrv.srv	<br>
>  )


## ROS Parameters:<br>
ROS Parameters are the global variables in a ROS Environment, i.e. they are accessible by all the nodes.

To access a parameter inside a node: <br>
> Variable_name = rospy.get_param(“parameter_name”)

Note: Launching the node without setting the parameter prior will lead to an error, as it needs to be set before accessing it.

To initialise a new parameter using a node:<br>
> rospy.set_param(“parameter_name”,data)


Command line tools can be used to access parameters.<br>
Resource: http://wiki.ros.org/rosparam

## Launch File:
A launch file is used to launch all the services and nodes specified in it.
Advantage: The user doesn’t have to run all the nodes, services and parameters one by one.

*Launchfile folders are also called as bringup folders.

Launch files are written in xml format.

Creating a launch file :

"<launch>
	<param name = “parameter_name” type = “data_type” value=”value”/>
	<node name = “node_name” pkg=”package_name” type = “node_name.py”/>
</launch>"

Running a launch file: 
> roslaunch launch_package_name launch_file_name.launch

## ROS Bag:
Ros bag is used to record data of an event and play it in the same order.

Recording an event:

> rosbag record topic_name

Playback an event:

> rosbag info file_name.bag

## ROS OpenCV:
For exchanging image(OpenCV) messages within ROS environment, CvBridge is used for the conversion process.

### Installation:

#### 1. Dependencies : 
sudo apt-get install libfontconfig1-dev libdbus-1-dev libfreetype6-dev libudev-dev libicu-dev libsqlite3-dev libxslt1-dev libssl-dev libasound2-dev libavcodec-dev libavformat-dev libswscale-dev libgles2-mesa-dev libxcb-icccm4-dev libxcb-image0-dev libxcb-keysyms1-dev libxcb-xinerama0-dev libprotobuf-dev libleveldb-dev libsnappy-dev libhdf5-serial-dev protobuf-compiler libopenblas-dev liblapack-dev libopenblas-dev liblapack-dev libgflags-dev libgoogle-glog-dev liblmdb-dev cmake cmake-gui gfortran liblapack-dev libblas-dev libatlas-base-dev libarpack2-dev libarpack++2-dev

#### 2. Install OpenCV CMake version,
	Resource: https://docs.opencv.org/trunk/d7/d9f/tutorial_linux_install.html
#### 3. CvBridge install:
	sudo apt-get install ros-(ROS version name)-cv-bridge 
	sudo apt-get install ros-(ROS version name)-vision-opencv 
#### 4. Usage:
	from cv_bridge import CvBridge,CvBridgeError


### Image Conversion:
OpenCV stores image in numpy arrays (8bit format).<br>

ROS Messages require images in bgr8 format, hence CvBridge is used for this conversion process.



Converting cv image to ros image:

> ros_image = CvBridge().cv2_to_imgmsg(image,’bgr8’)

After the conversion, the ros_image can be published using Image message from sensor_msg library.

Converting ros image to cv image:

> cv_image = CvBridge().imgmsg_to_cv2(Ros_Image,'bgr8')

# Ros Serial Arduino
## Installation
1. Install Arduino IDE:<br>
	https://www.arduino.cc/en/guide/linux

2. Follow the steps given in the link below:<br>
	http://wiki.ros.org/rosserial_arduino/Tutorials/Arduino%20IDE%20Setup

## Establishing Serial COM between Arduino and ROS:
>	rosrun rosserial_arduino serial_node.py _port:=/dev/ttyUSB0

## Nodes and Topics
Nodes in ROS-Serial are very similar to the nodes in default ros ecosystem
**Importing Necessary Libraries**
> #include <ros.h> <br>
> #include <std_msgs/Float32.h>

**Starting ROS NodeHandle**
> ros::NodeHandle nh;<br>

**Creating an instance of the message**
> std_msgs::Float32 laser_msg;

**Initialising a Publisher**
>ros::Publisher pub("Laser_MSG_Topic",&laser_msg);

**Initialising and Advertising a node**
>void setup() <br>
>{	<br>
>nh.initNode();<br>
>nh.advertise(pub);<br>
>}

**Publishing Data values**
> void loop()<br>
> { laser_msg.data = 18.0;
>	pub.publish(&laser_msg);<br>
>	nh.spinOnce(); //Similar to rospy.spin() <br>
>	}

## Services 
ROS Serial doesn't work when using the Arduino as a server.
This issue is specific to ROS Melodic.

Eg: A server used for calling /ApplyJointEffort service of agzebo

**Importing Necessary Libraries**
>#include<ros.h> <br>
>#include<gazebo_msgs/ApplyJointEffort.h>

**Starting ROS NodeHandle**
> ros::NodeHandle nh;<br>

**Creating an instance of the message**
> std_msgs::Float32 laser_msg;

**Initialising a the Service**
>ros::ServiceClient<gazebo_msgs::ApplyJointEffort::Request,gazebo_msgs::ApplyJointEffort::Response>client("/gazebo/apply_joint_effort");

**Initialising and Advertising the publisher**
>void setup() <br>
>{	<br>
>nh.initNode();<br>
>nh.serviceClient(client);<br>
>}

**Creating and Publishing Service Request and Accepting Response**
void loop() {<br>
>//Defining Requests and Responses  <br>
>gazebo_msgs::ApplyJointEffort::Request req;<br>
>gazebo_msgs::ApplyJointEffort::Response res;<br>
>
> //Sending a request with specified arguments<br>
>req.joint_name = "Engine";<br>
>req.effort = 10.0;<br>
>req.start_time = nh.now();<br>
>req.duration = ros::Duration(1,1);<br>
>client.call(req,res);<br>
>
>nh.spinOnce();<br>
>}                 

### Array messages Exception (ROS-Serial Specific)
While sending array messages in ROS-Serial, the length of the array must be predefined within the message param.
 
Eg: Publishing ranges in Laser Scan Messages
> //Defining The Array <br>
>float distance_values[100]<br>
>
>//Defining the length of array in scan message
>distance_ultra.ranges_length = 18; <br>
>
> //Assigning the array as a message param
>distance_ultra.ranges = distance_values;
