#!/usr/bin/env python 
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Char
import sys,select,termios,tty

force_values = {'w': [[2.0,0.0,0.0],[0.0,0.0,0.0]],
                's': [[-2.0,0.0,0.0],[0.0,0.0,0.0]],
                'a': [[0.0,0.0,0.0],[0.0,0.0,2.0]],
                'd': [[0.0,0.0,0.0],[0.0,0.0,-2.0]]}

def callback(msg):
    if msg.data:
        rospy.loginfo("The Key entered is: {}".format(str(msg.data)))



def publisher():
    rospy.init_node('Publisher',anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)

    # Adding a Input topic Subscriber
    sub = rospy.Subscriber("Key_Input",Char,callback= callback)

    rate = rospy.Rate(30)
    rospy.loginfo('Starting keyboard service....')
    rospy.spin()
    # while not rospy.is_shutdown():
        # Get the entered key value
        # key = getKey()
        # twist = Twist()
        
        # # If a key is pressed, check its value in the dictionary and give output accordingly
        # if key:
        #     rospy.loginfo("Entered Key is: {}".format(key))

        #     twist.linear.x = force_values[key][0][0]
        #     twist.linear.y = force_values[key][0][1]
        #     twist.linear.z = force_values[key][0][2]
            
        #     twist.angular.x = force_values[key][1][0]
        #     twist.angular.y = force_values[key][1][1]
        #     twist.angular.z = force_values[key][1][2]

        #     rospy.loginfo(twist)

        # pub.publish(twist)
        # rate.sleep()

if __name__ == "__main__":
    
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass