#!/usr/bin/env python
import rospy 
from Robot_Messages.srv import BatterySrv

LED = 0

def handler(request):
    global LED
    # rospy.loginfo("Entered Percentage is:"+str(request.Percentage))
    if request.Percentage == 25:
        rospy.loginfo("[1,0,0,0]")
        return True
    if request.Percentage == 50:
        rospy.loginfo("[1,1,0,0]")
        return True
    if request.Percentage == 75:
        rospy.loginfo("[1,1,1,0]")
        return True
    if request.Percentage == 100:
        rospy.loginfo("[1,1,1,1]")
        return True

    if request.Percentage != 100 & request.Percentage != 75 & request.Percentage != 50 & request.Percentage != 25 &request.Percentage != 125:
        # rospy.loginfo("[1,1,1,1]")
        return False


def server():
    rospy.init_node('server_node')
    service = rospy.Service('/battery_percentage',BatterySrv,handler)
    rospy.loginfo('Battery server started')
    rospy.spin()

if __name__ == '__main__':
    try:
        server()
    except rospy.ROSInterruptException:
        pass