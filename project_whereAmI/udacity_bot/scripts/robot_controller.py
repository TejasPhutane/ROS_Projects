#!/usr/bin/env python

import rospy
from geometry_msgs.msg  import Twist
from nav_msgs.msg import Odometry
from math import pow,atan2,sqrt
from tf.transformations import euler_from_quaternion
import math

class MoveRobot():

    def __init__(self):
        
        #Initializing ROS node
        rospy.init_node('move_robot', anonymous=True)
        #Publish/Subscribe ROS topics
        self.velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.pose_subscriber = rospy.Subscriber('/odom', Odometry,self.PoseCallback)       
        self.rate = rospy.Rate(5)

    ### Getting robot position
    def PoseCallback(self,pose_message):
    
        self.odom_x = round(pose_message.pose.pose.position.x,4)
        self.odom_y = round(pose_message.pose.pose.position.y,4)
        #print self.odom_x,self.odom_y
        rot_q = pose_message.pose.pose.orientation
        _,_,theta = euler_from_quaternion ([rot_q.x, rot_q.y, rot_q.z, rot_q.w])
        
        self.odom_theta = round(theta,4)
        #changing interval from [-pi, pi] to [0, 2*pi]
        # if  self.odom_theta < 0:
        #     self.odom_theta = self.odom_theta + 2*math.pi
        #print self.odom_theta
        #self.position = [self.odom_x,self.odom_y,self.odom_theta]   
        #print self.position
        # rot = self.odom_theta
        # if rot < 0:
        #     self.total_odom = 2*math.pi + rot
        # else:
        #     self.odom_theta = rot

    # Rotate robot using cmd_vel topic
    def rotate(self, param_degree, param_speed, param_dir):

        obj_velocity_mssg = Twist()

        # Store start orientation
        start_degree = self.odom_theta
        current_degree = self.odom_theta

        
        var_loop_rate = rospy.Rate(10)
        # Set the speed of rotation according to param_dir
        if(param_dir == 'a'):
            obj_velocity_mssg.angular.z = math.radians(
                abs(int(param_speed)))  # Anticlockwise
        else:
            # Clockwise
            obj_velocity_mssg.angular.z = (-1) * \
                math.radians(abs(int(param_speed)))

        # Rotate till desired angle is reached
        degree_rotated = 0.0

        while not rospy.is_shutdown():
            if((round(degree_rotated) < math.radians(abs(param_degree)))):
                self.velocity_publisher.publish(obj_velocity_mssg)

                var_loop_rate.sleep()

                current_degree = self.odom_theta
                degree_rotated = abs(current_degree - start_degree)
                print('Degree Rotated: {}'.format(math.degrees(degree_rotated)))
            else:
                break

        # Stop the Turtle after the desired angle is reached
        obj_velocity_mssg.angular.z = 0.0
        self.velocity_publisher.publish(obj_velocity_mssg)
        print('Angle Reached')
    
    def move_forward(self,speed, distance, is_forward):
        #declare a Twist message to send velocity commands
        velocity_message = Twist()
        #get current location 
        x0 = self.odom_x
        y0 = self.odom_y

        if (speed > 0.4):
            print 'speed must be lower than 0.4'
            return

        if (is_forward):
            velocity_message.linear.x =abs(speed)
        else:
        	velocity_message.linear.x =-abs(speed)

        distance_moved = 0.0
        loop_rate = rospy.Rate(10) # we publish the velocity at 10 Hz (10 times a second)    
    

        while not rospy.is_shutdown():
                rospy.loginfo("Robot moves forwards")
                self.velocity_publisher.publish(velocity_message)

                loop_rate.sleep()
                
                #distance_moved = abs((self.odom_x-x0) )
                distance_moved = abs(math.sqrt(((self.odom_x-x0) ** 2) + ((self.odom_y-y0) ** 2)))  
                rospy.loginfo(distance_moved)               
                if  not (distance_moved<distance):
                    rospy.loginfo("reached")
                    break
        
        #finally, stop the robot when the distance is moved
        velocity_message.linear.x =0
        self.velocity_publisher.publish(velocity_message)
    
    # Go to Goal Based on P Controller
    #TODO: PID controller 
    def go_to_goal(self,x_goal, y_goal):
        velocity_message = Twist()

        while (True):
            K_linear = 0.2 
            distance = abs(math.sqrt(((x_goal-self.odom_x) ** 2) + ((y_goal-self.odom_y) ** 2)))

            linear_speed = distance * K_linear


            K_angular = 1.0
            desired_angle_goal = math.atan2(y_goal-self.odom_y, x_goal-self.odom_x)
            angular_speed = (desired_angle_goal-self.odom_theta)*K_angular

            velocity_message.linear.x = linear_speed
            velocity_message.angular.z = angular_speed

            self.velocity_publisher.publish(velocity_message)
            
            #print velocity_message.linear.x
            #print velocity_message.angular.z
            print 'x=', self.odom_x, 'y=',self.odom_y

            if (distance <0.01):
                break
        velocity_message.linear.x = 0
        velocity_message.angular.z = 0
        self.velocity_publisher.publish(velocity_message)

if __name__ == '__main__':
    try:
        #Testing our function
        robot = MoveRobot()
        rospy.sleep(2)
        #rospy.spin()
        robot.move_forward(0.2,1.0,True)
        # robot.rotate(90,30,'a')
        # rospy.sleep(2)
        # robot.rotate(90,30,'a')
        # rospy.sleep(2)
        # robot.rotate(90,30,'a')
        # rospy.sleep(2)
        # robot.rotate(90,30,'a')
    except rospy.ROSInterruptException: 
       pass

 
    