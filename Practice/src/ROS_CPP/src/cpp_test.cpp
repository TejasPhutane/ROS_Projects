#include<ros/ros.h>
#include<std_msgs/String.h>

int main(int argc,char **argv)
{   
    ros::init(argc,argv,"Publisher");
    ros::NodeHandle nh;
    ros::Publisher pub = nh.advertise<std_msgs::String>("CPP_Topic",10);
    ros::Rate rate(3);

    while (ros::ok)
    {
        std_msgs::String data_packet;
        data_packet.data = "Helllloooo adad";
        pub.publish(data_packet);
        rate.sleep();
    }
}