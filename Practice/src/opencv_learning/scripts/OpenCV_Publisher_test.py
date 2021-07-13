#!/usr/bin/env python
import numpy as np
import rospy
import cv2

from cv_bridge import CvBridge,CvBridgeError
from sensor_msgs.msg import Image

def publisher():
    cv_image = cv2.imread('/home/anish/git/ROS_Projects/catkin_ws_2/src/opencv_learning/scripts/Barca1.jpg')
    bridge = CvBridge()
    ros_image = bridge.cv2_to_imgmsg(cv_image,encoding='bgr8')
    
    rospy.init_node('Image_Publisher',anonymous=True)
    pub = rospy.Publisher('Image_Publisher',Image,queue_size=10)
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        rospy.loginfo('Publishing Image....')
        pub.publish(ros_image)  
        a = cv2.waitKey(0)&0xFF
        rospy.loginfo("A is{}".format(a))  
        rate.sleep()


if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass