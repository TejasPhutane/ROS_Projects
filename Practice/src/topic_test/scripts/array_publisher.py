#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32MultiArray

counter = 0

# def callback(msg):
#     global counter
#     rospy.loginfo("I heard ")
#     counter = counter + msg.data
#     rospy.loginfo(counter)

def subscriber():
    rospy.init_node('Number_Subscriber',anonymous= True)
    pub = rospy.Publisher('/array_pub',Float32MultiArray,queue_size=10)
    
    while not rospy.is_shutdown():
        msg = Float32MultiArray()
        msg.data = [1.0]
        msg.layout.dim = [1]
        pub.publish(msg)


if __name__ == "__main__":
    try:
        subscriber()
    except rospy.ROSInterruptException:
        pass