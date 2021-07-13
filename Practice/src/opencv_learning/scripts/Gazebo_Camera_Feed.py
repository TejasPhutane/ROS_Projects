#! /usr/bin/env python

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge,CvBridgeError
import cv2
Bridge = CvBridge()

def callback(ROS_Image):
    global Bridge
    try:
        cv_image = Bridge.imgmsg_to_cv2(ROS_Image,'bgr8')
    except CvBridgeError as error:
        rospy.loginfo(error)
    cv2.imshow('Gazebo_Camera_Data',cv_image)
    cv2.imwrite('~/catkin_ws/src/opencv_learning/scripts/Template_Gazebo.jpg',cv_image)
    cv2.waitKey(1)

def image_subscriber():
    rospy.init_node("Image_Reiever",anonymous=True)
    rospy.Subscriber("/rrbot/camera1/image_raw",Image,callback=callback)
    rospy.spin()

if __name__ == "__main__":
    try :
        image_subscriber()
    except rospy.ROSInterruptException():
        pass
