#!/usr/bin/env python
import rospy 
from Robot_Messages.srv import BatterySrv

Charge = 0

rospy.init_node('battery_discharging')
rospy.wait_for_service('/battery_percentage')

charging_rate = rospy.Rate(0.571428571)
discharging_rate = rospy.Rate(0.3)

try:
    battery_service = rospy.ServiceProxy('/battery_percentage',BatterySrv)

    if Charge == 0
        while Charge <= 100:
            Charge +=25 
            feedback = battery_service(Charge)
            charging_rate.sleep()
            rospy.loginfo(feedback.Return)
            
    # if Charge == 100:
    #     while Charge >= 0:
    #         feedback = battery_service(Charge)
    #         discharging_rate.sleep()  
    #         Charge -= 25
    # rospy.spin() 
except rospy.ROSInterruptException as e:
    rospy.loginfo('Service failed:'+str(e))