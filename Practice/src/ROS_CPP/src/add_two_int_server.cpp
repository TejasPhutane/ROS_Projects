#include<ros/ros.h>
#include<rospy_tutorials/AddTwoInts.h>

bool handler(rospy_tutorials::AddTwoInts::Request &req,
            rospy_tutorials::AddTwoInts::Response &res)
{
    int sum = req.a + req.b;
    ROS_INFO("Sum of %d,%d = %d",(int)req.a,(int)req.b,(int)sum);
    res.sum = sum;
    return true;
}

int main(int argc,char **argv)
{
    ros::init(argc,argv,"Adder_Service_Node");
    ros::NodeHandle nh;
    ros::ServiceServer server = nh.advertiseService("add_test_srv",
        handler);
    ros::spin();
}