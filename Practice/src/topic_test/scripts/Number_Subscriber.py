#!/usr/bin/env python

import rospy
from std_msgs.msg import Int64
from std_srvs.srv import SetBool

counter = 0

def handler(request):
    if request.data:
        global counter
        counter =0
        return True, "Counter reset"
    else:
        return False, "Counter not reset"
def callback(msg):
    global counter
    rospy.loginfo("I heard ")
    counter = counter + msg.data
    rospy.loginfo(counter)

def subscriber():
    rospy.init_node('Number_Subscriber',anonymous= True)
    
    rospy.Subscriber('Number_Exchange',Int64,callback)
    
    service = rospy.Service('/reset',SetBool,handler)
    rospy.spin()

if __name__ == "__main__":
    try:
        subscriber()
    except rospy.ROSInterruptException:
        pass