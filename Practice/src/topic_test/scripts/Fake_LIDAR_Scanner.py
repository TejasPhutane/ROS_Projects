#!/usr/bin/env python  
import roslib
roslib.load_manifest('learning_tf')
import rospy
from std_msgs.msg import Header
import tf
import turtlesim.msg

def header_publisher():
    rospy.init_node('head')
    pub = rospy.Publisher('/header_publisher',Header,queue_size=10)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        msg = Header()
        msg.frame_id = "Hello"
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        header_publisher()
    except rospy.ROSInternalException:
        pass