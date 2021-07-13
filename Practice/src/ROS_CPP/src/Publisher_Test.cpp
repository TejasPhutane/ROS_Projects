#include<ros/ros.h>
#include<std_msgs/String.h>

int main(int argc,char **argv)
{
    ros::init(argc,argv,"Publisher Node");
    ros::NodeHandle nh;
    ros::Publisher pub = nh.advertise<std_msgs::String>("CPP_Radio",10);
    ros::Rate rate(3);

    while (ros::ok)
    {
        std_msgs::String data_packet;
        // nh.loginfo("Publisher Node Started");
        pub.publish(data_packet);
        rate.sleep();
    }
}