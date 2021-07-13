#!/usr/bin/env python
import rospy 
from std_msgs.msg import String 
from Robot_Messages.srv import TestSrv

def handler(request):
    rospy.loginfo("Joint Name is:{} , Effort is:{}".format(request.a,request.b))
    boolean = 1
    return boolean

def server():
    rospy.init_node('Server',anonymous=True)
    rospy.Service('/tester_service',TestSrv,handler)
    rospy.loginfo('Server started...')

    rospy.spin()


if __name__ == "__main__":
    try:
        server()
    except rospy.ROSInterruptException():
        pass