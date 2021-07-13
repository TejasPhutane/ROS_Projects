#!/usr/bin/env python
import rospy
# from geometry_msgs.msg import Twist
from std_msgs.msg import Int32
import sys,tty,termios
brightness_values = {'w':[10.0],
                     's':[-10.0]}

def get_key():
    tty.setraw(sys.stdin.fileno())
    r_list = [sys.stdin]

    if r_list:
        key = sys.stdin.read(1)
    else:
        key = ''
    termios.tcsetattr(sys.stdin,termios.TCSADRAIN,termios.tcgetattr(sys.stdin))
    return key
def glow():
    pub = rospy.Publisher('led_glower',Int32, queue_size= 10)
    rospy.init_node('speeder', anonymous=True)
    rate = rospy.Rate(60)
    while not rospy.is_shutdown():
        key = get_key()
        brightness = Int32()
        if key:
            brightness.data = brightness_values[key][0]
            pub.publish(brightness)
    
        rate.sleep()

if __name__ == '__main__':
    try:
        glow()
    except rospy.ROSInterruptException:
        pass