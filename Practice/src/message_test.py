#!/usr/bin/env python
import rospy
from Robot_Messages.msg import HardwareStatus

if __name__ == "__main__":
    try:
        rospy.init_node('custom_message_publisher',anonymous= True)
        pub = rospy.Publisher('Custom_Message_Testing',HardwareStatus,queue_size= 10)
        rate = rospy.Rate(10)
        while not rospy.is_shutdown():
            msg = HardwareStatus()
            msg.temprature = 30
            msg.motor_status = True
            msg.debug_msg = "It works"
            rospy.loginfo(msg)
            pub.publish(msg)
            rate.sleep()
    except rospy.ROSInterruptException:
        pass