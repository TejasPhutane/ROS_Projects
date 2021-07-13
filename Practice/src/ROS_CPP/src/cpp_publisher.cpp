#include <ros/ros.h>
#include <std_msgs/String.h>
int main(int argc,char **argv)
{   //Initialising the node
    ros::init(argc,argv,"Publisher_CPP");
    // Initialising the node handle
    ros::NodeHandle nh;
    // Creating a publisher and advertising the service
    ros::Publisher pub = nh.advertise<std_msgs::String>("CPP_Radio",10);
    ros::Rate rate(3);
    while (ros::ok)
    {
        // Creating a instance of string
        std_msgs::String data_packet;
        data_packet.data = "Publishing CPP Message";
        pub.publish(data_packet);
        rate.sleep();
    }
    
}