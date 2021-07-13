#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

def mover():
    pub = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size= 10)
    rospy.init_node('mover',anonymous= True)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        vel = Twist()
        
        vel.angular.x = 0.0
        vel.angular.y = 0.0
        vel.angular.z = 1.8

        vel.linear.x = 2.0
        vel.linear.y = 0.0
        vel.linear.z = 0.0

        rospy.loginfo(vel)
        pub.publish(vel)
        rate.sleep()

if __name__ == '__main__':
    try:    
        mover()
    except rospy.ROSInterruptException:
        pass