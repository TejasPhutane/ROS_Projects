#!/usr/bin/env python

import rospy
from Robot_Messages.srv import TestSrv


rospy.init_node('client_node',anonymous= True)
# rospy.wait_for_service('/adder',AddTwoInts)
rospy.wait_for_service('/tester_service')
try:
    adder_service = rospy.ServiceProxy("/tester_service",TestSrv)

    start_time = rospy.Time.now()
    duration = rospy.Duration(5)
    # msg_a = '12'
    msg_b = 2
    response = adder_service(start_time,msg_b)

    rospy.loginfo('Sum is:'+ str(response.success))
except rospy.ROSInterruptException as e:
    rospy.loginfo('Service failed:'+str(e))