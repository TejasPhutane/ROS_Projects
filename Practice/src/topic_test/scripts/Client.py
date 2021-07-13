#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64
from rospy_tutorials.srv import AddTwoInts

rospy.init_node('client_node',anonymous= True)
# rospy.wait_for_service('/adder',AddTwoInts)
rospy.wait_for_service('/adder')
try:
    adder_service = rospy.ServiceProxy("/adder",AddTwoInts)
    response = adder_service(7,8)

    rospy.loginfo('Sum is:'+ str(response.sum))
except rospy.ROSInterruptException as e:
    rospy.loginfo('Service failed:'+str(e))