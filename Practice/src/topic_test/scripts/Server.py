#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64
from rospy_tutorials.srv import AddTwoInts

def handler(request):
    summation = request.a + request.b
    rospy.loginfo("Sum of a:"+str(request.a) + "and b:" + str(request.b) + " is :" + str(summation))
    return summation

def server():
    rospy.init_node('server_node')
    service = rospy.Service('add_test_srv',AddTwoInts,handler)
    rospy.loginfo('Addition server started')
    rospy.spin()

if __name__ == '__main__':
    try:
        server()
    except rospy.ROSInterruptException:
        pass
