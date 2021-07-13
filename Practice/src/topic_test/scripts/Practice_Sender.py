#!/usr/bin/env python

import rospy 
from std_msgs.msg import String
from Robot_Messages.srv import CircleArea

def handler(request):
    radius = request.radius
    area = 3.14*radius*radius
    return area


def Publisher():
    rospy.init_node('Tester',anonymous= True)
    # pub = rospy.Publisher('Messaging',String,queue_size= 10)
    # rate = rospy.Rate(5)
    rospy.Service('/weather_service',CircleArea,handler)
    rospy.loginfo("---Weather Service started---")
    rospy.spin()


if __name__=='__main__':
    try:
        Publisher()
    except rospy.ROSInterruptException():
        pass 
