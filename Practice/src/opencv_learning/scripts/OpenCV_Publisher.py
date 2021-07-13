#!/usr/bin/env python
import numpy as np
import rospy
import cv2

from sensor_msgs.msg import Image
from std_msgs.msg import String
from cv_bridge import CvBridge,CvBridgeError
import sys

bridge = CvBridge()
cap = cv2.VideoCapture(0)
def publisher():
    global bridge,cv_img

    rospy.init_node('Image_Publisher')
    
    pub = rospy.Publisher('/image',Image,queue_size=10)
    
    rate = rospy.Rate(30)
    rospy.loginfo('Service Started')    
    while not rospy.is_shutdown():
        ret,frame = cap.read()
        ros_img = bridge.cv2_to_imgmsg(frame,'bgr8')
        pub.publish(ros_img)
        rate.sleep()

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass

