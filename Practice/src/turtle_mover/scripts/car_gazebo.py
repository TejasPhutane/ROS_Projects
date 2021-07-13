#!/usr/bin/env python
import rospy
from gazebo_msgs.srv import ApplyJointEffort
import sys,tty,termios

force_values = {'d':['Steering',-0.1],
                'a':['Steering',0.1],
                'w':['Engine',-1.0],
                's':['Engine',1.0]}

def get_key():
    ''' Sets terminal in raw input mode and returns the entered key'''
    tty.setraw(sys.stdin.fileno())
    rlist = [sys.stdin]
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''
    # Draining the previous attributes 
    termios.tcsetattr(sys.stdin,termios.TCSADRAIN,termios.tcgetattr(sys.stdin))
    return key

def car_mover():
    rospy.init_node("Force_Giver")
    car_service = rospy.ServiceProxy('/gazebo/apply_joint_effort',ApplyJointEffort)
    rate = rospy.Rate(30)
    rospy.loginfo("Control Service Started....") 
    rospy.loginfo("----------------------------")
    
    while not rospy.is_shutdown():
        key = get_key()
        
        if key:
            
            start_time = rospy.Time.now()
            duration = rospy.Duration(0.5)

            response = car_service(force_values[key][0],force_values[key][1],start_time,duration)
            # rospy.loginfo(response.success)
        
        
        rate.sleep()

if __name__ == "__main__":
    try:
        car_mover()
    except rospy.ROSInterruptException():
        pass