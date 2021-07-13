#include<ros/ros.h>
#include<rospy_tutorials/AddTwoInts.h>

int main(int argc,char **argv)
{
    ros::init(argc,argv,"add_two_ints_client");
    ros::NodeHandle nh;
    ros::ServiceClient client = 
    nh.serviceClient<rospy_tutorials::AddTwoInts>("add_two_ints");
    rospy_tutorials::AddTwoInts srv;
    srv.request.a = 1;
    srv.request.b = 3;
    if (client.call(srv))
        ROS_INFO("It Works");
    else
        ROS_INFO("Doesnt work");
    
}

// int main(int argc ,char **argv)
// {
//     ros::NodeHandle nh;
//     ros::init(argc,argv,"Client");
//     ros::ServiceClient client = nh.serviceClient<rospy_tutorials::AddTwoInts>("add_two_ints");
//     rospy_tutorials::AddTwoInts srv;
//     srv.request.a  =1;
//     srv.request.b = 11;
//     if (client.call(srv))
//         ROS_INFO("It Works");
//     else
//         ROS_INFO("Doesnt work");
// }