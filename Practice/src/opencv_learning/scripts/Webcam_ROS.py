#!/usr/bin/env python
import numpy as np
import cv2 
import rospy

from sensor_msgs.msg import Image
from std_msgs.msg import String
from cv_bridge import CvBridge,CvBridgeError
import sys

bridge = CvBridge()
def image_handler(Ros_Image):
    global bridge
    try:
        cv_image = bridge.imgmsg_to_cv2(Ros_Image,'bgr8')
    except CvBridgeError as error:
        rospy.loginfo(error)
    cv2.imshow('Webcam',cv_image)
    cv2.waitKey(1)

def subscriber(): 
    rospy.init_node('Image_Receiver',anonymous= True)
    sub = rospy.Subscriber('/image',Image,image_handler) 
    rospy.spin()

if __name__ == '__main__':
    try:
        subscriber()
    except rospy.ROSInterruptException:
        pass
