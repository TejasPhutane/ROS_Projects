# Gazebo Documentation

# Creating/Simulating models
For basic simulation purposes, use the Gazebo GUI.
## Launching Gazebo
#### Use terminal and input 
	gazebo

# Gazebo Joints
Joints are used to connect two bodies and give their connection specified degrees of freedom.
To apply force on joint, use the apply force tab on the left hand side of the GUI and give the joint desired force.

### Note
Gazebo version 7 crashes when using the joint creator window, so save your file before opening the joint windowt.

## Using Gazebo with ROS
### Use-case
ROS can be integrated with gazebo to send cross-platform messages, services etc.
eg: 1. Car simulation in Gazebo can be controlled using an arduino keypad using ROS Serial.
    2. It can be used to bridge the gap between the real world and a simulated one.

### Setup
For using gazebo with ros, include `gazebo_ros` tag while creating a catkin package.
eg:
	catkin_create_pkg gazebo_test rospy roscpp std_msgs gazebo_ros

### Launching gazebo using ROS launch
	roslaunch gazebo_ros empty_world.launch

### Using ROS Services to control a simulation
To see a list of all the advertised services, use
	rosservice list
All the services containing `/gazebo` prefix can be used for communication between ROS and Gazebo.

#### Resetting a simulation using ROS Service
	rosservice call /gazebo/reset_simulation

#### Applying Joint efforts using a ROS Service
	rosservice call /gazebo/ApplyJointEffort

- The `Teleop Car` model in this repository uses the keyboard keys as the input for driving a simulated car in Gazebo.
- A similar version of `Teleop Car` is controlled using ROS Serial.