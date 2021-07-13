#include <ros/ros.h>
int main(int argc,char **argv)
{
    ros::init(argc,argv, "First_CPP_Node");
    // Using node handle to start the node
    ros::NodeHandle nh;
    ROS_INFO("First ROS Node started");
    ros::Rate rate(10);
    while (ros::ok)
    {
        ROS_INFO("Its Working");
        rate.sleep();
    }
    
}