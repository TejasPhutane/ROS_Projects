#include<ros/ros.h>
#include<std_msgs/String.h>
void callback_receiver(const std_msgs::String msg)
{
    ROS_INFO("Message recieved: %s",msg.data.c_str());
}

int main(int argc,char **argv)
{
    ros::init(argc,argv,"CPP_Subscriber_Node");
    ros::NodeHandle nh;
    ros::Subscriber sub = nh.subscribe("/CPP_Radio",1000,callback_receiver);
    ros::spin();
}