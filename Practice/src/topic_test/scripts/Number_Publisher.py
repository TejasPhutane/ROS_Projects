#!/usr/bin/env python

import rospy
from std_msgs.msg import Int64

def publisher():
    rospy.init_node('Number_Publisher',anonymous= True)
    pub = rospy.Publisher('Number_Exchange',Int64,queue_size=10)
    rate = rospy.Rate(5)
    while not rospy.is_shutdown():
        msg = Int64()
        msg.data = 10
        rospy.loginfo(msg)
        pub.publish(msg)
        rate.sleep()

if __name__ == "__main__":
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass