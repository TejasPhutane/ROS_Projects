#!/usr/bin/env python

import rospy 
from std_msgs.msg import String
from Robot_Messages.srv import CircleArea

def Subscriber():
    rospy.init_node('Client',anonymous= True)
    rospy.wait_for_service('/weather_service')
    
try:
    area_service = rospy.ServiceProxy("/weather_service",CircleArea)
    response = area_service(1)
    rospy.loginfo(response)

if __name__=='__main__':
    try:
        Subscriber()
    except rospy.ROSInterruptException():
        pass 
