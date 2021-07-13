#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Float32MultiArray


def speed():
    pub = rospy.Publisher('/turtle',Twist, queue_size= 10)
    rospy.init_node('speeder', anonymous=True)
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        # twist = Twist()
        # twist.linear.x = 2.0
        # twist.linear.y = 0.0
        # twist.linear.z = 0.0
        
        # twist.angular.x = 0.0
        # twist.angular.y = 0.0
        # twist.angular.z = 2.0

        # rospy.loginfo(twist)
        # pub.publish(twist)
        array = Float32MultiArray()
        array.data= [10.0]
        array.layout.dim = 1

        pub.publish(array)
        rate.sleep()

if __name__ == '__main__':
    try:
        speed()
    except rospy.ROSInterruptException:
        pass